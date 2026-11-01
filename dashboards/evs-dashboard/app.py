"""
EVS Notes Dashboard
-------------------
Multi-page Flask site for the four illustrated weekly EVS notebooks.

Routes:
  GET  /                  dashboard: full syllabus, two-level expandable topic tree
  GET  /week/<int:num>    a week's notebook, with prev/next/back-to-dashboard nav
  GET  /pdf/<file>        week 5-6 PDF notebooks, inline (embedded viewer)
  GET  /download/<file>   original self-contained standalone HTML (offline copy)

Run:
    pip install -r requirements.txt
    python app.py
    open http://127.0.0.1:4000
"""

import json
import os
import random
from flask import Flask, abort, flash, redirect, render_template, request, send_from_directory, url_for

app = Flask(__name__)
app.secret_key = "evs-dashboard-local-dev-key"  # only used for flash messages; local tool, not public-facing

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(BASE_DIR, "notes")  # original standalone files, for download
DATA_DIR = os.path.join(BASE_DIR, "data")

# Quiz question bank: {"1": {"s1": {"label": ..., "questions": [...]}, ...}, "2": {...}, ...}
# Parsed from the user-supplied MCQ bank; 5 questions per topic, each question has
# level (Bloom's), q (stem), options (4, in bank order), answer (0-based index into options).
with open(os.path.join(DATA_DIR, "quiz_bank.json"), encoding="utf-8") as f:
    QUIZ_BANK = json.load(f)

