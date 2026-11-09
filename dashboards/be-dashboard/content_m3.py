from sections import *
import diagrams_b as B

g1 = sec("g1", "G1. Engineering Drawing: Importance &amp; Scope", "Drawing as the language of engineers, what it is used for, and the move from drawing boards to CAD.",
 [("Engineering drawing", "a graphical language giving the shape, size, material and finish of an object so it can be made."), ("BIS", "Bureau of Indian Standards; SP 46 is its drawing code, first-angle projection since 1991."), ("Machine / assembly / production drawing", "part drawings, how parts fit, and manufacturing details."),
  ("Pictorial view", "a 3-D-looking view (isometric, perspective)."), ("Orthographic view", "flat views (front, top, side) that show true shapes."), ("CAD", "computer-aided design/drafting.")],
 P("Words alone cannot describe a shape exactly. An engineering drawing communicates <em>shape, size, material, tolerances and surface finish</em> in a standard form that a designer in one place and a machinist in another read identically. It is the link between design and manufacture and the legal record of a design. A standard (BIS) fixes the symbols, line types, lettering and layout so that the drawing means the same to everyone.")
 + UL(["<b>Scope:</b> mechanical, civil (building drawings), electrical and electronic layouts, piping, shipbuilding, aircraft.", "<b>Before CAD (1950–80):</b> rooms full of draughtsmen on drawing boards; <b>today:</b> 3-D CAD models from which drawings, analysis and CNC/3-D-printing files are generated.",
       "<b>CAD is used for:</b> product design, simulation/analysis, manufacturing drawings, architecture, animation and visualisation, and rapid prototyping."])
 + F("Learn the standards (G2–G5) and the views (G6–G10) by hand first — CAD (G13) automates the drawing, but the exam asks you to draw, dimension and read views correctly."))

g2 = sec("g2", "G2. Drawing Sheets, Scales &amp; Title Block", "A-series sheet sizes (A0–A4), the title block and what it records.",
 [("A-series", "sheet sizes in which every size is half of the previous; sides in ratio 1 : √2."), ("A0", "841 × 1189 mm, area 1 m²."), ("Title block", "box at the bottom right giving drawing identity and details."), ("Scale", "ratio of drawing size to actual size (1:2 reduces, 2:1 enlarges, 1:1 full size)."),
  ("Revision", "recorded change to a drawing.")],
 B.d_sheet_sizes()
 + T(["Size", "Dimensions (mm)"], [["A0", "841 × 1189"], ["A1", "594 × 841"], ["A2", "420 × 594"], ["A3", "297 × 420"], ["A4", "210 × 297"]])
 + B.d_title_block()
 + UL(["<b>Key functions of the title block:</b> identifies the drawing (title, number, revision); shows ownership (company, designer, approver); gives scale and projection method; tracks revisions and dates; lists material and technical details; ensures standardisation; helps organisation (sheet numbers, references)."])
 + E("A 1.5 m long object drawn at scale 1:20 is 1500/20 = <code>75 mm</code> on paper. A 30 mm part drawn at 2:1 appears <code>60 mm</code> long — but the dimension figure still reads 30.")
 + M("The dimension figure on a drawing is the <em>actual</em> size, never the measured length on paper; the scale only affects how big the drawn line is."))

g3 = sec("g3", "G3. Types of Lines", "BIS line types A–K and what each is used for in orthographic drawing; pencil grades.",
 [("Visible outline", "thick continuous line (type A)."), ("Hidden line", "dashed thin line (F) for edges not visible."), ("Centre line", "long-dash-dot thin line (G)."), ("Dimension / extension / leader", "thin continuous lines (B)."),
  ("Cutting plane line", "chain thin with thick ends and at changes of direction (H)."), ("Hatching", "thin parallel lines (B) on cut surfaces."), ("Break line", "freehand wavy (C) or zig-zag (D).")],
 B.d_line_types()
 + P("In orthographic projection the lines normally met are A (visible outlines/edges), F (hidden), G (centre lines, symmetry, trajectories, pitch circles), B (dimension, extension, projection, short centre, leader and reference lines, hatching) and H (cutting planes). Use <b>HB</b> pencils for thick and <b>2H</b> for thin lines.")
 + M("When lines coincide the usual order of preference is: visible outline first, then hidden line, then centre line, then cutting-plane line, then dimension/projection lines — draw the one that takes priority.", "Which line wins?"))

