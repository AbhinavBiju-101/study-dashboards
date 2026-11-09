from sections import *
import diagrams_b as B

SRC = M("Your syllabus lists this topic but I did not have your lecturer's slides for Module 4, so this is written from the standard textbook treatment (plus the CAT-1 casting question and key). Send the slides and I will align terms and examples to them.", "Source note")

h1 = sec("h1", "H1. Metal Casting", "Pouring molten metal into a mould: sand casting steps, pattern allowances (CAT-1 Q5), types and defects.",
 [("Casting", "shaping metal by pouring it molten into a mould cavity and letting it solidify."), ("Pattern", "replica of the part (made larger) used to make the mould cavity."), ("Mould / cope / drag", "sand cavity; upper / lower box."), ("Core", "insert forming internal cavities."),
  ("Sprue / runner / gate / riser", "vertical channel / horizontal channel / entry to cavity / reservoir that feeds the shrinking casting."), ("Parting line", "joint face between cope and drag."), ("Fettling", "cleaning: cutting gates and risers, grinding."),
  ("Shrinkage / machining / draft allowance", "extra size or taper built into the pattern.")],
 SRC + B.d_sand_mould()
 + OL(["<b>Pattern making</b> (with allowances).", "<b>Moulding:</b> sand rammed round the pattern in cope and drag; pattern removed; cores set; mould closed.", "<b>Melting</b> the metal and <b>pouring</b> through the sprue.", "<b>Solidification</b> and cooling (riser feeds shrinkage).", "<b>Shake-out</b>, fettling, inspection and heat treatment/machining if needed."])
 + H("Pattern allowances — CAT-1 Q5 (answer in the key)")
 + B.d_pattern_allowances()
 + UL(["<b>Shrinkage allowance:</b> the pattern is made larger than the casting because the metal contracts as it cools from the liquid to the solid state; the value depends on the material and its contraction.",
       "<b>Machining allowance:</b> as-cast surfaces are rough; extra stock is added so that it can be machined off to reach the required size and finish.",
       "<b>Draft allowance:</b> vertical faces of the pattern (⟂ the parting line) are given a slight taper so the pattern can be withdrawn without damaging the mould."])
 + E("<b>Part (b) of the question — what if shrinkage and draft are neglected?</b><br>No shrinkage allowance → the cast part ends up <em>smaller</em> than the target, so it malfunctions in service or will not fit the assembly. No draft → the pattern jams when drawn from the sand, damaging mould surfaces and causing defects in the casting.<br>"
     "Numerical: cast-iron shrinkage ≈ 1% (10 mm per metre): a 500 mm casting needs a pattern of 500 × 1.01 = <code>505 mm</code> (before machining allowance).")
 + T(["Method", "Feature"], [["Sand casting", "cheap, any size/metal, rough finish"], ["Die casting", "metal dies, high accuracy, large volumes, non-ferrous"], ["Investment (lost wax)", "fine detail, excellent finish, costly"], ["Centrifugal", "rotating mould; pipes, rings, sound castings"]])
 + P("<b>Common defects:</b> blowholes/porosity (trapped gas), shrinkage cavities (poor feeding), misruns and cold shuts (metal too cold), sand inclusions, hot tears."))