# One entry per week. `topics` is a two-level tree: each top-level topic has an
# id (anchor on the week page), a label, a one-line summary of what it covers, and
# (where the notes had subheadings) a list of subtopics with their own id/label/summary.
# This is what powers the dashboard's expandable syllabus.
WEEKS = {
    1: {
        "num": 1,
        "title": 'Foundations: Earth Systems & Ecosystem Ecology',
        "desc": "What environmental science actually is, Earth's four spheres, ecosystem structure, energy flow (10% law, GPP/NPP), biogeochemical cycles, and ecological succession.",
        "accent": '#2f6b4f',
        "accent_dk": '#204a37',
        "download_file": "week1.html",
        "topics": [
            {
                "id": 's1',
                "label": 'Environmental science, studies & engineering',
                "summary": '"Environmental science, environmental studies, and environmental engineering are basically the same subject with different names." They aren\'t — they differ in what…',
                "subtopics": [],
            },
            {
                "id": 's2',
                "label": 'Scope & the multidisciplinary approach',
                "summary": 'Environmental problems are never confined to one department of knowledge. A single issue — water scarcity, say — is simultaneously a hydrology problem, a law-and-policy…',
                "subtopics": [
                    {"id": 's2-1', "label": 'Why environmental studies matters', "summary": 'Protection: guides conservation of ecosystems, biodiversity, and natural resources. Public health: connects pollution and degradation directly to human disease burden.…'},
                    {"id": 's2-2', "label": 'Major environmental issues — quick reference', "summary": 'Cause → effect, for the headline issues of this decade Issue Primary cause Key effects Climate change CO₂, CH₄, N₂O from fossil fuels & deforestation Global warming…'},
                ],
            },
            {
                "id": 's3',
                "label": 'Earth as a life-support system',
                "summary": 'Earth supports life because four interacting "spheres" each supply something no organism can live without: air, water, food, and solid ground. The word sphere literally…',
                "subtopics": [
                    {"id": 's3-1', "label": '3.1 The Atmosphere — five layers, and why each behaves differently', "summary": 'Air temperature with altitude is not one smooth gradient — it zig-zags, because different layers are heated by different sources. The troposphere is warmed from below by…'},
                    {"id": 's3-2', "label": '3.2 The Hydrosphere & the water cycle', "summary": "The hydrosphere is all the water on, under, and above Earth's surface: oceans (~97%), lakes/rivers (~2%), and — critically — only about 1% is fresh, accessible water for…"},
                    {"id": 's3-3', "label": '3.3 The Geosphere', "summary": 'The solid Earth, from inner core to crust. It has an interior structure that directly drives surface geology: Inner core — solid iron-nickel. Outer core — liquid…'},
                    {"id": 's3-4', "label": '3.4 The Biosphere', "summary": 'The sum of every ecosystem where life exists — forests, deserts, oceans, wetlands, grasslands — plus the living organisms in them: producers (plants), consumers…'},
                ],
            },
            {
                "id": 's4',
                "label": 'Ecosystems: structure, types, components',
                "summary": 'An ecosystem is a dynamic complex of living organisms (biotic) and their non-living surroundings (abiotic), interacting as a system that exchanges energy and cycles…',
                "subtopics": [
                    {"id": 's4-1', "label": 'Natural vs. artificial ecosystems', "summary": 'A forest or river is self-sustaining and evolves without human input. A garden or aquarium is artificial — it needs continuous human management (watering, feeding…'},
                    {"id": 's4-2', "label": 'Biotic and abiotic components', "summary": 'Biotic (living) Abiotic (non-living) Producers, consumers, decomposers, microorganisms Light, temperature, water, soil, air, minerals, pH, salinity These two sets are…'},
                ],
            },
            {
                "id": 's5',
                "label": 'Levels of ecological organization',
                "summary": 'Ecology studies life at a nested set of scales. Each level is built entirely out of the level below it — nothing new is added except interaction . Notice: the arrows…',
                "subtopics": [],
            },
            {
                "id": 's6',
                "label": 'Food chains, food webs & ecological pyramids',
                "summary": 'A food chain is a single linear path of energy transfer: Grass → Grasshopper → Frog → Snake → Eagle . A food web is the full network of overlapping, interconnected food…',
                "subtopics": [
                    {"id": 's6-1', "label": 'Ecological pyramids', "summary": 'Three ways to draw the same food chain, each revealing something different: Pyramid type Measures Shape Numbers Count of organisms per level Usually upright, but can…'},
                ],
            },
            {
                "id": 's7',
                "label": 'Energy flow in an ecosystem',
                "summary": 'Energy flow is unidirectional : Sun → Producers → Primary consumers → Secondary consumers → Tertiary consumers. Unlike nutrients (Section 8), energy is never recycled…',
                "subtopics": [
                    {"id": 's7-1', "label": "The 10% Law (Lindeman's Law)", "summary": 'When energy passes from one trophic level to the next, only about 10% is stored as new biomass; the remaining 90% is lost , mostly to respiration and incomplete…'},
                    {"id": 's7-2', "label": 'Gross vs. Net Primary Production', "summary": 'GPP = NPP + R GPP (Gross Primary Production) is the total energy plants capture via photosynthesis. Plants then spend some of that on their own respiration ( R ) just to…'},
                    {"id": 's7-3', "label": 'Two energy-flow models', "summary": 'Model Idea Limitation Single-channel One straight line: producers → herbivores → carnivores Too simple; ignores dead organic matter (detritus) Y-shaped (two-channel)…'},
                ],
            },
            {
                "id": 's8',
                "label": 'Biogeochemical cycles',
                "summary": 'Energy flows one way and leaves the system as heat — it can never be recycled. Matter is different: the same carbon, nitrogen and phosphorus atoms are used, released…',
                "subtopics": [
                    {"id": 's8-1', "label": 'Carbon cycle', "summary": 'photosynthesis pulls CO₂ out of the air; respiration and combustion push it back in . Fossil-fuel burning taps a carbon store that took millions of years to…'},
                    {"id": 's8-2', "label": 'Nitrogen cycle', "summary": 'Nitrogen makes up 78% of the atmosphere, yet plants cannot use it in that gaseous (N₂) form directly — a key point that surprises many learners. "Since the air is 78%…'},
                    {"id": 's8-3', "label": 'Phosphorus cycle', "summary": 'Carbon and nitrogen both have an atmospheric gas phase (CO₂, N₂) — they can move through the air. Phosphorus has no gas phase ; it only moves by the weathering of rock…'},
                    {"id": 's8-4', "label": 'Decomposition — the process that keeps every cycle turning', "summary": 'Fragmentation (detritivores like earthworms break up dead matter) → leaching (water dissolves out soluble nutrients) → catabolism (microbial enzymes break complex…'},
                ],
            },
            {
                "id": 's9',
                "label": 'Ecological succession',
                "summary": 'Ecological succession is the gradual, predictable replacement of one biological community by another over time, ending (usually) in a stable climax community . Notice…',
                "subtopics": [
                    {"id": 's9-1', "label": 'The four stages of any succession', "summary": 'Nudation — a bare area forms (volcanic eruption, landslide, fire, flood, glacier retreat). Invasion — pioneer species arrive (lichens/mosses in primary; weeds/grasses in…'},
                    {"id": 's9-2', "label": 'Two theories of what "climax" even means', "summary": 'Theory Proposed by Claim Monoclimax F. E. Clements Within a region, all land converges on one climate-determined climax type Polyclimax A. Tansley Climax vegetation…'},
                ],
            },
            {
                "id": 's10',
                "label": 'Stability, resilience & human impact',
                "summary": 'Stability = resisting change in the first place. Resilience = bouncing back after a disturbance. These are not the same property — an ecosystem can be low-stability but…',
                "subtopics": [
                    {"id": 's10-1', "label": 'Feedback loops', "summary": 'Negative feedback (stabilizing): more prey → more predators → predators reduce prey → population settles back down. This is what keeps most ecosystems in dynamic…'},
                    {"id": 's10-2', "label": 'Human pressures, summarised', "summary": 'Pressure Mechanism of damage Deforestation Habitat loss + disrupted water cycle + lost carbon sink + soil erosion Pollution Toxins enter food chains and accumulate at…'},
                ],
            },
            {
                "id": 'test',
                "label": 'Self-test checklist',
                "summary": "Close the notebook and try each of these without looking back. If you can't, that's exactly the section to reread. Explain why the stratosphere gets warmer with altitude…",
                "subtopics": [],
            },
        ],
    },
    2: {
        "num": 2,
        "title": 'Biodiversity, Conservation, Water Pollution & Disasters',
        "desc": 'Levels of biodiversity, species interactions, extinct/endangered/endemic/rare species, conservation strategies, GM crops, water pollution, and disaster management.',
        "accent": '#a6742d',
        "accent_dk": '#4a3418',
        "download_file": "week2.html",
        "topics": [
            {
                "id": 's1',
                "label": 'Biodiversity — definition & three levels',
                "summary": 'Biodiversity (biological diversity) is the full variety of life on Earth, existing simultaneously at three nested levels: genetic (within a species), species (across a…',
                "subtopics": [
                    {"id": 's1-1', "label": 'Genetic diversity', "summary": 'Variation in genes within one species — different dog breeds, different rice varieties suited to different soils/climates. It is what lets a species adapt to disease…'},
                    {"id": 's1-2', "label": 'Species diversity', "summary": 'Measured by two separate things: richness (how many different species) and evenness (how balanced their populations are). A monoculture field has low richness and low…'},
                    {"id": 's1-3', "label": 'Ecosystem diversity', "summary": 'The range of distinct habitat types in a region — forests, wetlands, deserts, coral reefs. More ecosystem types means more distinct services (carbon storage, water…'},
                ],
            },
            {
                "id": 's2',
                "label": 'Significance & hotspots',
                "summary": 'Why biodiversity matters, by category Value What it looks like Ecological Pollination, decomposition, natural water purification, food-web stability Economic…',
                "subtopics": [],
            },
            {
                "id": 's3',
                "label": 'Threats to biodiversity',
                "summary": 'Threat Mechanism Habitat loss & fragmentation Urbanization/agriculture/dams split ecosystems into small, isolated patches — disrupting migration and breeding Pollution…',
                "subtopics": [],
            },
            {
                "id": 's4',
                "label": 'Species interactions',
                "summary": 'Five patterns describe how any two species in a shared habitat affect one another. The distinguishing question is simple: who benefits, and does the other party gain…',
                "subtopics": [],
            },
            {
                "id": 's5',
                "label": 'Extinct, endangered, endemic, rare',
                "summary": 'These four terms are often used loosely as synonyms for "in trouble." They actually answer four different questions: Does it still exist anywhere? (extinct) · Is it…',
                "subtopics": [],
            },
            {
                "id": 's6',
                "label": 'Conservation strategies',
                "summary": 'In-situ conservation protects species within their natural habitat (national parks, sanctuaries, biosphere reserves) — ecological processes and evolution continue…',
                "subtopics": [
                    {"id": 's6-1', "label": 'Conservation operates at three levels simultaneously', "summary": 'Species level: flagship species (e.g. the Tiger) draw public support and funding; keystone species (e.g. the Asian Elephant) have outsized ecological impact — protecting…'},
                    {"id": 's6-2', "label": 'Key Indian legislation', "summary": 'Act Focus Wildlife Protection Act (1972) Legal basis for national parks/sanctuaries; bans hunting/trade of protected species Forest Conservation Act (1980) Requires…'},
                ],
            },
            {
                "id": 's7',
                "label": 'Genetically modified crops',
                "summary": "Genetic engineering directly inserts a useful gene from one organism into another's DNA — including between completely unrelated species — to introduce a trait that…",
                "subtopics": [
                    {"id": 's7-1', "label": "India's regulatory reality", "summary": 'GM crops are regulated by the Genetic Engineering Appraisal Committee (GEAC) under the Ministry of Environment, requiring multi-stage field trials before commercial…'},
                    {"id": 's7-2', "label": 'Weighing benefits against concerns', "summary": 'Benefits Concerns Higher yield, pest/disease resistance Cross-pollination risk with wild/non-GM relatives Less chemical pesticide use Herbicide-tolerant crops can drive…'},
                ],
            },
            {
                "id": 's8',
                "label": 'Water pollution',
                "summary": 'Water pollution is contamination that makes water unfit for drinking, cooking, cleaning or supporting aquatic life. Sources are either point sources (one identifiable…',
                "subtopics": [
                    {"id": 's8-1', "label": 'Groundwater vs. surface-water pollution', "summary": "Type Sources Why it's hard to fix Groundwater Septic tanks, tanneries, deep-well injection, mining, landfill leachate Once an aquifer is polluted it may stay unusable…"},
                    {"id": 's8-2', "label": 'Types of contaminants', "summary": 'Organic: detergents, food-processing waste, petroleum hydrocarbons, pesticides. Nitrogen & phosphorus compounds: feed algae growth (see eutrophication below). Inorganic…'},
                    {"id": 's8-3', "label": 'Eutrophication — the mechanism worth understanding in full', "summary": "the fish don't die from a toxin — they suffocate. Excess nutrients feed an algae bloom; the algae layer blocks light and eventually dies, and bacteria…"},
                    {"id": 's8-4', "label": 'Biomagnification — a second, separate mechanism', "summary": "Some pollutants (like DDT) are not water-soluble, so an organism's body can't flush them out — they accumulate in fat tissue instead. When a predator eats many prey, it…"},
                ],
            },
            {
                "id": 's9',
                "label": 'Disaster management',
                "summary": 'Disaster management is the cycle of prevention → preparedness → response → recovery , applied to both natural and human-made disasters. Note that this is a cycle, not a…',
                "subtopics": [
                    {"id": 's9-1', "label": 'Floods', "summary": 'Type Trigger Riverine Rivers overflow after prolonged rain or snowmelt Flash Sudden, localized heavy rain, dam breaks, or rapid snowmelt — most dangerous due to lack of…'},
                    {"id": 's9-2', "label": 'Earthquakes', "summary": "Earthquakes are the release of stress that has slowly built up along a fault line as tectonic plates try to move past, apart from, or into one another (recall Week 1's…"},
                    {"id": 's9-3', "label": 'Cyclones', "summary": "Warm ocean water evaporates, rises, and leaves low pressure behind it; surrounding air rushes in to fill that gap. Earth's rotation (the Coriolis effect ) deflects that…"},
                    {"id": 's9-4', "label": 'Landslides', "summary": 'Type Description Rockfall Boulders break loose and tumble down steep slopes Debris flow Fast-moving mix of soil, rock and water Mudslide Saturated soil flows downhill…'},
                ],
            },
            {
                "id": 'test',
                "label": 'Self-test checklist',
                "summary": 'Name the three levels of biodiversity and give one original example of each. State the two conditions a region must meet to qualify as a biodiversity hotspot.…',
                "subtopics": [],
            },
        ],
    },
    3: {
        "num": 3,
        "title": 'Energy Resources, Thermal Pollution & Sustainable Transport',
        "desc": 'Hydroelectric, wind, ocean thermal and geothermal energy, thermal pollution, water management & conservation, and electric / CNG vehicles.',
        "accent": '#2b5f7a',
        "accent_dk": '#122b3a',
        "download_file": "week3.html",
        "topics": [
            {
                "id": 's1',
                "label": 'Hydroelectric power',
                "summary": "Hydroelectric power converts the gravitational potential energy of stored water into electricity: water falls, spins a turbine, the turbine's shaft spins a generator.…",
                "subtopics": [
                    {"id": 's1-1', "label": 'Two methods to harvest hydropower', "summary": 'Method How it works Dam-based Reservoir accumulates water; opening underwater gates releases it through the penstock to spin turbines; output is throttled by how far the…'},
                ],
            },
            {
                "id": 's2',
                "label": 'Wind energy',
                "summary": "Wind energy is indirect solar energy : the sun heats Earth's surface unevenly, creating differences in temperature, density, and pressure that drive air movement. A wind…",
                "subtopics": [],
            },
            {
                "id": 's3',
                "label": 'Ocean thermal energy (OTEC)',
                "summary": 'Ocean Thermal Energy Conversion (OTEC) exploits the temperature difference between sun-warmed surface seawater and cold deep seawater to generate electricity. It…',
                "subtopics": [],
            },
            {
                "id": 's4',
                "label": 'Geothermal energy',
                "summary": "Geothermal energy taps heat stored deep inside the Earth — not a form of solar energy at all, but heat generated by ongoing nuclear fusion-like reactions in the Earth's…",
                "subtopics": [
                    {"id": 's4-1', "label": 'Where geothermal energy is harvested', "summary": 'Magma rising from the mantle creates localized "hot spots." When magma meets underground water, steam forms — and where that steam finds a natural surface opening, you…'},
                ],
            },
            {
                "id": 's5',
                "label": 'Comparing the five renewables',
                "summary": 'All five ultimately do the same last step — spin a shaft, drive a generator. What differs is the upstream energy source and its reliability. Source Upstream energy…',
                "subtopics": [],
            },
            {
                "id": 's6',
                "label": 'Thermal pollution',
                "summary": "Thermal pollution is a sudden rise or fall in a water body's temperature caused by human activity, disrupting the aquatic ecosystem — heat contamination, not chemical…",
                "subtopics": [
                    {"id": 's6-1', "label": 'Causes', "summary": 'Industrial discharges (steel mills, refineries, paper/chemical plants) using water for cooling Power plants (nuclear and coal-fired) — the largest single contributor…'},
                    {"id": 's6-2', "label": 'Consequences — a causal chain, not a list of unrelated symptoms', "summary": 'the oxygen-depletion pathway (top row) and the reaction-rate pathway (bottom text) are two independent mechanisms triggered by the same temperature rise…'},
                    {"id": 's6-3', "label": 'Remedial measures', "summary": 'Measure How it dissipates heat Cooling ponds Shallow reservoirs — evaporation, convection, radiation before discharge Cooling towers (wet) Hot water sprayed downward…'},
                ],
            },
            {
                "id": 's7',
                "label": 'Water management & conservation',
                "summary": "Only 2.5–3% of Earth's water is fresh , and less than 1% is easily accessible for human use. Water management is planning/distributing that scarce resource; conservation…",
                "subtopics": [
                    {"id": 's7-1', "label": 'Principles of water management', "summary": "Principle Meaning Sustainability Today's use must not compromise tomorrow's supply Equity Fair distribution across agriculture, industry, and domestic users Efficiency…"},
                    {"id": 's7-2', "label": 'Conservation methods, with their real-world savings', "summary": 'Method Typical savings Drip / micro-irrigation 28–35% (up to 80% in Israeli smart-drip systems, which also boosted yield 100%) Rainwater harvesting 10–30%+ reduction in…'},
                    {"id": 's7-3', "label": "India's key water policies", "summary": 'National Water Policy (1987, 2002, 2012) — IWRM, rainwater harvesting, groundwater regulation Jal Shakti Abhiyan (2019) — nationwide rainwater harvesting & water-body…'},
                ],
            },
            {
                "id": 's8',
                "label": 'Electric & CNG vehicles',
                "summary": 'An Electric Vehicle (EV) replaces the internal combustion engine with an electric motor powered by a battery. Three core components: battery → controller → electric…',
                "subtopics": [
                    {"id": 's8-1', "label": 'Four types of electric vehicle — the real distinction is "where does the energy come from?"', "summary": 'Type Energy source Can plug into the grid? BEV (Battery EV / All-Electric) Onboard battery only Yes — sole charging method PHEV (Plug-in Hybrid) Battery + combustion…'},
                    {"id": 's8-2', "label": 'Why EVs are more energy-efficient, not just cleaner', "summary": 'EV batteries convert roughly 59–62% of stored energy into actual vehicle movement; a gasoline engine converts only 17–21% — the rest is lost as waste heat through the…'},
                    {"id": 's8-3', "label": 'CNG (Compressed Natural Gas)', "summary": 'CNG is natural gas (mostly methane) compressed to under 1% of its normal volume (3000–3600 psi), making it dense enough to store onboard a vehicle. It is not the same as…'},
                ],
            },
            {
                "id": 'test',
                "label": 'Self-test checklist',
                "summary": 'Explain why a pumped-storage plant is functionally a "battery" for the electrical grid, not a net energy generator. Trace the common final mechanical step shared by…',
                "subtopics": [],
            },
        ],
    },
    4: {
        "num": 4,
        "title": 'Environmental Impact Assessment & Environmental Law',
        "desc": "The EIA process and assessment methodologies, plus India's Environment Protection, Water, Air, Forest and Wildlife Acts.",
        "accent": '#31394f',
        "accent_dk": '#14172a',
        "download_file": "week4.html",
        "topics": [
            {
                "id": 's1',
                "label": 'What is EIA, and why',
                "summary": "Environmental Impact Assessment (EIA) evaluates a proposed project's likely environmental — and social, cultural, and health — consequences before it begins, so that…",
                "subtopics": [
                    {"id": 's1-1', "label": 'Objectives', "summary": 'Identify potential impacts, positive and negative Predict their magnitude and significance Evaluate alternatives to the proposed project Develop mitigation measures…'},
                    {"id": 's1-2', "label": 'Key principles', "summary": 'Participation Stakeholders are involved in the process Transparency Information is open and accessible Accountability Responsibility for outcomes is clearly assigned…'},
                ],
            },
            {
                "id": 's2',
                "label": 'The EIA process, step by step',
                "summary": 'monitoring loops back conceptually into future screening decisions — an EIA doesn\'t end at approval; ongoing monitoring data feeds "adaptive management,"…',
                "subtopics": [
                    {"id": 's2-1', "label": 'Screening — deciding if a full EIA is even needed', "summary": 'Projects are checked against two schedules: Schedule Rule Schedule 1 EIA required in every case (e.g. integrated iron/steel works; thermal power stations ≥300 MW)…'},
                    {"id": 's2-2', "label": 'Scoping — deciding what the EIA should actually study', "summary": 'Identifies key issues and concerns early, by asking: who is concerned, what are their concerns, why, and at what threshold does a change become unacceptable? This…'},
                    {"id": 's2-3', "label": 'Impact assessment — classifying what kind of impact each effect is', "summary": 'Axis Two poles Valence Positive or negative Pathway Direct or indirect Duration Short-term or long-term Recoverability Reversible or irreversible'},
                    {"id": 's2-4', "label": 'Mitigation hierarchy — in strict priority order', "summary": 'Avoid the impact (e.g. relocate the project away from a sensitive site) Minimise the impact (e.g. control emissions) Rehabilitate / restore (e.g. replant vegetation)…'},
                ],
            },
            {
                "id": 's3',
                "label": 'Methodologies for impact assessment',
                "summary": 'From simplest/fastest to most rigorous/slowest Method How it works Strength Limitation Ad hoc Opinion poll, expert opinion, or Delphi (structured questionnaire) method…',
                "subtopics": [],
            },
            {
                "id": 's4',
                "label": 'EIA across sectors',
                "summary": 'Sector What EIA focuses on Typical mitigation Infrastructure (roads, airports, dams) Air/water quality, noise, habitat fragmentation, community displacement Noise…',
                "subtopics": [
                    {"id": 's4-1', "label": 'Persistent challenges', "summary": 'Weak technical/financial capacity in many developing regions Limited public participation in practice, despite it being a stated principle Weak enforcement of EIA…'},
                ],
            },
            {
                "id": 's5',
                "label": 'Roots of Indian environmental law',
                "summary": "India's core environmental legislation didn't emerge from abstract policy planning — it traces to two specific historical triggers worth remembering as anchors for the…",
                "subtopics": [],
            },
            {
                "id": 's6',
                "label": 'The Environment (Protection) Act, 1986',
                "summary": 'Passed under Article 253 of the Constitution, in force from 19 November 1986. 26 sections across four chapters, giving the Central Government broad powers to prevent…',
                "subtopics": [
                    {"id": 's6-1', "label": 'Critical definitions', "summary": 'Environment: water, air, land, and the interrelationships among them and with living beings. Environmental pollutant: any solid, liquid, or gaseous substance present in…'},
                    {"id": 's6-2', "label": 'What the Act actually empowers', "summary": 'Sets standards for air, water, and soil quality with maximum permissible pollutant limits Lets the Central Government restrict or ban industries/operations in specified…'},
                ],
            },
            {
                "id": 's7',
                "label": 'The Water Act, 1974',
                "summary": 'Enacted to prevent and control water pollution and to maintain or restore the "wholesomeness" of water, applicable across all Indian states.',
                "subtopics": [
                    {"id": 's7-1', "label": 'The consent mechanism — how it actually gets enforced', "summary": "the Act's teeth come from a consent-then-verify loop, not just a one-time approval — the State Pollution Control Board (SPCB) retains the right to check…"},
                    {"id": 's7-2', "label": 'Core prohibitions', "summary": "No person may knowingly discharge poisonous/noxious/polluting matter into a stream, well, sewer, or land beyond State Board standards. No person may impede a stream's…"},
                    {"id": 's7-3', "label": 'Roles: Central vs. State Pollution Control Boards', "summary": 'Central PCB State PCB Advises central government on corrective measures; coordinates technical guidance nationally; sets water-quality standards; develops/recognises…'},
                ],
            },
            {
                "id": 's8',
                "label": 'The Air Act, 1981',
                "summary": '50 sections, amended in 1987 to also cover noise pollution . Prevents and controls pollution from solid, liquid, and gaseous emissions — no industrial plant may operate…',
                "subtopics": [],
            },
            {
                "id": 's9',
                "label": 'Forest & Wildlife Protection Acts',
                "summary": '',
                "subtopics": [
                    {"id": 's9-1', "label": 'The Forest (Conservation) Act, 1980', "summary": "Forests aren't protected only because they house wildlife — the Act's justification explicitly rests on forests regulating the hydrological cycle (50–80% of atmospheric…"},
                    {"id": 's9-2', "label": 'The Wildlife (Protection) Act, 1971', "summary": '(Amended 1982, 1986, 1991, 1993, 2002, 2006.) Provides for national parks and sanctuaries, regulates zoos and trade in wild animals, and establishes a Wild Life Advisory…'},
                ],
            },
            {
                "id": 'test',
                "label": 'Self-test checklist',
                "summary": "Explain why EIA's mitigation hierarchy (avoid → minimise → restore → offset) is ordered by decreasing certainty, not arbitrarily. Distinguish Schedule 1 from Schedule 2…",
                "subtopics": [],
            },
        ],
    },
    5: {
        "num": 5,
        "title": "Climate Change, Carbon Sequestration & Environmental Monitoring",
        "desc": "Greenhouse effect from energy balance, climate impacts and causes, carbon sequestration methods, and sensor / IoT / AI environmental health monitoring.",
        "accent": "#2a6f7a",
        "accent_dk": "#1c4d55",
        "download_file": "week5.html",
        "topics": [
            {
                "id": "s1",
                "label": "Global climate change: greenhouse effect, impacts and causes",
                "summary": "The greenhouse effect derived from energy balance, impacts with their mechanisms, and attribution of causes.",
                "subtopics": [
                    {
                        "id": "s1-1",
                        "label": "8.1 The Greenhouse Effect",
                        "summary": "Greenhouse gases let sunlight in but absorb outgoing infrared; the natural effect lifts Earth from about 255 K to 288 K, and human emissions enhance it (global warming).",
                        "page": 2
                    },
                    {
                        "id": "s1-2",
                        "label": "8.2 Impacts of Climate Change",
                        "summary": "Extreme weather, ice-albedo and permafrost feedbacks, ground-level ozone, ocean acidification, sea-level rise (about 8 inches since 1880), deaths and extinctions.",
                        "page": 5
                    },
                    {
                        "id": "s1-3",
                        "label": "8.3 Causes of Global Climate Change",
                        "summary": "Fossil fuels, deforestation, industry, livestock, fertiliser and F-gases versus natural drivers (reflectivity, orbit, sun, volcanoes, natural CO2); human cause above 95%.",
                        "page": 4
                    }
                ],
                "page": 2
            },
            {
                "id": "s2",
                "label": "Carbon sequestration",
                "summary": "Natural sinks, biological, oceanic, physical and chemical methods, and why each stores carbon for as long as it does.",
                "subtopics": [
                    {
                        "id": "s2-1",
                        "label": "9.1 Introduction and Natural Carbon Sinks",
                        "summary": "Long-term CO2 storage; terrestrial and ocean sinks; CO2 up 52% on pre-industrial; oceans absorb more than 25% of human CO2.",
                        "page": 9
                    },
                    {
                        "id": "s2-2",
                        "label": "9.2 Terrestrial Biosequestration",
                        "summary": "Reforestation, afforestation, proforestation, urban forestry, peat, wetlands, cropland and deep soil, with a simple pool model dC/dt = I - kC.",
                        "page": 9
                    },
                    {
                        "id": "s2-3",
                        "label": "9.3 Oceanic Sequestration",
                        "summary": "Iron/urea fertilisation, the sperm-whale pump, mixing layers and seaweed farming, with Liebig's limiting-nutrient idea.",
                        "page": 11
                    },
                    {
                        "id": "s2-4",
                        "label": "9.4 Physical Sequestration",
                        "summary": "BECCS, burial, biochar, deep-ocean injection, geological storage near 1 km (supercritical CO2) and mineral carbonation.",
                        "page": 11
                    }
                ],
                "page": 9
            },
            {
                "id": "s3",
                "label": "Environmental health monitoring: sensors, IoT, AI",
                "summary": "The sense-transmit-store-analyse-act pipeline, remote sensing with NDVI, databases and case studies.",
                "subtopics": [
                    {
                        "id": "s3-1",
                        "label": "7.1 Concept and Key Aspects of Environmental Health Monitoring",
                        "summary": "Systematic collection and analysis of air, water and soil data to detect risks, track trends, guide policy and protect public health.",
                        "page": 15
                    },
                    {
                        "id": "s3-2",
                        "label": "7.2 Role of AI in Environmental Health Monitoring",
                        "summary": "AI forecasting (LSTM air quality), flood early warning, habitat mapping, anomaly detection for poaching and illegal fishing, hazard detection.",
                        "page": 17
                    },
                    {
                        "id": "s3-3",
                        "label": "7.3 Role of IoT in Environmental Health Monitoring",
                        "summary": "IoT sensors: real-time data, remote monitoring, predictive alerts, automated responses, resource management and lower cost.",
                        "page": 15
                    },
                    {
                        "id": "s3-4",
                        "label": "7.4 Tools, Case Studies, Remote Sensing and Databases",
                        "summary": "Air, water, soil, acoustic and wearable sensors, digital twins, e-noses, dashboards; IIT Kharagpur arsenic and Ocean Cleanup; remote sensing, NMIS, ENVIS.",
                        "page": 16
                    }
                ],
                "page": 15
            },
            {
                "id": "test",
                "label": "Summary tables and self-test checklist",
                "summary": "Key relations, numbers to memorise and a checklist to rehearse each derivation.",
                "subtopics": [],
                "page": 18
            }
        ]
    },
    6: {
        "num": 6,
        "title": "Solar, Biomass & Hydrogen Energy (with Hydro, Wind, Ocean, Geothermal & Law recall)",
        "desc": "Solar thermal and PV, biomass fuels, hydrogen and fuel cells, plus quick recall of hydro, wind, OTEC, geothermal, environmental acts and EIA.",
        "accent": "#a4432c",
        "accent_dk": "#7a2f1e",
        "download_file": "week6.html",
        "topics": [
            {
                "id": "s1",
                "label": "Energy resources and solar energy",
                "summary": "Net energy and solar thermal and photovoltaic systems, from physics to numbers.",
                "subtopics": [
                    {
                        "id": "s1-1",
                        "label": "1.1 What Is Energy? Need for Energy Resources",
                        "summary": "Energy from en-ergon (in-work); Franklin, Faraday (1831), Edison, Tesla; energy use as a development indicator.",
                        "page": 2
                    },
                    {
                        "id": "s1-2",
                        "label": "1.2 Types of Energy Resources; Net Energy",
                        "summary": "Renewable versus non-renewable; net energy = useful output minus input; nuclear (low net) versus coal (high net, high CO2).",
                        "page": 2
                    },
                    {
                        "id": "s1-3",
                        "label": "1.3 Solar Energy: Direct and Indirect Use",
                        "summary": "Direct (thermal, photovoltaic) versus indirect solar (fossil fuels, wind, hydro); the sun is abundant, free and free of political barriers.",
                        "page": 3
                    },
                    {
                        "id": "s1-4",
                        "label": "1.4 Passive Solar Energy (Solar Cooker, Daylighting)",
                        "summary": "Solar box cooker (black chamber, glass, insulation, above 100 C), Mount Abu steam kitchen (38,000 people), daylighting with south-facing windows.",
                        "page": 3
                    },
                    {
                        "id": "s1-5",
                        "label": "1.5 Active Solar Energy (Collectors, Furnace, Electricity, Cooling)",
                        "summary": "Flat-plate and concentrating collectors, solar furnace (Mont-Louis, above 3500 C), solar thermal power, solar cooling; T_max = (CS/sigma)^(1/4).",
                        "page": 4
                    },
                    {
                        "id": "s1-6",
                        "label": "1.6 Solar Cells / Photovoltaic Technology",
                        "summary": "Silicon p-n cells, doping, modules and arrays, DC to AC inverter, Bhadla (14,000 acres, 2250 MW), uses from satellites to calculators.",
                        "page": 6
                    }
                ],
                "page": 2
            },
            {
                "id": "s2",
                "label": "Hydroelectric and wind energy",
                "summary": "Dam, pumped-storage and run-of-river hydro; wind turbines; power formulas.",
                "subtopics": [
                    {
                        "id": "s2-1",
                        "label": "2.1 Hydroelectric Power: History and the Dam Principle",
                        "summary": "Dam, reservoir, penstock, turbine, generator; over 18% of world electricity; Fox River 1882; P = eta rho g Q H.",
                        "page": 18
                    },
                    {
                        "id": "s2-2",
                        "label": "2.2 Pumped-Storage Plants and Run-of-River",
                        "summary": "Pumped storage with two reservoirs shifts surplus off-peak power to peak demand; run-of-river for small scale.",
                        "page": 18
                    },
                    {
                        "id": "s2-3",
                        "label": "2.3 Advantages and Disadvantages of Hydroelectric Energy",
                        "summary": "Efficiency above 80%, controllable, 40-50 year life; but cost, landscape change, habitat loss, displacement, floods and disputes.",
                        "page": 18
                    },
                    {
                        "id": "s2-4",
                        "label": "2.4 Wind Energy: Origin, History and Turbine Types",
                        "summary": "Wind as indirect solar; windmill history; turbine components; horizontal versus vertical axis; P = 1/2 rho A v^3 Cp.",
                        "page": 18
                    },
                    {
                        "id": "s2-5",
                        "label": "2.5 Wind Farms, Wind Energy in India, and Advantages/Disadvantages",
                        "summary": "Wind farms; Tamil Nadu and Gujarat lead India (fifth globally); clean and cheap but variable, noisy, harms birds, remote.",
                        "page": 18
                    }
                ],
                "page": 18
            },
            {
                "id": "s3",
                "label": "Ocean thermal and geothermal energy",
                "summary": "OTEC cycles with their Carnot limit; geothermal gradient, wells and trade-offs.",
                "subtopics": [
                    {
                        "id": "s3-1",
                        "label": "3.1 Ocean Thermal Energy: Principle and Requirements",
                        "summary": "Surface-to-deep temperature difference above 20 C (tropics 20-25 C); efficiency depends on the difference; Carnot ceiling about 7%.",
                        "page": 19
                    },
                    {
                        "id": "s3-2",
                        "label": "3.2 OTEC Technologies: Closed-Cycle and Open-Cycle",
                        "summary": "Closed cycle (ammonia, propane, R-134a) versus open cycle (low-pressure flash boiling, desalinated water as by-product).",
                        "page": 19
                    },
                    {
                        "id": "s3-3",
                        "label": "3.3 Advantages and Disadvantages of Ocean Thermal Energy",
                        "summary": "Renewable, reliable, weather-independent, low maintenance; costly, harms marine life, 1-3% efficiency, location-specific.",
                        "page": 19
                    },
                    {
                        "id": "s3-4",
                        "label": "3.4 Geothermal Energy: Origin and Harvesting",
                        "summary": "Heat from Earth's interior (1 C per 35-40 m), magma, hot spots, geysers; injection and production wells, steam turbine, re-injection.",
                        "page": 19
                    },
                    {
                        "id": "s3-5",
                        "label": "3.5 Advantages and Disadvantages of Geothermal Energy",
                        "summary": "Inexhaustible, 24x7 and clean; expensive, location-specific, earthquake risk, releases H2S and SO2.",
                        "page": 19
                    }
                ],
                "page": 19
            },
            {
                "id": "s4",
                "label": "Energy from biomass",
                "summary": "Combustion, digestion, pyrolysis, fermentation; bioethanol, biodiesel and biogas with mass balances.",
                "subtopics": [
                    {
                        "id": "s4-1",
                        "label": "4.1 What Is Biomass? Three Products of Biomass",
                        "summary": "Biomass is organic material (mostly lignocellulosic); three products: bioenergy, biofuels, biogas; indirect solar energy.",
                        "page": 9
                    },
                    {
                        "id": "s4-2",
                        "label": "4.2 Converting Biomass to Heat and Electricity: Combustion, Digestion, Pyrolysis, Fermentation",
                        "summary": "Combustion, anaerobic digestion, pyrolysis (charcoal with about 2x the energy, above 800 F) and fermentation.",
                        "page": 9
                    },
                    {
                        "id": "s4-3",
                        "label": "4.3 Bioethanol",
                        "summary": "Fermentation of sugar and starch crops; E10 and E85 blends; raises octane, cuts greenhouse gases, lowers fuel economy 2-3%.",
                        "page": 11
                    },
                    {
                        "id": "s4-4",
                        "label": "4.4 Biodiesel",
                        "summary": "Fatty-acid esters from oils and fats plus methanol (transesterification); jatropha in India; Indian Railways.",
                        "page": 12
                    },
                    {
                        "id": "s4-5",
                        "label": "4.5 Biogas",
                        "summary": "Anaerobic digestion gives biogas (about 65% methane) and fertiliser digestate; cheap rural fuel; methane leaks warm the climate.",
                        "page": 10
                    },
                    {
                        "id": "s4-6",
                        "label": "4.6 Biomass vs Fossil Fuels; Advantages and Disadvantages of Biomass Energy",
                        "summary": "Biomass renews in years versus millions; carbon-neutral cycle; cheaper than fossil fuels, cuts landfill 60-90%; deforestation and siting issues.",
                        "page": 13
                    }
                ],
                "page": 9
            },
            {
                "id": "s5",
                "label": "Hydrogen energy and the solar-hydrogen cycle",
                "summary": "Production routes, electrolysis thermodynamics, fuel cells, storage and the hydrogen economy.",
                "subtopics": [
                    {
                        "id": "s5-1",
                        "label": "5.1 What Is Hydrogen Energy? Hydrogen as an Energy Carrier",
                        "summary": "Hydrogen is an energy carrier, not a source; light and clean, high energy per kg but low per litre.",
                        "page": 14
                    },
                    {
                        "id": "s5-2",
                        "label": "5.2 Hydrogen Production: Natural Gas Reforming and Thermochemical Water Splitting",
                        "summary": "Steam methane reforming (49% of production; CH4 + 2H2O gives CO2 + 4H2) and thermochemical water splitting (500-2000 C).",
                        "page": 15
                    },
                    {
                        "id": "s5-3",
                        "label": "5.3 Hydrogen Production: Electrolytic Processes",
                        "summary": "PEM electrolyser: anode 2H2O gives O2 + 4H+ + 4e-, cathode 4H+ + 4e- gives 2H2; delta G / nF = 1.23 V.",
                        "page": 15
                    },
                    {
                        "id": "s5-4",
                        "label": "5.4 Solar-Driven and Biological Hydrogen Production",
                        "summary": "Solar-hydrogen cycle (electrolyser, tank, fuel cell); photobiological, photoelectrochemical and solar thermochemical routes; microbial routes.",
                        "page": 16
                    },
                    {
                        "id": "s5-5",
                        "label": "5.5 Hydrogen Fuel Cells, Hydrogen Economy, Applications, Advantages and Disadvantages",
                        "summary": "Fuel cell makes electricity, heat and water; hydrogen economy; refining, fertilisers, homes, vehicles; storage and cost drawbacks.",
                        "page": 16
                    }
                ],
                "page": 14
            },
            {
                "id": "s6",
                "label": "Environmental Protection Acts and EIA",
                "summary": "Stockholm to the 1986 Act, Water, Air, Forest and Wildlife Acts, EIA steps and methods.",
                "subtopics": [
                    {
                        "id": "s6-1",
                        "label": "6.1 Introduction and the Stockholm Conference",
                        "summary": "Stockholm 1972 and World Environment Day (5 June); the Air, Water, Forest and Wildlife Acts.",
                        "page": 20
                    },
                    {
                        "id": "s6-2",
                        "label": "6.2 The Environment (Protection) Act, 1986: Features, Objectives, Provisions and Pollution Control Boards",
                        "summary": "EP Act 1986 after Bhopal (MIC, 1984): Article 253, 26 sections, 4 chapters, umbrella law, standards, pollution control boards.",
                        "page": 20
                    },
                    {
                        "id": "s6-3",
                        "label": "6.3 The Water (Prevention and Control of Pollution) Act, 1974",
                        "summary": "Water Act 1974: SPCB consent to establish and operate, penalties, appellate authority; effluent plant at Ranipet.",
                        "page": 20
                    },
                    {
                        "id": "s6-4",
                        "label": "6.4 The Air (Prevention and Control of Pollution) Act, 1981",
                        "summary": "Air Act 1981 (50 sections; noise added 1987): consent within 4 months, limits on particulates and gases.",
                        "page": 20
                    },
                    {
                        "id": "s6-5",
                        "label": "6.5 The Forest (Conservation) Act, 1980 and the Wildlife Protection Act",
                        "summary": "Forest (Conservation) Act 1980 and Wildlife Protection Act: sanctuaries, national parks, 104/551/86/11 counts.",
                        "page": 20
                    },
                    {
                        "id": "s6-6",
                        "label": "6.6 Environmental Impact Assessment (EIA): Stages, Elements, Scoping, Screening",
                        "summary": "EIA: screening (Schedules 1 and 2), scoping, impact prediction, mitigation, report, decision, monitoring.",
                        "page": 20
                    },
                    {
                        "id": "s6-7",
                        "label": "6.7 EIA Methodologies: Ad hoc, Checklist, Matrix, Network, Overlay",
                        "summary": "Ad hoc (poll, expert, Delphi), checklist (four types), matrix (Leopold), network and overlay (GIS) methods.",
                        "page": 20
                    }
                ],
                "page": 20
            },
            {
                "id": "test",
                "label": "Summary tables and self-test checklist",
                "summary": "Key relations, numbers to memorise and a checklist to rehearse each derivation.",
                "subtopics": [],
                "page": 20
            }
        ]
    },
}
TOTAL_WEEKS = len(WEEKS)