g4 = sec("g4", "G4. Lettering &amp; Dimensioning", "Single-stroke capital lettering; elements and systems of dimensioning; chain vs parallel.",
 [("Lettering", "writing of words and numerals on a drawing — plain, single-stroke, uniform."), ("Extension (projection) line", "thin line showing the extent of a dimension."), ("Dimension line", "thin line with arrowheads between extension lines."), ("Leader line", "thin line from a feature to a note or size."),
  ("Aligned / unidirectional system", "figures placed parallel to the dimension line (readable from bottom or right) / all figures horizontal."), ("Datum", "reference surface from which dimensions are measured."), ("Fully defined", "all geometry dimensioned, nothing missing or redundant.")],
 P("<b>Lettering</b> must be neat, uniform and legible. Capital letters in single-stroke style are used; recommended heights are roughly 6–8 mm for main titles, 3–6 mm for sub-titles and 3–5 mm for notes and dimension figures.")
 + B.d_dim_elements()
 + P("<b>Systems:</b> in the <em>aligned</em> system figures are written parallel to the dimension line and read from the bottom or from the right; in the <em>unidirectional</em> system all figures read from the bottom. Dimension lines carry arrowheads (about 3 mm long, 1 mm wide); extension lines start about 1 mm from the outline and extend about 3 mm beyond the dimension line.")
 + B.d_dim_systems()
 + UL(["<b>Chain (continuous):</b> each dimension relates to the previous one; tolerances accumulate.", "<b>Parallel / progressive:</b> all dimensions from one datum; errors do not accumulate; preferred for functional features.", "<b>Combined:</b> a mix of both."]))

g5 = sec("g5", "G5. Dimensioning Rules &amp; Checking Errors", "Rules for placing dimensions correctly, with the CAT-1 'identify the dimensioning errors' question.",
 [("Overall dimension", "the total length, width or height of the object."), ("Redundant (duplicate) dimension", "a size given twice — not allowed."), ("Ø / R / SR / □", "diameter, radius, spherical radius and square symbols."), ("Chamfer", "bevelled edge, dimensioned as angle × length."), ("Functional dimension", "one needed for the function of the part.")],
 UL(["Dimension lines are <b>outside</b> the views where possible; avoid dimensioning inside the outline.", "Give each dimension <b>once</b>, on the view where the feature is most clearly seen; no duplicates and no unnecessary closed chains.", "Place smaller dimensions nearer the view and larger ones outside; keep about 8–10 mm between parallel dimension lines.",
     "Never use an outline, centre line or extension line as a dimension line; do not cross dimension lines with other lines.", "Dimension a circle with <b>Ø</b> (leader line), an arc with <b>R</b>; give holes by their centre position (from two edges) and size.",
     "Write plain numbers, no unit (the unit is stated once — mm); no trailing decimals such as '.00'.", "Dimensions are those of the <em>finished</em> part."])
 + E("<b>CAT-1 Q1 (10 marks):</b> a plate 110 × 70 with a 40-wide slot, two Ø20 holes and a 20 × 40 post is dimensioned with the overall length twice (110 top and bottom), some figures inside the outline, values written as '110.00', and centre lines used as dimension lines.<br>"
     "<b>Corrected version (the key):</b> one overall length 110 (bottom) and one overall height 70 (left); positions from the left/bottom edges — 25 to the first hole's centre, 40 slot width, 20 post width, 20 from the top, 15 and 40 from the right; Ø20 shown with leaders for both holes; all dimension lines outside the views; no '.00'. List the errors first, then redraw.")
 + F("Marks are given for (i) naming each error, (ii) a clean redrawn view with correct line types, (iii) every dimension given once, outside, with arrowheads, extension lines and the Ø symbol."))

