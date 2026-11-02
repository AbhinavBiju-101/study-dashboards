"""Registry of study dashboards shown on the hub.

To add a new subject:
  1. Drop its Flask project in dashboards/<slug>-dashboard/ (it must expose `app` in app.py).
  2. Add one entry below.  It is then mounted at /<slug>/ and gets a card and search coverage.
  3. For the mixed quiz, add a loader for its quiz bank in banks.py.

note_pattern: regex (full match) for the dashboard's notes-page links, used to build the search index.
"""

SUBJECTS = [
    {
        "slug": "evs",
        "note_pattern": r"/week/\d+",
        "code": "EVS",
        "title": "Environmental Studies",
        "blurb": "Earth systems, ecosystems, pollution, energy, sustainability and EIA, as illustrated weekly notebooks.",
        "unit": "weeks",
        "accent": "#2f6b4f",
        "local_port": 4000,
    },
    {
        "slug": "be",
        "note_pattern": r"/topic/\d+",
        "code": "BE",
        "title": "Basic Engineering",
        "blurb": "DC and AC circuits, network theorems, then electrical machines, with an expandable syllabus tree.",
        "unit": "topics",
        "accent": "#3949ab",
        "local_port": 4001,
    },
    {
        "slug": "baeng101",
        "note_pattern": r"/module/\d+",
        "code": "BAENG101",
        "title": "Reading & Writing",
        "blurb": "Modules 3 and 4: critical reading of scientific texts, review papers, literature reviews and referencing.",
        "unit": "modules",
        "accent": "#a4432c",
        "local_port": 4002,
    },
    {
        "slug": "phy",
        "note_pattern": r"/module/\d+",
        "code": "BAPHY105",
        "title": "Quantum Mechanics",
        "blurb": "Wave-particle duality, maths foundations, postulates, particle in a box, and quantum computing.",
        "unit": "modules",
        "accent": "#6d28d9",
        "local_port": 4005,
    },
]