h2 = sec("h2", "H2. Forming Processes", "Shaping by plastic deformation: forging, rolling, extrusion, drawing and sheet-metal operations.",
 [("Plastic deformation", "permanent shape change under load."), ("Hot / cold working", "deforming above / below the recrystallisation temperature."), ("Forging", "shaping by compressive hammering/pressing."), ("Rolling", "reducing thickness by passing between rolls."),
  ("Extrusion", "forcing metal through a die."), ("Drawing", "pulling through a die (wire, tube)."), ("Blanking / piercing / bending / deep drawing", "sheet-metal operations.")],
 SRC + P("In <b>forming</b> the volume of metal is conserved while its shape is changed by plastic flow; there is little material waste and the grain flow improves strength.")
 + T(["Process", "How", "Typical products"], [["Forging", "compressive force in open or closed dies", "crankshafts, connecting rods, tools"], ["Rolling", "metal squeezed between rotating rolls", "plates, sheets, rails, beams"], ["Extrusion", "pushed through a shaped die", "tubes, window frames, rods"],
                                                 ["Drawing", "pulled through a die", "wire, thin tubes"], ["Sheet metal", "blanking (cut out), piercing (hole), bending, deep drawing", "car panels, utensils, cans"]])
 + UL(["<b>Hot working:</b> large deformation at low force, no strain hardening, poorer finish and accuracy.", "<b>Cold working:</b> better finish, accuracy and strength (strain hardening), needs more force and gives less deformation."])
 + E("Rolling a plate from 20 mm to 15 mm: draft = 5 mm, reduction = 5/20 = <code>25%</code>."))

h3 = sec("h3", "H3. Joining Processes", "Welding (arc, gas, resistance), soldering, brazing, riveting, adhesives.",
 [("Welding", "joining by melting (fusion) or pressure so the joint becomes one piece."), ("Filler metal", "added material that fills the joint."), ("Flux / shielding gas", "protects molten metal from oxidation."), ("Soldering", "joining with a filler melting below 450 °C."),
  ("Brazing", "filler melts above 450 °C but below the base metal's melting point."), ("Weld joint types", "butt, lap, T, corner, edge.")],
 SRC + T(["Process", "Principle", "Use"], [["Arc welding (SMAW, MIG/GMAW, TIG/GTAW)", "an electric arc between electrode and work melts the metal", "structures, pipes, general fabrication"], ["Gas (oxy-acetylene) welding", "flame from burning acetylene in oxygen", "thin sheets, repair, cutting"],
                                                 ["Resistance (spot) welding", "heat from current through contact resistance + pressure", "car body sheets"], ["Soldering", "low-melting filler, base not melted", "electronics, plumbing"], ["Brazing", "higher-melting filler, base not melted", "tool tips, pipes"],
                                                 ["Riveting / bolting", "mechanical, non-permanent or permanent", "bridges, aircraft"], ["Adhesive bonding", "glue", "composites, dissimilar materials"]])
 + P("<b>Defects:</b> porosity, cracks, incomplete fusion/penetration, undercut, distortion. In soldering/brazing the base metal is <em>not</em> melted — the key difference from welding."))

h4 = sec("h4", "H4. Cutting (Machining) Processes", "Material removal on lathe, drill, mill, shaper and grinder; cutting speed and material-removal rate.",
 [("Machining", "removing material with a cutting tool."), ("Cutting speed V", "surface speed of the work/tool, m/min."), ("Feed f", "tool advance per revolution (mm/rev)."), ("Depth of cut d", "thickness of material removed in one pass."), ("MRR", "material removal rate, mm³/min."), ("Turning / drilling / milling / shaping / grinding", "the basic operations.")],
 SRC + T(["Operation", "Machine", "Motion"], [["Turning, facing, threading", "lathe", "work rotates, tool feeds"], ["Drilling", "drilling machine", "drill rotates and feeds"], ["Milling", "milling machine", "multi-tooth cutter rotates, work feeds"], ["Shaping / planing", "shaper / planer", "reciprocating tool or work, flat surfaces"], ["Grinding", "grinder", "abrasive wheel, fine finish"]])
 + FM("V = π D N / 1000 &nbsp;(m/min) &nbsp;;&nbsp; turning MRR ≈ (π D N) × f × d &nbsp;(mm³/min)")
 + E("D = 50 mm at N = 400 rpm: V = π×50×400/1000 = <code>62.8 m/min</code>. With f = 0.2 mm/rev, d = 2 mm: MRR = (π×50×400) × 0.2 × 2 = 62 832 × 0.4 ≈ <code>25 100 mm³/min</code>.")
 + P("<b>Tool materials:</b> high-speed steel (HSS), carbide, ceramic, diamond — harder (and costlier) materials allow higher speeds."))