g6 = sec("g6", "G6. Orthographic Projection: Principles, First &amp; Third Angle", "Planes of projection, the four quadrants, first- vs third-angle layout and symbols.",
 [("Projection", "representing a 3-D object on a plane by projectors from its points."), ("Parallel / perspective projection", "projectors parallel / converging to the eye."), ("Orthographic projection", "projectors parallel to each other and perpendicular to the plane."), ("VP / HP / PP", "vertical, horizontal and profile (side) planes."),
  ("Front view (FV) / top view (TV) / side view", "elevation / plan / end elevation."), ("Quadrant", "one of the four regions formed by HP and VP."), ("XY line", "line of intersection of HP and VP (reference line).")],
 P("In <b>orthographic projection</b> the object is viewed along lines of sight that are parallel to each other and perpendicular to the plane of projection, so each view shows true shapes and sizes. Normally the front view (from the front), top view and a side view are used; together they define the object completely.")
 + B.d_quadrants()
 + T(["Point in quadrant", "Front view vs XY", "Top view vs XY"], [["I (above HP, in front of VP)", "above", "below"], ["II (above HP, behind VP)", "above", "above"], ["III (below HP, behind VP)", "below", "above"], ["IV (below HP, in front of VP)", "below", "below"]])
 + B.d_first_third()
 + T(["First angle projection", "Third angle projection"],
     [["object kept in the first quadrant", "object kept in the third quadrant"], ["object lies <b>between</b> observer and the plane", "plane lies <b>between</b> observer and object"], ["plane assumed non-transparent", "plane assumed transparent"],
      ["top view comes <b>below</b> the front view", "top view comes <b>above</b> the front view"], ["left-side view is drawn to the <b>right</b> of the elevation", "left-side view is drawn to the <b>left</b> of the elevation"],
      ["recommended by BIS (since 1991) — use in exams unless told otherwise", "used in the USA and other countries"]])
 + M("<b>Hidden edges:</b> draw them dashed thin; if a hidden line coincides with a visible edge, the visible line is drawn. <b>Centre lines</b> are shown for holes and axes."))

g7 = sec("g7", "G7. Drawing Orthographic Views: Method &amp; Worked Examples", "Steps for converting a pictorial view to FV, TV and LSV, with the CAT-1 style question.",
 [("Pictorial view", "the 3-D picture given in the question."), ("Direction of view (X)", "arrow showing which face is the front view."), ("Hidden detail", "edges seen only through the object, shown dashed."), ("Projector (construction line)", "thin line carrying a point from one view to another."), ("Landscape layout", "sheet orientation required for the views.")],
 OL(["Choose the <b>front-view direction</b> (the X arrow) so that the front view shows the most shape.", "Measure the overall <b>length, height, depth</b>; plan the layout so all three views fit with gaps for dimensions.", "Draw thin boxes of overall size for each view (first angle: FV top-left, TV below it, LSV to the right of FV).",
     "Add the details one feature at a time, carrying points between views with thin projectors (height between FV and LSV; width between FV and TV).", "Show hidden detail dashed; add centre lines for holes (a hole is a circle in the view along its axis, dashed lines in the others).", "Darken the outlines (HB), then dimension each feature once."])
 + B.d_step_views()
 + E("<b>CAT-1 Q3 (10 marks):</b> a base 75 × 48 × 10 carries a raised block with a Ø22 hole and a triangular rib on one end. Using first angle: (a) front view looking along X — base rectangle 75 × 10 with the block and its Ø22 circle above; (b) top view — 75 × 48 base with the block and rib; (c) left-side view — shows the base, the block and the sloping rib, with the hole as dashed lines. The key shows the hole's axis as centre lines and its hidden edges dashed in TV and LSV.")
 + P("<b>Pyramid question (CAT-1 Q2):</b> see G8. <b>Practice approach:</b> sketch the views freehand first (G10) to check proportions, then draw to scale.")
 + F("For '<em>identify the missing view</em>' questions, use the same projector rules in reverse: widths must match between FV and TV, heights between FV and LSV."))