_VALID_DOWNLOADS = {w["download_file"] for w in WEEKS.values()} | {"week5.pdf", "week6.pdf"}


@app.route("/")
def dashboard():
    """Full syllabus: one card per week, each expandable into topics -> subtopics."""
    weeks = [WEEKS[n] for n in sorted(WEEKS)]
    return render_template("dashboard.html", weeks=weeks, total=TOTAL_WEEKS)


@app.route("/week/<int:num>")
def week(num):
    """Render one week's notebook inside the shared nav layout."""
    if num not in WEEKS:
        abort(404)
    w = WEEKS[num]
    return render_template(
        f"week{num}.html",
        current=num,
        total=TOTAL_WEEKS,
        prev_num=num - 1 if num > 1 else None,
        next_num=num + 1 if num < TOTAL_WEEKS else None,
        accent=w["accent"],
    )


@app.route("/pdf/<path:filename>")
def pdf_inline(filename):
    """Serve a week's PDF notebook inline (for the embedded viewer)."""
    if filename not in _VALID_DOWNLOADS or not filename.endswith(".pdf"):
        abort(404)
    return send_from_directory(NOTES_DIR, filename, as_attachment=False)


@app.route("/download/<path:filename>")
def download(filename):
    """Serve the original self-contained standalone HTML file for offline use."""
    if filename not in _VALID_DOWNLOADS:
        abort(404)
    return send_from_directory(NOTES_DIR, filename, as_attachment=True)


