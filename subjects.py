"""Registry of study dashboards shown on the hub.

To add a new subject:
  1. Drop its Flask project in dashboards/<slug>/ (it must expose `app` in app.py).
  2. Add one entry below.  That's it: it is mounted at /<slug>/ and gets a card.
"""

SUBJECTS = [
    {
        "slug": "evs",
        "code": "EVS",
        "title": "Environmental Studies",
        "blurb": "Earth systems, ecosystems, pollution, energy, sustainability and EIA, as illustrated weekly notebooks.",
        "unit": "weeks",
        "units": 6,
        "accent": "#2f6b4f",
        "local_port": 4000,
    },
    {
        "slug": "be",
        "code": "BE",
        "title": "Basic Engineering",
        "blurb": "DC and AC circuits, network theorems, then electrical machines, with an expandable syllabus tree.",
        "unit": "topics",
        "units": 2,
        "accent": "#3949ab",
        "local_port": 4001,
    },
    {
        "slug": "baeng101",
        "code": "BAENG101",
        "title": "Reading & Writing",
        "blurb": "Modules 3 and 4: critical reading of scientific texts, review papers, literature reviews and referencing.",
        "unit": "modules",
        "units": 3,
        "accent": "#a4432c",
        "local_port": 4002,
    },
    {
        "slug": "phy",
        "code": "BAPHY105",
        "title": "Quantum Mechanics",
        "blurb": "Wave-particle duality, maths foundations, postulates, particle in a box, and quantum computing.",
        "unit": "modules",
        "units": 5,
        "accent": "#6d28d9",
        "local_port": 4005,
    },
]