g8 = sec("g8", "G8. Projection of Solids", "Front and top views of prisms, pyramids, cylinders and cones in simple positions; CAT-1 pyramid.",
 [("Polyhedron", "solid bounded by plane faces (prism, pyramid, cube)."), ("Solid of revolution", "generated by rotating a figure (cylinder, cone, sphere)."), ("Axis", "line joining the centres of the two ends (bases)."), ("Base / apex", "the face on which a solid rests / the top point of a pyramid or cone."),
  ("Simple position", "axis perpendicular or parallel to a reference plane."), ("Generator", "slant line of a cone/cylinder surface.")],
 P("<b>Solids:</b> prisms (square, hexagonal …), pyramids, cylinders, cones, spheres. <b>Simple positions:</b> axis ⟂ HP (resting on its base), axis ⟂ VP, axis ∥ to both (resting on a face or generator). Rule: <em>when the axis is perpendicular to a plane, the view on that plane shows the true shape of the base</em>.")
 + B.d_solids()
 + T(["Solid, axis ⟂ HP", "Top view", "Front view"], [["Square prism", "square", "rectangle"], ["Square pyramid", "square with diagonals", "isosceles triangle"], ["Hexagonal prism", "regular hexagon", "rectangle with 2 inner lines (edge ∥ VP)"], ["Cylinder", "circle", "rectangle"], ["Cone", "circle with centre dot", "isosceles triangle"], ["Sphere", "circle", "circle"]])
 + E("<b>CAT-1 Q2:</b> square pyramid, base 50, axis 70, resting on its base on HP with a base side parallel to VP. <b>TV:</b> square 50 × 50 with both diagonals to the apex (o is at the centre). <b>FV:</b> an isosceles triangle with base 50 on the XY line (a′(d′) and b′(c′) — rear corners coincide) and apex o′ <code>70</code> above XY, on the axis. Label corners, show the axis as a chain line, dimension 50 and 70.<br>"
     "<b>Hexagonal prism</b>, side 25, height 65, base edge ∥ VP: TV hexagon of side 25 (width across corners 50, across flats 25√3 = 43.3); FV a 50 × 65 rectangle with inner lines at ±12.5 from the axis.")
 + M("Do not forget the <em>rear</em> corners: in the front view the corners behind the front ones coincide with them (written a′(d′)); hidden edges are dashed only if they are really hidden."))

g9 = sec("g9", "G9. Isometric Projection", "Isometric axes, isometric scale (0.816), isometric drawing vs projection, circles and the CAT-1 cylinder.",
 [("Isometric", "equal measure — all three axes equally foreshortened."), ("Isometric axes", "one vertical, two at 30° to the horizontal; 120° apart."), ("Isometric scale", "scale of shortened lengths; 0.816 of true length."), ("Isometric drawing", "drawn with true lengths (scale 1) — easier, 22% larger."),
  ("Isometric projection", "drawn with the isometric scale."), ("Isometric / non-isometric lines", "lines parallel to the axes / all others."), ("Four-centre method", "arcs construction of the isometric ellipse inside a rhombus.")],
 P("Orthographic views are accurate but need spatial imagination; an <b>isometric view</b> presents the object in 3-D in one picture. The cube is turned so that its three visible edges make equal angles with the picture plane, so they are drawn 120° apart.")
 + B.d_iso_axes_cube()
 + W("The cube's diagonal is in the vertical plane; a true edge BP and its isometric image BA satisfy BA/BO = 1/cos 30° = 2/√3 and BP/BO = 1/cos 45° = √2. Hence BA/BP = (2/√3)(1/√2) = √2/√3 = <b>0.816</b> (≈ 9/11).", "Why 0.816?")
 + B.d_iso_scale()
 + T(["", "Isometric projection", "Isometric drawing"], [["Lengths along axes", "× 0.816 (isometric scale)", "true length"], ["Size", "smaller, true projection", "22% larger, same shape"], ["Used", "exact representation", "exam drawings (faster)"]])
 + B.d_iso_step()
 + H("Isometric of a circle (four-centre method)")
 + OL(["Draw a rhombus of side equal to the circle's diameter on the 30° axes.", "Mark the midpoints of each side.", "Join them to the opposite acute corners to locate the centres; draw the four arcs inside the rhombus.", "The result is the isometric ellipse."])
 + E("<b>CAT-1 Q4:</b> vertical cylinder Ø50, axis 60. Draw a rhombus of side 50 (30° lines) for the top, make the ellipse (major axis ≈ 1.22 × 50 = <code>61 mm</code>, minor ≈ 0.71 × 50 = <code>35 mm</code> in an isometric drawing), repeat at the bottom 60 below along the vertical, and join the two ellipses by vertical tangents. In true isometric <em>projection</em> the ellipse's major axis equals the true diameter (50) and the minor is 50/√3 = 29.")
 + B.d_iso_cylinder()
 + P("<b>Orthographic → isometric (from the freehand lecture):</b> construct a box of the overall length, width and height on the 30° axes, then cut away or add the features measured along the axes; transfer non-isometric (sloping) edges by locating their end points."))