h5 = sec("h5", "H5. CNC Machining", "Computer-controlled machine tools: components, axes, G/M codes, closed-loop control.",
 [("NC / CNC", "numerical / computer numerical control."), ("MCU", "machine control unit — reads the program, drives the axes."), ("G-code", "motion commands (G00 rapid, G01 linear feed, G02/G03 arcs)."), ("M-code", "machine functions (M03 spindle on, M05 stop, M06 tool change, M30 end)."),
  ("Servo motor + encoder", "drive and position feedback."), ("ATC", "automatic tool changer."), ("Axes (X, Y, Z)", "directions of table/tool motion; 3-axis, 5-axis machines.")],
 SRC + B.d_cnc_loop()
 + P("Workflow: <b>CAD model → CAM (toolpaths) → G-code part program → CNC machine</b>. A <b>closed loop</b> compares commanded and measured position (encoder) so errors are corrected. Advantages: accuracy and repeatability, complex shapes, less labour, lights-out production.")
 + E("<code>G21 G90</code> (mm, absolute); <code>G00 X0 Y0</code> (rapid to origin); <code>G01 X50 F100</code> (feed 50 mm along X at 100 mm/min) — takes 50/100 = 0.5 min = <code>30 s</code>; <code>M30</code> end."))

h6 = sec("h6", "H6. Additive Manufacturing (3-D Printing)", "Building parts layer by layer from a CAD model: process chain, technologies, applications.",
 [("Additive manufacturing", "making a part by adding material layer by layer."), ("STL", "triangulated surface file sent to the printer."), ("Slicing", "cutting the model into layers and generating toolpath (G-code)."), ("FDM / FFF", "fused deposition modelling: melts and extrudes thermoplastic filament."),
  ("SLA", "stereolithography: UV light cures liquid resin."), ("SLS / SLM", "laser fuses powder (polymer / metal)."), ("Layer height", "thickness of each layer."), ("Support structure", "temporary material supporting overhangs.")],
 SRC + B.d_fdm()
 + OL(["<b>CAD model</b> → export <b>STL</b>.", "<b>Slice</b> into layers, choose orientation, supports, infill.", "<b>Print</b> layer by layer.", "<b>Post-process:</b> remove supports, sand, cure, heat-treat."])
 + T(["Technology", "Material", "Feature"], [["FDM / FFF", "PLA, ABS filament", "cheap, common, visible layer lines"], ["SLA", "photopolymer resin", "fine detail and smooth surface"], ["SLS", "nylon powder", "strong, no supports needed"], ["SLM / DMLS", "metal powder", "functional metal parts (aerospace, medical)"]])
 + UL(["<b>Advantages:</b> complex geometry, no tooling, low waste, quick prototypes, customisation.", "<b>Limits:</b> slow for volume, surface finish, anisotropic strength, size and material limits.", "<b>Applications:</b> prototypes, tooling, medical implants, aerospace parts, customised products."])
 + E("FDM: 0.4 mm nozzle, 0.2 mm layers, 60 mm/s → volumetric rate 0.4 × 0.2 × 60 = 4.8 mm³/s. A 30 cm³ (30 000 mm³) part takes 30 000/4.8 = 6250 s ≈ <code>1.7 h</code> of pure printing."))