def _quiz_topic_picker():
    """Build {week_num: [{id, label, count}, ...]} straight from the question bank,
    in topic order, for rendering the quiz setup page's checkboxes."""
    picker = {}
    for wnum_str in sorted(QUIZ_BANK, key=int):
        wnum = int(wnum_str)
        topics = []
        for tid in sorted(QUIZ_BANK[wnum_str], key=lambda t: int(t[1:])):
            entry = QUIZ_BANK[wnum_str][tid]
            topics.append({"id": tid, "label": entry["label"], "count": len(entry["questions"])})
        picker[wnum] = topics
    return picker


@app.route("/quiz")
def quiz_setup():
    """Quiz setup: pick weeks/topics and how many questions, fully custom."""
    picker = _quiz_topic_picker()
    weeks = [
        {
            "num": n,
            "title": WEEKS[n]["title"],
            "accent": WEEKS[n]["accent"],
            "accent_dk": WEEKS[n]["accent_dk"],
            "topics": picker[n],
            "total_available": sum(t["count"] for t in picker[n]),
        }
        for n in sorted(WEEKS)
    ]
    grand_total = sum(w["total_available"] for w in weeks)
    return render_template("quiz_setup.html", weeks=weeks, grand_total=grand_total)


@app.route("/quiz/start", methods=["POST"])
def quiz_start():
    """Build a randomised, per-attempt-shuffled question set from the selected topics."""
    selected = request.form.getlist("topics")  # e.g. ["1:s1", "1:s3", "2:s7"]
    backtracking = request.form.get("backtracking") == "on"
    try:
        requested_count = int(request.form.get("count", 10))
    except ValueError:
        requested_count = 10

    pool = []
    for token in selected:
        if ":" not in token:
            continue
        wnum_str, tid = token.split(":", 1)
        if wnum_str not in QUIZ_BANK or tid not in QUIZ_BANK[wnum_str]:
            continue
        topic_label = QUIZ_BANK[wnum_str][tid]["label"]
        for i, q in enumerate(QUIZ_BANK[wnum_str][tid]["questions"]):
            pool.append({
                "key": f"{wnum_str}-{tid}-{i}",
                "week": int(wnum_str),
                "topic_id": tid,
                "topic_label": topic_label,
                "level": q["level"],
                "q": q["q"],
                "options": q["options"],
                "answer": q["answer"],
            })

    if not pool:
        flash("Pick at least one topic before starting the quiz.")
        return redirect(url_for("quiz_setup"))

    count = max(1, min(requested_count, len(pool)))
    chosen = random.sample(pool, count)

    # Per-attempt shuffle: randomise each question's option order (and remap the
    # correct index) so the same question never has a predictable answer position.
    quiz_questions = []
    for q in chosen:
        order = list(range(len(q["options"])))
        random.shuffle(order)
        shuffled_options = [q["options"][i] for i in order]
        new_answer = order.index(q["answer"])
        quiz_questions.append({
            "key": q["key"],
            "week": q["week"],
            "topic_id": q["topic_id"],
            "topic_label": q["topic_label"],
            "level": q["level"],
            "q": q["q"],
            "options": shuffled_options,
            "answer": new_answer,
        })

    week_titles = {n: WEEKS[n]["title"] for n in WEEKS}

    return render_template(
        "quiz_run.html",
        questions=quiz_questions,
        pool_size=len(pool),
        requested_count=requested_count,
        selected_topics=selected,
        backtracking=backtracking,
        week_titles=week_titles,
    )


if __name__ == "__main__":
    app.run(debug=True, port=4000)