g10 = sec("g10", "G10. Freehand Sketching", "Why and how to sketch lines, circles and orthographic views by hand.",
 [("Freehand sketch", "drawn without instruments, quickly, with correct proportions."), ("Proportion", "the correct relative sizes of features."), ("Construction (thin) lines", "light guide lines later darkened."), ("Visualisation", "the ability to picture an object in 3-D."), ("Overall size box", "thin rectangle of length × height for each view.")],
 UL(["<b>Why sketch:</b> quick idea generation; flexible; effective communication; encourages creativity; supports problem solving; useful in early design stages; improves visualisation; needs no special tools."])
 + B.d_freehand()
 + UL(["<b>Vertical lines</b> are drawn from top to bottom (long lines with overlapping strokes); <b>horizontal</b> lines from left to right; the eye must be on the end point.", "<b>Inclined lines</b> are drawn upward from left to right or downward from right to left.", "Always <b>mark the end points first</b>.",
       "<b>Circle:</b> draw centre lines, mark points at the radius on them (add diagonals for accuracy), then sweep through the marks; an ellipse is built the same way."])
 + H("Guidelines for orthographic sketches")
 + OL(["Decide the views to be drawn.", "Draw boxes with thin lines of the overall length, width and height of the object.", "Add the details; dark outlines for visible edges, dashed for hidden edges.", "Dimension."])
 + E("Object with overall 70 (length) × 30 (height) × 50 (depth): boxes — FV 70 × 30, TV 70 × 50 below it, right-side view 50 × 30 to the left of the front view (third angle). Then add the step (15 mm high, 40 wide), the 20 slot, and so on. A second example (slot 16 wide × 10 deep through a 60 × 40 × 40 block) is sketched the same way: FV with the slot notch, TV with three strips, LSV with two dashed lines for the hidden slot.")
 + P("<b>Simple machine components</b> to practise: bolt and nut, washer, V-block, bearing block, shaft with keyway, bracket — sketch the proportions first, then add holes, fillets and centre lines."))