h7 = sec("h7", "H7. Thermal Engineering &amp; the IC Engine", "Heat engines, four-stroke and two-stroke engines, SI vs CI, compression ratio, Otto efficiency, brake power.",
 [("Heat engine", "device converting heat to work."), ("IC engine", "engine burning fuel inside the cylinder."), ("TDC / BDC", "top / bottom dead centre — extreme piston positions."), ("Stroke / bore", "piston travel / cylinder diameter."), ("Compression ratio r", "V<sub>max</sub>/V<sub>min</sub>."),
  ("SI / CI", "spark-ignition (petrol) / compression-ignition (diesel)."), ("Brake power BP", "power at the shaft, 2πNT/60."), ("Thermal efficiency", "work output ÷ heat input.")],
 SRC + B.d_four_stroke()
 + UL(["<b>Four-stroke:</b> suction, compression, power, exhaust — 2 crank revolutions, one power stroke per cycle.", "<b>Two-stroke:</b> the cycle is completed in one revolution (a power stroke every revolution) with ports instead of valves; simpler and lighter but less efficient and more polluting."])
 + T(["", "SI (petrol)", "CI (diesel)"], [["Fuel intake", "air + fuel mixture", "air only; fuel injected at the end of compression"], ["Ignition", "spark plug", "heat of compression"], ["Compression ratio", "6–10", "15–22"], ["Ideal cycle", "Otto", "Diesel"], ["Efficiency", "lower", "higher"]])
 + FM("swept volume = (π/4) D² L &nbsp;;&nbsp; Otto efficiency η = 1 − 1 / r<sup>γ−1</sup> &nbsp;;&nbsp; BP = 2π N T / 60")
 + E("4-cylinder engine, bore 80 mm, stroke 90 mm: V<sub>s</sub> = π/4 × 80² × 90 = 452 389 mm³ ≈ 0.452 L per cylinder → <code>1.81 L</code> total. With r = 10, γ = 1.4: η = 1 − 10<sup>−0.4</sup> = 1 − 0.398 = <code>0.60</code> (ideal). Torque 150 N·m at 3000 rpm: BP = 2π×3000×150/60 = <code>47.1 kW</code>."))

h8 = sec("h8", "H8. Power Plants", "Steam (thermal), hydro, nuclear and gas-turbine plants and how each converts energy.",
 [("Rankine cycle", "steam power cycle: boiler → turbine → condenser → pump."), ("Prime mover", "turbine or engine driving the generator."), ("Penstock", "pipe carrying water to a hydro turbine."), ("Reactor / moderator / control rods", "nuclear: fission vessel / slows neutrons / absorbs neutrons."),
  ("Capacity factor", "actual output ÷ maximum possible."), ("Overall efficiency", "electrical output ÷ fuel energy input.")],
 SRC + B.d_rankine()
 + T(["Plant", "Energy source → conversion", "Notes"], [["Thermal (steam)", "coal/gas heat → steam → turbine → generator", "≈35–40% efficient; needs cooling water; emissions"], ["Hydro", "water potential energy → turbine", "P = ρ g Q H η; clean, flexible, site-limited"],
                                                  ["Nuclear", "U-235 fission heat → steam", "no CO₂ in operation; waste and safety issues"], ["Gas turbine", "fuel burnt in compressed air → turbine", "fast start, peaking plants; combined cycle ≈ 55–60%"], ["Diesel", "diesel engine + alternator", "standby and remote areas"]])
 + E("<b>Hydro:</b> Q = 10 m³/s, H = 50 m, η = 0.85: P = 1000×9.81×10×50×0.85 = <code>4.17 MW</code>.<br><b>Thermal:</b> 500 MW output at 38% overall efficiency needs 500/0.38 = 1316 MW of fuel heat; with coal of 20 MJ/kg that is 65.8 kg/s ≈ <code>237 t/h</code>."))

h9 = sec("h9", "H9. Refrigeration &amp; Air Conditioning", "Vapour-compression cycle, COP, tonnage and what an air conditioner does.",
 [("Refrigeration", "removing heat from a cold space and rejecting it to a warmer place."), ("Refrigerant", "working fluid (R134a, R32…)."), ("Compressor / condenser / expansion valve / evaporator", "the four main components."), ("COP", "coefficient of performance = Q<sub>L</sub>/W."),
  ("Ton of refrigeration", "3.517 kW (211 kJ/min)."), ("Air conditioning", "controlling temperature, humidity, cleanliness and distribution of air.")],
 SRC + B.d_vcr()
 + FM("COP = refrigeration effect / work input = Q<sub>L</sub> / W &nbsp;;&nbsp; Carnot COP = T<sub>L</sub> / (T<sub>H</sub> − T<sub>L</sub>) &nbsp; (kelvin)")
 + E("An evaporator absorbs 3.5 kW with a 1 kW compressor: COP = <code>3.5</code>. Limit between −10 °C (263 K) and 35 °C (308 K): COP<sub>Carnot</sub> = 263/45 = <code>5.8</code>; a real cycle is lower. A 1.5-ton AC removes 1.5 × 3.517 ≈ 5.3 kW of heat.")
 + P("<b>Air conditioning</b> adds control of humidity (dehumidifying at the cold coil), filtering and air circulation; window, split and central types. Heat taken from the room plus the compressor work is rejected outdoors at the condenser."))

h10 = sec("h10", "H10. Fuel Cells &amp; Sustainable Energy", "Hydrogen fuel cell operation; solar, wind and other renewable technologies.",
 [("Fuel cell", "electrochemical device converting fuel's chemical energy directly into electricity."), ("Anode / cathode / electrolyte (PEM)", "fuel electrode / oxidant electrode / proton-conducting membrane."), ("Renewable energy", "from sources replenished naturally."), ("Photovoltaic effect", "light generating voltage in a semiconductor."),
  ("Betz limit", "maximum 59.3% of wind power can be extracted."), ("Sustainability", "meeting present needs without harming future generations.")],
 SRC + B.d_fuel_cell()
 + FM("overall: 2H₂ + O₂ → 2H₂O + electricity + heat &nbsp;;&nbsp; ideal cell voltage ≈ 1.23 V (≈ 0.6–0.8 V under load)")
 + UL(["<b>Efficiency:</b> typically 40–60% electrical (higher with heat recovery) — not limited by the Carnot cycle; emits only water if hydrogen is used.", "<b>Types:</b> PEMFC (vehicles), SOFC, alkaline, phosphoric-acid, molten-carbonate.", "<b>Uses:</b> fuel-cell vehicles, backup power, portable power."])
 + T(["Technology", "Principle"], [["Solar PV", "photovoltaic effect in silicon cells → DC (then inverter)"], ["Solar thermal", "sunlight heats a fluid → steam or hot water"], ["Wind", "P = ½ ρ A v³ C<sub>p</sub>"], ["Biomass", "burning/digesting organic matter"], ["Geothermal", "Earth's internal heat"], ["Tidal/hydro", "water motion"]])
 + E("A stack of 100 cells each giving 0.7 V under load: <code>70 V</code> (series). Wind: rotor radius 40 m (A = 5027 m²), v = 12 m/s, C<sub>p</sub> = 0.4: P = 0.5×1.225×5027×12³×0.4 = <code>2.1 MW</code> (note the v³ — doubling wind speed gives 8× power)."))

h11 = sec("h11", "H11. Mechanisms: Four-Bar &amp; Hexapod", "Links, pairs, degrees of freedom, Grashof's law and the inversions of the four-bar chain; the hexapod.",
 [("Link", "rigid body joining others."), ("Kinematic pair", "joint between two links (revolute, prismatic)."), ("Kinematic chain / mechanism", "assembly of links; mechanism = chain with one link fixed."), ("Degrees of freedom (DOF)", "independent motions."), ("Grashof's law", "s + l ≤ p + q for a link to rotate fully."),
  ("Crank / rocker / coupler", "fully rotating / oscillating / floating link."), ("Inversion", "a different mechanism obtained by fixing another link."), ("Hexapod (Stewart platform)", "parallel mechanism with six linear actuators.")],
 SRC + B.d_fourbar()
 + FM("planar DOF (Grübler): F = 3(n − 1) − 2j &nbsp; (n links, j lower pairs) &nbsp;;&nbsp; four-bar: F = 3·3 − 2·4 = 1")
 + T(["Fixed link", "Mechanism (Grashof chain)"], [["link adjacent to the shortest", "<b>crank-rocker</b> — crank rotates fully, rocker oscillates"], ["the shortest link", "<b>double-crank</b> (drag link) — both cranks rotate"], ["link opposite to the shortest", "<b>double-rocker</b> — both oscillate (shortest link = coupler rotates)"]])
 + P("If s + l &gt; p + q (non-Grashof) no link can rotate fully and every inversion is a triple/double-rocker. Common four-bar uses: windscreen wipers (crank-rocker), locomotive coupling rods (double crank), and the slider-crank (IC engine, pumps) as a related chain.")
 + E("Links 20, 40, 50, 60: s + l = 20 + 60 = 80 ≤ p + q = 40 + 50 = 90 → Grashof. Fix the link next to the 20 → crank-rocker; fix the 20 → double-crank; fix the link opposite the 20 → double-rocker.")
 + B.d_hexapod()
 + P("A <b>hexapod</b> moves the platform in all 6 DOF by changing six leg lengths; parallel structure gives high stiffness and precision — flight simulators, positioning stages, telescopes, machining."))