g11 = sec("g11", "G11. Perspective Projection", "How a picture plane image of an object looks to an observer: terms, types, visual-ray method.",
 [("Perspective", "the image formed on a picture plane by visual rays from the eye to the object."), ("PP (picture plane)", "transparent vertical plane on which the image is formed."), ("GP (ground plane)", "horizontal plane on which the object stands."), ("GL (ground line)", "intersection of PP and GP."),
  ("Station point (S)", "position of the observer's eye."), ("Horizon line (HL)", "horizontal line at eye level on the PP."), ("Centre of vision (C)", "foot of the axis of vision on the PP."), ("Visual ray", "line from the eye to a point of the object."), ("Vanishing point", "where receding parallel lines appear to meet.")],
 P("In parallel (orthographic/isometric) projection the projectors are parallel; in <b>perspective</b> they converge on the eye, so parts farther away look smaller, as in a photograph. The object is placed behind the transparent picture plane and the image is formed where the visual rays pierce the PP.")
 + B.d_persp_terms()
 + UL(["<b>One-point</b> perspective: one face parallel to the PP; <b>two-point</b>: object turned so two sets of horizontals vanish at two points on the horizon; <b>three-point</b>: also a vanishing point for verticals."])
 + H("Visual-ray method (square pyramid example)")
 + P("Data: pyramid base 20, axis height 40, base 25 behind the PP; station point 50 above GP, 40 in front of PP and 40 to the left of the axis.")
 + OL(["Draw the PP and GL; mark the plan (top view) of the pyramid at its distance behind the PP, and the station point's plan.", "Join the station point's plan to each plan point (visual rays); mark where each ray cuts the PP line.", "Project these cut points down to the elevation, drawing the elevation of the object and of the station point above GL.",
       "In elevation, join the station point to each point of the object; the intersection of each of these lines with the projector from step 3 is that point's perspective.", "Join the perspective points in order, hidden edges dashed."])
 + M("The result depends on the station point: moving the observer closer to the object increases the foreshortening and the convergence."))

g12 = sec("g12", "G12. Introduction to Building Drawing (Floor Plan)", "Plan, elevation and section; BIS conventions; a simple residential floor plan.",
 [("Plan", "horizontal section through the building about 1 m above floor level."), ("Elevation", "outside view of a face of the building."), ("Section", "vertical cut showing heights and construction."), ("PCC / RCC", "plain / reinforced cement concrete."), ("Plinth", "part of the wall between ground and floor level."),
  ("Lintel", "beam above a door or window opening."), ("Parapet", "low wall at the edge of a roof."), ("Weathering course", "waterproof layer on a roof."), ("Habitable room", "room for living, sleeping, etc.")],
 P("A <b>building drawing</b> shows what to build: a <b>plan</b> (rooms, walls, doors, windows), <b>elevations</b> and a <b>section</b> (foundation, wall, floor, roof heights). Drawings follow BIS conventions (your lecture cites IS 962:1967; the syllabus mentions SP 7, the National Building Code) with standard symbols and material hatching for brick, stone, concrete and so on. Scales: 1:100 for plans; 1:50 or larger for sections and details.")
 + UL(["<b>Parts of a building:</b> foundation (PCC footings), plinth, superstructure (walls), lintel, roof slab (RCC), parapet, weathering course, floor finish, steps.", "<b>Typical thicknesses in the lecture pump-house example:</b> parapet 200, weathering course 100, RCC roof slab 120, PCC (1:4:8) flooring 120, cement-mortar plaster about 20.",
       "<b>Material notation:</b> cement mortar ratios (e.g. CM 1:5, 1:3) and concrete mixes (e.g. 1:4:8, 1:2:4) are written on the section."])
 + B.d_floorplan()
 + UL(["External walls 230 mm, partitions 115 mm; doors shown with the swing arc; windows as double lines in the wall.", "Typical minimum sizes (National Building Code, check the latest): habitable room ≈ 9.5 m² (width ≥ 2.4 m); kitchen ≈ 4.5 m² (width ≥ 1.8 m); bathroom ≈ 1.8 m².", "Lines: thick for sectioned walls, thin for furniture and dimension lines; room names and sizes written inside."])
 + E("Plot 10 m × 12 m = 120 m²; built-up area of the plan above = 6.8 × 6.0 = 40.8 m² → <code>34%</code> of the plot. Living 3.6 × 3.6 = 13 m² and bedroom 3.2 × 3.6 = 11.5 m² both exceed the 9.5 m² minimum; kitchen 3.6 × 2.4 = 8.6 m² exceeds 4.5 m²."))