h12 = sec("h12", "H12. Mechanical Components &amp; Motion Control", "Gears, belts, chains, cams, bearings, couplings, clutches, brakes and rotary-to-linear conversion.",
 [("Gear ratio", "speed ratio N₁/N₂ = z₂/z₁."), ("Module m", "d/z; teeth sizes must match to mesh."), ("Cam & follower", "profile converting rotation into a programmed linear motion."), ("Bearing", "supports a rotating shaft with low friction."),
  ("Coupling / clutch / brake", "joins shafts / engages–disengages / slows."), ("Lead screw", "screw converting rotation to linear motion: v = lead × N."), ("Torque", "turning moment; multiplies as speed falls.")],
 SRC + T(["Component", "Function"], [["Spur / helical gears", "transmit motion between parallel shafts; helical quieter"], ["Bevel gears", "shafts at an angle (usually 90°)"], ["Worm and worm wheel", "large reduction, often self-locking"], ["Rack and pinion", "rotary ↔ linear"], ["Belt (V, timing) and chain", "power over distance; chain/timing belt do not slip"],
                                                 ["Cam and follower", "irregular timed motion (valves)"], ["Bearings (ball, roller, journal)", "support and guide shafts"], ["Couplings, clutches, brakes", "connect, engage, stop"]])
 + FM("i = N₁/N₂ = z₂/z₁ = d₂/d₁ &nbsp;;&nbsp; centre distance = m(z₁ + z₂)/2 &nbsp;;&nbsp; belt: N₁D₁ = N₂D₂ &nbsp;;&nbsp; lead-screw speed v = lead × N")
 + E("Pinion 20 teeth at 1200 rpm drives a 60-tooth gear: N₂ = 1200 × 20/60 = <code>400 rpm</code>, torque ×3 (no losses). With m = 2 mm, centre distance = 2(20+60)/2 = <code>80 mm</code>. A lead screw of 5 mm lead at 300 rpm moves the nut <code>1500 mm/min</code>."))