g13 = sec("g13", "G13. Introduction to CAD", "What CAD is, 2-D sketching vs 3-D solid modelling, common features, file types and the CAD→CAM link.",
 [("CAD", "computer-aided design — creating and modifying drawings/models on a computer."), ("Sketch & constraint", "2-D profile with geometric (parallel, tangent) and dimensional constraints."), ("Feature", "extrude, revolve, cut, fillet, chamfer, shell."), ("Parametric model", "model whose dimensions drive the geometry."),
  ("Layer", "transparent overlay organising drawing content."), ("DWG / DXF / STEP / STL", "drawing, exchange, neutral solid and 3-D-printing mesh file types."), ("CAM", "computer-aided manufacturing.")],
 P("In CAD software you <b>sketch</b> a 2-D profile with basic tools (line, circle, arc), add <b>geometric and dimensional constraints</b>, then build a 3-D solid with <b>features</b> — <em>extrude</em> (push a profile to a depth), <em>revolve</em> (spin it about an axis), <em>cut</em>, <em>fillet</em> (round an edge), <em>chamfer</em> (bevel an edge) and <em>shell</em> (hollow out). The 2-D engineering drawing — multiple views, dimensions, annotations — is then generated from the 3-D model, so a change in the model updates the drawing. (This is the content of the SolidWorks lab experiments.)")
 + UL(["<b>Advantages:</b> accuracy, easy editing, storage and sharing, standard parts libraries, simulation, direct link to CNC and 3-D printing.", "<b>Common packages:</b> AutoCAD (2-D drafting), SolidWorks, CATIA, Fusion 360, FreeCAD (3-D)."])
 + E("<b>Coordinate input.</b> Absolute: type <code>50,30</code> → point (50, 30). Relative polar: <code>@50&lt;30</code> → a line 50 long at 30°: Δx = 50 cos 30° = <code>43.3</code>, Δy = 50 sin 30° = <code>25</code>.")
 + F("CAD files feed Module 4: an STL file goes to the 3-D-printer slicer (H6) and the CAM toolpath goes to the CNC machine (H5)."))

g14 = sec("g14", "G14. CAT-1 Pattern — What the Paper Asked", "The CAT-1 question types (Module 3 and casting) and where to revise each.",
 [("BL", "Bloom's level of a question (1 Remember … 6 Create)."), ("CO", "course outcome the question tests (CO3 graphics, CO4 manufacturing).")],
 T(["Q", "Task", "Marks / BL", "Revise"],
   [["1", "identify dimensioning errors; redraw and dimension to BIS", "10 / 3 (Apply)", "G4, G5"], ["2", "top and front view of a square pyramid (base 50, axis 70, side ∥ VP)", "10 / 3", "G8"],
    ["3", "pictorial view → FV, TV and left-side view, first angle", "10 / 3", "G6, G7"], ["4", "isometric view of a vertical cylinder (Ø50 × 60)", "10 / 3", "G9"], ["5", "types of pattern allowances; what if shrinkage and draft are neglected", "10 / 2 (Understand), CO4", "H1"]])
 + P("<b>Instructions on the paper:</b> all dimensions in mm; neat drawings with proper pencil grades for each line type; BIS lettering, numbering and dimensioning; <em>orthographic projections in landscape orientation</em>; plan the layout so that every view (including the side view) fits.")
 + UL(["Draw outlines in HB, thin lines in 2H.", "Always label views (FRONT VIEW, TOP VIEW, …) and state 'ALL DIMENSIONS ARE IN mm'.", "Show hidden lines and centre lines where needed; keep construction lines light."]))

SECTIONS = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14]
CHECKLIST = ["State the A0–A4 sheet sizes and the contents of a title block.", "Name the BIS line types and what each is used for; state the pencil grades.", "Identify and correct dimensioning errors in a given figure.", "Sketch the four quadrants and state where each view lies in first and third angle.",
             "Draw FV, TV and LSV of a pictorial object in first angle, with hidden lines and centre lines.", "Draw the views of a pyramid, prism, cone and cylinder in simple position.", "Derive the isometric scale 0.816 and draw an isometric view including a circle/cylinder.", "Sketch lines, circles and orthographic views freehand with the right technique.",
             "Define the terms of perspective projection and outline the visual-ray method.", "Name the parts of a building and draw a simple plan with BIS conventions.", "Describe a CAD workflow: sketch, constraints, features, drawing generation."]