h13 = sec("h13", "H13. Introduction to Robotics &amp; Automation", "Robot anatomy, DOF, configurations, sensors and actuators, simple kinematics, levels of automation.",
 [("Robot", "reprogrammable multifunctional manipulator."), ("Manipulator / end effector", "arm made of links and joints / gripper or tool at its tip."), ("Joint (revolute / prismatic)", "rotary / sliding."), ("Degrees of freedom", "number of independent joint motions."), ("Workspace", "region the end effector can reach."),
  ("Actuator / sensor / controller", "motor, hydraulic or pneumatic drive / encoder, proximity, force, vision / the computer."), ("PLC", "programmable logic controller for automation.")],
 SRC + B.d_robot_arm()
 + T(["Configuration", "Joints", "Example use"], [["Cartesian", "3 prismatic", "gantry, 3-D printer, pick-and-place"], ["Cylindrical", "1 revolute + 2 prismatic", "assembly"], ["Spherical (polar)", "2 revolute + 1 prismatic", "spot welding (older)"], ["SCARA", "revolute, horizontal compliance", "electronics assembly"], ["Articulated", "3+ revolute", "welding, painting, general industry"]])
 + FM("2-link planar arm: x = L₁cosθ₁ + L₂cos(θ₁+θ₂) &nbsp;;&nbsp; y = L₁sinθ₁ + L₂sin(θ₁+θ₂)")
 + E("L₁ = 0.5 m, L₂ = 0.3 m, θ₁ = 30°, θ₂ = 45°: x = 0.5 cos30° + 0.3 cos75° = 0.433 + 0.078 = <code>0.51 m</code>; y = 0.5 sin30° + 0.3 sin75° = 0.25 + 0.290 = <code>0.54 m</code>.")
 + UL(["<b>Automation levels:</b> fixed (hard) automation, programmable, flexible.", "<b>Applications:</b> welding, painting, assembly, material handling, surgery, inspection, warehouses."]))

h14 = sec("h14", "H14. Pneumatic &amp; Hydraulic Actuators", "Pascal's law, cylinders and force, and how pneumatic and hydraulic systems compare.",
 [("Actuator", "device converting fluid or electrical energy into motion."), ("Pascal's law", "pressure in a confined fluid acts equally in all directions."), ("Pneumatic", "uses compressed air (≈ 6–8 bar)."), ("Hydraulic", "uses oil under high pressure (to ≈ 200–350 bar)."),
  ("Cylinder", "linear actuator: piston in a barrel."), ("Valve (DCV)", "directs/controls flow."), ("FRL unit", "filter, regulator, lubricator for compressed air.")],
 SRC + B.d_hydraulic()
 + FM("p = F/A &nbsp;;&nbsp; F₂ = F₁ (A₂/A₁) &nbsp;;&nbsp; cylinder force F = p × A")
 + T(["", "Pneumatic", "Hydraulic"], [["Fluid", "air (compressible)", "oil (incompressible)"], ["Pressure", "low (≈ 6–8 bar)", "high (≈ 100–350 bar)"], ["Force", "moderate", "very large"], ["Speed", "fast", "slower, smooth, accurate positioning"], ["Cleanliness", "clean, exhaust to air", "oil leaks possible"],
                                         ["Components", "compressor, FRL, valves, cylinders", "pump, reservoir, valves, cylinders/motors"], ["Uses", "factory automation, pick-and-place, tools", "presses, excavators, brakes, lifts"]])
 + E("<b>Hydraulic press:</b> F₁ = 50 N on A₁ = 10 cm², A₂ = 100 cm²: F₂ = 50 × 100/10 = <code>500 N</code>. <b>Pneumatic cylinder:</b> bore 50 mm (A = 1963 mm²) at 6 bar (0.6 N/mm²): F = 0.6 × 1963 ≈ <code>1180 N</code> (less on the return stroke because of the rod area)."))

SECTIONS = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14]
CHECKLIST = ["Describe the sand-casting steps and the three pattern allowances; explain what happens if shrinkage and draft are neglected.", "Compare hot and cold working and name the forming processes.", "Distinguish welding, brazing and soldering.", "Calculate cutting speed and material-removal rate for turning.",
             "Explain CNC components, axes and a few G/M codes.", "Describe the 3-D printing workflow and compare FDM, SLA and SLS.", "Explain the four-stroke cycle, compare SI and CI and compute Otto efficiency and brake power.", "Sketch the layout of a steam power plant and a vapour-compression refrigeration cycle; compute COP.",
             "Explain how a hydrogen fuel cell works and compare it with a heat engine.", "Apply Grashof's law and name the four-bar inversions.", "Compute gear/belt ratios and lead-screw speed.", "Describe robot configurations and compute the end position of a 2-link arm.", "Compare pneumatic and hydraulic actuators and apply Pascal's law."]
