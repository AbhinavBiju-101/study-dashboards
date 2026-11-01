# Key-terms boxes + extra teaching content for Topic 2 (Electrical Machines)
# Content follows the lecture slides (construction, types, applications, equations).

TERMS2 = {
"c1": [
("Yoke", "the outer frame (cast/rolled steel): supports the poles, protects the machine and carries the magnetic flux between poles."),
("Field system", "the stationary part that produces the main flux: an even number of pole cores bolted to the yoke, with field winding on each."),
("Salient pole", "a pole that projects inward towards the armature."),
("Pole core / pole shoe", "the core carries the field coil; the curved shoe spreads the flux over the armature, supports the coil and lowers reluctance."),
("Field winding", "the coils on the poles that, when energised, create alternate N and S poles."),
("Armature", "the rotating part: core + winding; it carries the current that interacts with the field to make torque."),
("Armature core", "slotted cylinder of insulated soft-steel laminations mounted on the shaft."),
("Armature winding", "insulated conductors placed in the slots and suitably interconnected — lap winding or wave winding."),
("Commutator", "a mechanical rectifier/inverter of wedge-shaped copper segments insulated by mica; connects the rotating armature to the fixed supply."),
("Brushes / brush holder", "carbon blocks pressed on the commutator by springs; they carry current between the supply and the armature."),
("Air gap", "the small gap between pole shoe and armature across which the flux passes."),
("Lamination", "thin insulated steel sheet; stacking them breaks up the paths for eddy currents."),
("Eddy current", "circulating currents induced inside the iron by changing flux; they only waste heat, so they are minimised."),
("Spider", "a spoked frame on which laminations are mounted in large machines instead of being keyed directly to the shaft."),
],
"c2": [
("Torque (T)", "the turning effort of the shaft; T ∝ Φ·I<sub>a</sub>."),
("Fleming's left-hand rule", "for MOTORS: thuMb = Motion (force), First finger = Field, seCond finger = Current."),
("Fleming's right-hand rule", "for GENERATORS: thuMb = Motion, First finger = Field, seCond finger = induced EMF/current."),
("Back EMF (counter EMF), E<sub>b</sub>", "the EMF induced in the armature of a running motor; it opposes the supply voltage."),
("Armature current (I<sub>a</sub>) and resistance (R<sub>a</sub>)", "the current in, and resistance of, the armature winding."),
("Commutation", "the reversal of current in an armature coil as it passes from under one pole to the next."),
("Motoring action", "electrical input → mechanical output (supply pushes current against E<sub>b</sub>)."),
("Generating action", "mechanical input → electrical output (E drives current out to the load)."),
("Starter", "a series resistor (or electronic controller) that limits the very large starting current."),
("Speed equation", "N ∝ E<sub>b</sub>/Φ — speed rises with back-EMF and falls with flux."),
],
"c3": [
("Separately excited", "field winding fed from an independent DC source."),
("Self-excited", "field winding fed from the machine's own armature supply (shunt, series, compound)."),
("Shunt motor", "field winding (high resistance, many turns) in <em>parallel</em> with the armature."),
("Series motor", "field winding (low resistance, few heavy turns) in <em>series</em> with the armature."),
("Compound motor", "both shunt and series field windings."),
("Short shunt / long shunt", "short: shunt field across the armature only, series field in the supply line. Long: shunt field across armature + series field together."),
("Cumulative / differential compound", "cumulative: series field <em>aids</em> the shunt flux. Differential: it <em>opposes</em> it."),
("Starting torque", "the torque at zero speed; high for series motors."),
("Speed regulation", "how little the speed changes from no-load to full-load; excellent for shunt motors."),
("Over-compounded generator", "a cumulative compound generator whose terminal voltage <em>rises</em> with load, compensating line drop."),
],
"c4": [
("Primary / secondary winding", "the winding connected to the source / the winding connected to the load."),
("Core", "the laminated silicon-steel path that carries the mutual flux."),
("Limb / yoke (transformer)", "limb: the part of the core carrying a winding; yoke: the part that joins the limbs."),
("Mutual inductance", "the property by which a changing current in one coil induces an EMF in a neighbouring coil."),
("Turns ratio", "N<sub>1</sub>/N<sub>2</sub>, the number of primary turns to secondary turns."),
("Step-up / step-down", "step-up: V<sub>2</sub> &gt; V<sub>1</sub> (N<sub>2</sub> &gt; N<sub>1</sub>). Step-down: V<sub>2</sub> &lt; V<sub>1</sub>."),
("Core-type / shell-type", "windings around the limbs of a two-limb core / windings on the centre limb of a three-limb core."),
("Cylindrical (concentric) winding", "LV coil next to the core, HV coil concentric over it — used in core-type."),
("Sandwich (disc) winding", "LV and HV sections stacked alternately — used in shell-type."),
("Leakage flux", "flux that links only one winding; it is minimised by winding layout."),
("Hysteresis / eddy-current loss", "core losses; silicon steel cuts the first, lamination cuts the second."),
("Excitation (magnetising) current", "the small no-load primary current needed to set up the flux."),
],
"c5": [
("Flux (Φ, Φ<sub>m</sub>)", "magnetic flux in webers (Wb); Φ<sub>m</sub> is its peak value."),
("Faraday's law", "induced EMF = rate of change of flux linkage: e = −N dΦ/dt."),
("RMS EMF (E)", "E = 4.44 f Φ<sub>m</sub> N — the effective value of the induced EMF."),
("Form factor", "1.11 for a sine wave; note 4 × 1.11 = 4.44, the constant in the EMF equation."),
("Phase of EMF", "e lags the flux by 90°."),
("EMF per turn", "E/N = 4.44 f Φ<sub>m</sub> — the same in both windings."),
],
"c6": [
("Stator", "the stationary part: steel frame + slotted silicon-steel core + three-phase winding."),
("Rotor", "the rotating part, either squirrel-cage or wound."),
("Rotating magnetic field (RMF)", "a field of constant magnitude that rotates in space, produced by a balanced three-phase supply."),
("Synchronous speed (N<sub>s</sub>)", "the speed of the RMF, N<sub>s</sub> = 120f/P rpm."),
("Slip (s)", "s = (N<sub>s</sub> − N<sub>r</sub>)/N<sub>s</sub>; typically 2–5% at full load."),
("Poles (P)", "number of magnetic poles wound into the stator; more poles = slower speed."),
("Squirrel-cage rotor", "rotor bars (copper/aluminium) short-circuited by end rings."),
("End rings", "the rings that short-circuit the rotor bars at both ends."),
("Slip rings", "insulated rings on the shaft of a wound rotor that connect the rotor winding to external resistors through brushes."),
("Wound (slip-ring) rotor", "rotor with a three-phase winding (star-connected) brought out to slip rings."),
("Induction (asynchronous) motor", "a motor whose rotor current is <em>induced</em> by the stator field, and which never quite reaches synchronous speed."),
("Inrush (starting) current", "the very large current drawn when the motor is first switched on, often 5–7× rated."),
],
}

EXTRA2 = {}

EXTRA2["c1"] = r'''
<h4 class="sub">Part-by-part: what it is, what it's made of, why</h4>
<table>
<tr><th>Part</th><th>Construction</th><th>Purpose</th></tr>
<tr><td><b>Yoke</b></td><td>hollow cylinder of cast or rolled steel</td><td>(1) supports the pole cores and protects the machine; (2) provides a path for the flux produced by the field winding</td></tr>
<tr><td><b>Field system</b></td><td>even number of salient pole cores bolted to the yoke, field coils wound on each; pole shoe with curved face; laminated cores</td><td>produces the main magnetic flux; coils are connected so that adjacent poles alternate N, S, N, S</td></tr>
<tr><td><b>Pole shoe</b></td><td>widened curved end of each pole core</td><td>(1) supports the field coil; (2) increases the flux cross-section, lowering reluctance</td></tr>
<tr><td><b>Armature core</b></td><td>slotted cylinder of soft-steel laminations, insulated and clamped; keyed to shaft (small machines) or on a spider (large)</td><td>carries the armature winding and provides a low-reluctance flux path; laminations reduce eddy-current loss</td></tr>
<tr><td><b>Armature winding</b></td><td>insulated conductors in the slots, suitably interconnected (lap or wave)</td><td>carries the current that develops torque (motor) or the induced EMF (generator)</td></tr>
<tr><td><b>Commutator</b></td><td>wedge-shaped hard-drawn copper segments, insulated from each other and the shaft by mica; each segment joined to the ends of armature coils</td><td>reverses coil current at the right instant (a mechanical rectifier/inverter)</td></tr>
<tr><td><b>Brushes</b></td><td>carbon blocks in metal brush holders; spring pressure held constant</td><td>carry current between the external DC supply and the rotating commutator</td></tr>
</table>
<div class="box why"><span class="label">Why laminate the iron?</span>
Iron is a conductor. In the rotating armature core (and in AC-fed cores like transformers), changing flux induces circulating <b>eddy currents</b> inside the solid iron, wasting energy as heat. Slicing the core into thin, mutually insulated sheets breaks the circulating loops into tiny ones, so the currents (and the loss) fall drastically. The sheets are cut along the direction of flux so magnetic performance is unaffected.
</div>
<h4 class="sub">Lap vs wave winding</h4>
<table>
<tr><th></th><th>Lap winding</th><th>Wave winding</th></tr>
<tr><td>Parallel paths (A)</td><td>A = P (number of poles)</td><td>A = 2, whatever the number of poles</td></tr>
<tr><td>Best for</td><td>high current, low voltage</td><td>low current, high voltage</td></tr>
</table>
<div class="box mis"><span class="label">Fixing a common misconception</span>
The commutator does <b>not</b> make DC current alternate 'because it's broken' — it is deliberate. Inside the armature the current <em>must</em> alternate (so each conductor keeps pushing the same way), while the supply is DC. The commutator is the bridge that lets a DC supply feed an alternating-current armature. That is why the slides call it a 'mechanical rectifier' — in a generator it does the opposite job: it turns the armature's AC into DC for the load.
</div>
'''

EXTRA2["c2"] = r'''
<h4 class="sub">Working principle, step by step</h4>
<ol>
<li>Connect the DC supply: the <b>field winding</b> is energised and creates alternate N and S poles.</li>
<li>The <b>armature conductors</b> carry current — in one direction under the N pole, in the opposite direction under the S pole.</li>
<li>Each current-carrying conductor sits in a magnetic field, so a force F = BIL acts on it (Fleming's left-hand rule). For the layout shown in the slides, this tends to move each conductor anticlockwise.</li>
<li>The forces on all conductors add to give a driving <b>torque</b> that turns the armature.</li>
<li>As a conductor moves from under one pole to the next, the commutator reverses its current — and the new pole is of opposite polarity, so the force direction stays the same.</li>
<li>Result: continuous rotation in one direction.</li>
</ol>
<h4 class="sub">Torque and speed relations</h4>
<div class="formula">T ∝ Φ · I<sub>a</sub> &nbsp;&nbsp;|&nbsp;&nbsp; E<sub>b</sub> ∝ Φ · N &nbsp;&nbsp;|&nbsp;&nbsp; N ∝ E<sub>b</sub>/Φ = (V − I<sub>a</sub>R<sub>a</sub>)/Φ</div>
<p>Weaken the flux → the motor speeds up; raise the supply voltage → the motor speeds up. These two 'knobs' are how DC-motor speed is controlled.</p>
<div class="box why"><span class="label">Why a DC motor needs a starter</span>
At the instant of switching on, the armature is at rest, so N = 0 and E<sub>b</sub> = 0. The armature circuit equation V = E<sub>b</sub> + I<sub>a</sub>R<sub>a</sub> then gives I<sub>a</sub> = V/R<sub>a</sub>. Since R<sub>a</sub> is tiny (a fraction of an ohm), that current is enormous. E.g. 220 V and R<sub>a</sub> = 0.5 Ω gives <b>440 A</b> versus a normal 20 A. A starter resistor limits it and is cut out as E<sub>b</sub> builds up.
</div>
<div class="box ex"><span class="label">Worked example — speed change with load</span>
Motor: V = 220 V, R<sub>a</sub> = 0.5 Ω, I<sub>a</sub> = 20 A, N = 1000 rpm, flux constant.<br>
E<sub>b1</sub> = 220 − 20 × 0.5 = <code>210 V</code>.<br>
Load is reduced and I<sub>a</sub> falls to 10 A: E<sub>b2</sub> = 220 − 10 × 0.5 = <code>215 V</code>.<br>
Since N ∝ E<sub>b</sub> (Φ constant): N<sub>2</sub> = 1000 × 215/210 = <code>1024 rpm</code>. Speed rises slightly at light load — this small change is what 'good speed regulation' means.
</div>

<h4 class="sub">The same machine as a generator (DC generator principle)</h4>
<p>Run the machine backwards — spin the armature with a prime mover and it produces an EMF. Consider a <b>single-turn loop ABCD</b> rotating clockwise at constant speed in a uniform field. The flux linked with coil sides AB and CD changes continuously, inducing an EMF in each side; the two EMFs add.</p>
<table>
<tr><th>Loop position</th><th>How the coil sides cut the flux</th><th>Induced EMF</th></tr>
<tr><td>1</td><td>moving <em>parallel</em> to the flux</td><td>zero</td></tr>
<tr><td>2</td><td>cutting at an angle</td><td>small</td></tr>
<tr><td>3</td><td>moving at <em>right angles</em> to the flux</td><td><b>maximum</b></td></tr>
<tr><td>4</td><td>cutting at an angle</td><td>reduced</td></tr>
<tr><td>5</td><td>parallel to the flux again</td><td>zero</td></tr>
<tr><td>6</td><td>now under the <em>opposite pole</em></td><td>polarity reversed</td></tr>
<tr><td>7</td><td>right angles to the flux (other pole)</td><td>maximum in the reversed direction</td></tr>
<tr><td>back to 1</td><td>parallel again</td><td>zero — cycle repeats each revolution</td></tr>
</table>
<p>The EMF in the loop is therefore <b>alternating</b>. A commutator (one split ring for one loop) flips the connections to the brushes every half-turn, so the external load always sees the same polarity — pulsating DC. With many coils and many commutator segments, the ripples smooth out to nearly steady DC.</p>
@@GENERATOR_SVG@@
<table>
<tr><th></th><th>Motor</th><th>Generator</th></tr>
<tr><td>Energy conversion</td><td>electrical → mechanical</td><td>mechanical → electrical</td></tr>
<tr><td>Rule for direction</td><td>Fleming's <b>left</b>-hand</td><td>Fleming's <b>right</b>-hand</td></tr>
<tr><td>Armature equation</td><td>V = E<sub>b</sub> + I<sub>a</sub>R<sub>a</sub></td><td>V<sub>t</sub> = E − I<sub>a</sub>R<sub>a</sub></td></tr>
<tr><td>Which is larger?</td><td>supply V &gt; E<sub>b</sub></td><td>generated E &gt; terminal V<sub>t</sub></td></tr>
<tr><td>I<sub>a</sub> direction</td><td>into the armature</td><td>out of the armature</td></tr>
</table>
<div class="foreshadow">A generator's <em>generated EMF</em> and a motor's <em>back EMF</em> are the same physical thing — a conductor cutting flux. Every machine does both at once; what decides whether it is a motor or a generator is which way the energy flows.</div>
'''

EXTRA2["c3"] = r'''
<h4 class="sub">Circuit equations for every connection (motors)</h4>
<table>
<tr><th>Type</th><th>Currents</th><th>Supply equation</th></tr>
<tr><td>Separately excited</td><td>I<sub>a</sub> = I<sub>s</sub>; field current I<sub>f</sub> comes from a separate source</td><td>V<sub>s</sub> = E<sub>b</sub> + I<sub>a</sub>R<sub>a</sub></td></tr>
<tr><td>Shunt</td><td>I<sub>a</sub> = I<sub>s</sub> − I<sub>sh</sub>; I<sub>sh</sub> = V<sub>s</sub>/R<sub>sh</sub></td><td>V<sub>s</sub> = E<sub>b</sub> + I<sub>a</sub>R<sub>a</sub></td></tr>
<tr><td>Series</td><td>I<sub>a</sub> = I<sub>se</sub> = I<sub>s</sub></td><td>V<sub>s</sub> = E<sub>b</sub> + I<sub>a</sub>(R<sub>a</sub> + R<sub>se</sub>)</td></tr>
<tr><td>Compound — short shunt</td><td>I<sub>a</sub> = I<sub>s</sub> − I<sub>sh</sub>; series field in the supply line; I<sub>sh</sub> = (V<sub>s</sub> − I<sub>se</sub>R<sub>se</sub>)/R<sub>sh</sub></td><td>V<sub>s</sub> = E<sub>b</sub> + I<sub>a</sub>R<sub>a</sub> + I<sub>se</sub>R<sub>se</sub></td></tr>
<tr><td>Compound — long shunt</td><td>I<sub>a</sub> = I<sub>s</sub> − I<sub>sh</sub>; I<sub>se</sub> = I<sub>a</sub>; I<sub>sh</sub> = V<sub>s</sub>/R<sub>sh</sub></td><td>V<sub>s</sub> = E<sub>b</sub> + I<sub>a</sub>(R<sub>a</sub> + R<sub>se</sub>)</td></tr>
</table>
<div class="box mis"><span class="label">Heads-up on a slide detail</span>
In the short-shunt drawing the series field sits in the <em>supply line</em>, so physically it carries the line current I<sub>s</sub> (= I<sub>a</sub> + I<sub>sh</sub>). Some slides write I<sub>se</sub> = I<sub>a</sub> for it; that only holds for the <em>long</em> shunt. If your exam uses the slide's version, follow that — but know the physical reason, and check with your lecturer if a question depends on it.
</div>
<div class="box ex"><span class="label">Worked example — shunt motor</span>
V<sub>s</sub> = 220 V, R<sub>sh</sub> = 110 Ω, R<sub>a</sub> = 0.5 Ω, line current I<sub>s</sub> = 22 A.<br>
I<sub>sh</sub> = 220/110 = <code>2 A</code>; I<sub>a</sub> = 22 − 2 = <code>20 A</code>; E<sub>b</sub> = 220 − 20 × 0.5 = <code>210 V</code>; input power = 220 × 22 = 4840 W; mechanical power developed = E<sub>b</sub>I<sub>a</sub> = 210 × 20 = 4200 W.
</div>
<h4 class="sub">Where each motor is used</h4>
<table>
<tr><th>Motor</th><th>Characteristic</th><th>Applications</th></tr>
<tr><td><b>Shunt</b></td><td>almost constant speed from no-load to full-load</td><td>wipers and automatic windscreens, drills, conveyors, fans, blowers, boring mills, shapers, spinning and weighing machines, centrifugal pumps</td></tr>
<tr><td><b>Series</b></td><td>very high starting torque; speed falls sharply with load; dangerous if unloaded</td><td>cranes, air compressors, lifts and elevators, winches, electric traction, hair dryers, vacuum cleaners, power tools, sewing machines</td></tr>
<tr><td><b>Cumulative compound</b></td><td>high starting torque with fair speed regulation</td><td>presses, electric shovels, reciprocating machines, conveyors, stamping machines, elevators, compressors, rolling mills, heavy planers</td></tr>
<tr><td><b>Differential compound</b></td><td>speed <em>rises</em> with load — poor, unstable torque</td><td>not suitable for practical use</td></tr>
</table>

<h4 class="sub">DC generator types (same connections, different equations)</h4>
<table>
<tr><th>Type</th><th>Currents</th><th>Terminal voltage</th></tr>
<tr><td>Series generator</td><td>I<sub>a</sub> = I<sub>se</sub> = I<sub>L</sub></td><td>V<sub>t</sub> = E − I<sub>a</sub>(R<sub>a</sub> + R<sub>se</sub>)</td></tr>
<tr><td>Shunt generator</td><td>I<sub>a</sub> = I<sub>L</sub> + I<sub>sh</sub>; I<sub>sh</sub> = V<sub>t</sub>/R<sub>sh</sub></td><td>V<sub>t</sub> = E − I<sub>a</sub>R<sub>a</sub></td></tr>
<tr><td>Compound — short shunt</td><td>I<sub>a</sub> = I<sub>L</sub> + I<sub>sh</sub>; I<sub>se</sub> = I<sub>L</sub>; I<sub>sh</sub> = (V<sub>t</sub> + I<sub>se</sub>R<sub>se</sub>)/R<sub>sh</sub></td><td>V<sub>t</sub> = E − I<sub>a</sub>R<sub>a</sub> − I<sub>se</sub>R<sub>se</sub></td></tr>
<tr><td>Compound — long shunt</td><td>I<sub>a</sub> = I<sub>L</sub> + I<sub>sh</sub>; I<sub>se</sub> = I<sub>a</sub>; I<sub>sh</sub> = V<sub>t</sub>/R<sub>sh</sub></td><td>V<sub>t</sub> = E − I<sub>a</sub>(R<sub>a</sub> + R<sub>se</sub>)</td></tr>
</table>
<p>Note the sign flip against the motor: for a generator the drops <em>subtract</em> from the generated EMF (V<sub>t</sub> = E − drops); for a motor the drops <em>add</em> to the back-EMF (V = E<sub>b</sub> + drops).</p>
<table>
<tr><th>Generator</th><th>Applications</th></tr>
<tr><td>Separately excited</td><td>independent DC field source, so expensive and rarely used; wide voltage range for laboratory and commercial testing, speed-regulation tests, supplying speed-controlled DC motors</td></tr>
<tr><td>Series</td><td>limited use: voltage boosting in distribution feeders, constant-current high-voltage DC transmission (several in series), field excitation in DC locomotives for regenerative braking, series arc lighting</td></tr>
<tr><td>Shunt</td><td>nearly constant terminal voltage over short distances: battery charging, lighting and power supply (with field regulator), exciting alternators</td></tr>
<tr><td>Compound</td><td>over-compounded: compensates line drop for long transmission lines; cumulative: supplying DC motors, lighting and heavy power services; differential: arc welding (needs large voltage drop and constant current)</td></tr>
</table>
'''

EXTRA2["c4"] = r'''
<h4 class="sub">Working principle (mutual induction)</h4>
<ol>
<li>An alternating voltage V<sub>1</sub> is applied to the primary; a small alternating current flows and sets up an alternating flux Φ in the core.</li>
<li>This flux links <em>both</em> windings, so by Faraday's law it induces EMF E<sub>1</sub> in the primary and E<sub>2</sub> in the secondary.</li>
<li>The EMFs are proportional to the numbers of turns: E<sub>2</sub>/E<sub>1</sub> = N<sub>2</sub>/N<sub>1</sub>.</li>
<li>Connect a load across the secondary and a current I<sub>2</sub> flows; power passes from the primary circuit to the secondary circuit <b>magnetically</b>, with <b>no electrical connection</b> and <b>no change in frequency</b>.</li>
</ol>
<div class="box def"><span class="label">Ideal-transformer relations</span>
<div class="formula">V<sub>1</sub>/V<sub>2</sub> = N<sub>1</sub>/N<sub>2</sub> = I<sub>2</sub>/I<sub>1</sub> &nbsp;&nbsp;(V<sub>1</sub>I<sub>1</sub> = V<sub>2</sub>I<sub>2</sub>)</div>
A transformer that steps voltage <em>up</em> steps current <em>down</em> by the same ratio; power in = power out (for an ideal one). If N<sub>1</sub> &gt; N<sub>2</sub> it is <b>step-down</b>; if N<sub>2</sub> &gt; N<sub>1</sub> it is <b>step-up</b>.
</div>
<h4 class="sub">Core-type vs shell-type</h4>
<table>
<tr><th></th><th>Core type</th><th>Shell type</th></tr>
<tr><td>Magnetic circuit</td><td>two vertical limbs + two horizontal yokes (a single rectangular path)</td><td>three limbs; the two outer limbs give low-reluctance return paths for the central flux</td></tr>
<tr><td>Windings</td><td>half of each winding on each limb (reduces leakage flux); LV next to the core, HV over it — <b>cylindrical</b> (concentric) coils</td><td>both windings on the central limb, split into LV and HV sections stacked alternately — <b>sandwich</b> (disc) coils</td></tr>
</table>
<div class="box why"><span class="label">Why put LV next to the core?</span>
The low-voltage winding needs less insulation from the grounded core than the high-voltage one. Putting LV closest to the core and wrapping HV over it means only the LV coil needs to be insulated from the core, and the HV winding is insulated by the LV winding and its own insulation — saving space and cost.
</div>
<div class="box ex"><span class="label">Worked example — ideal transformer currents</span>
A 2200 V / 220 V, 10 kVA transformer. Turns ratio = 2200/220 = <code>10</code> (step-down). Rated primary current = 10 000/2200 = <code>4.55 A</code>; rated secondary current = 10 000/220 = <code>45.5 A</code> — ten times larger, matching I<sub>2</sub>/I<sub>1</sub> = N<sub>1</sub>/N<sub>2</sub> = 10.
</div>
<h4 class="sub">Losses and applications</h4>
<ul>
<li><b>Core (iron) loss:</b> hysteresis (reduced by silicon steel) + eddy current (reduced by laminations); roughly constant regardless of load.</li>
<li><b>Copper loss:</b> I²R in the windings; grows with load.</li>
<li><b>Uses:</b> stepping voltage up/down for power transmission and distribution; supplying suitable voltages to electronic devices (TV etc.) and low-voltage electronic circuits; stepping up voltage in home inverter systems.</li>
</ul>
<div class="box mis"><span class="label">Fixing a common misconception</span>
A transformer does not work on DC. With a steady primary current the flux is constant, dΦ/dt = 0, and no EMF is induced in the secondary. Worse, the winding resistance alone limits DC current, which can burn the primary out. Only <em>changing</em> flux induces voltage.
</div>
'''

EXTRA2["c5"] = r'''
<div class="box why"><span class="label">Where does 4.44 come from — a second way</span>
For a sinusoidal flux the <em>average</em> EMF over a quarter cycle is 4 f Φ<sub>m</sub> N (flux swings from 0 to Φ<sub>m</sub> in T/4 = 1/(4f)). The RMS value = form factor × average = 1.11 × 4fΦ<sub>m</sub>N = <b>4.44</b> fΦ<sub>m</sub>N. It agrees with the derivation in the box above (2π/√2 = 4.44), and it shows why the form factor from the AC-circuits topic matters here.
</div>
<div class="box def"><span class="label">Phase relations</span>
Because e = −N dΦ/dt and Φ = Φ<sub>m</sub> sin ωt, the EMF is −NΦ<sub>m</sub>ω cos ωt = NΦ<sub>m</sub>ω sin(ωt − 90°). So <b>the induced EMF lags the flux by 90°</b>, and E<sub>1</sub> and E<sub>2</sub> are in phase with each other (the same flux induces both). The primary draws a small magnetising current in phase with the flux.
</div>
<div class="box ex"><span class="label">Worked example — find the turns</span>
A 220 V, 50 Hz primary; peak core flux Φ<sub>m</sub> = 0.01 Wb. Neglect winding drop so E<sub>1</sub> ≈ 220 V.<br>
N<sub>1</sub> = E<sub>1</sub>/(4.44 f Φ<sub>m</sub>) = 220/(4.44 × 50 × 0.01) = 220/2.22 ≈ <code>99 ≈ 100 turns</code>.<br>
For a 22 V secondary: N<sub>2</sub> = N<sub>1</sub> × 22/220 = <code>10 turns</code>.
</div>
<div class="box why"><span class="label">What happens at a lower frequency?</span>
For a given voltage, Φ<sub>m</sub> = E/(4.44 f N). If the frequency <em>drops</em> (say a 50 Hz transformer on a 25 Hz supply), Φ<sub>m</sub> would double, pushing the core into saturation and causing very large magnetising current. That is why transformers are rated for a specific frequency, and why a 50 Hz design can't be freely used at lower frequency.
</div>
'''

EXTRA2["c6"] = r'''
<h4 class="sub">Stator construction</h4>
<ul>
<li>A cylindrical <b>frame</b> of fabricated steel encloses a hollow <b>core</b> of thin silicon-steel laminations (silicon steel and lamination together reduce hysteresis and eddy-current loss).</li>
<li>Evenly spaced <b>slots</b> on the inner surface hold the stator winding.</li>
<li>Three windings, connected in star or delta, form a balanced three-phase winding, wound for a definite number of poles.</li>
<li>More poles means lower speed (N<sub>s</sub> = 120f/P): 2 poles → 3000 rpm, 4 → 1500, 6 → 1000, 8 → 750 (at 50 Hz).</li>
</ul>
<h4 class="sub">Why the field rotates</h4>
<p>The three winding currents are 120° apart in time. Watch what they do at a few instants (I<sub>m</sub> = peak current):</p>
<table>
<tr><th>ωt</th><th>i<sub>A</sub></th><th>i<sub>B</sub></th><th>i<sub>C</sub></th><th>Which winding dominates?</th></tr>
<tr><td>0°</td><td>0</td><td>−0.87 I<sub>m</sub></td><td>+0.87 I<sub>m</sub></td><td>B and C (opposite signs)</td></tr>
<tr><td>90°</td><td>+I<sub>m</sub></td><td>−0.5 I<sub>m</sub></td><td>−0.5 I<sub>m</sub></td><td>A</td></tr>
<tr><td>210°</td><td>−0.5 I<sub>m</sub></td><td>+I<sub>m</sub></td><td>−0.5 I<sub>m</sub></td><td>B</td></tr>
<tr><td>330°</td><td>−0.5 I<sub>m</sub></td><td>−0.5 I<sub>m</sub></td><td>+I<sub>m</sub></td><td>C</td></tr>
</table>
<p>The 'strongest' winding hops A → B → C in turn, so the resultant magnetic axis sweeps around the stator. Adding the three fluxes vectorially gives a resultant of constant magnitude <b>1.5 Φ<sub>m</sub></b> that rotates at N<sub>s</sub>.</p>
@@THREEPHASE_SVG@@
<h4 class="sub">How the rotor is driven</h4>
<ol>
<li>The rotating field sweeps past the stationary rotor conductors and induces EMF in them (Faraday's law).</li>
<li>The rotor circuit is closed (short-circuited bars, or external resistors for a wound rotor), so rotor currents flow.</li>
<li>These currents lie in the stator's magnetic field, so each experiences a force (F = BIL) — together giving torque in the direction of the field's rotation (Lenz's law: the rotor 'chases' the change).</li>
<li>The rotor speeds up but can never catch the field: at N<sub>r</sub> = N<sub>s</sub> there would be no relative motion, no induced EMF, no current and no torque. Hence slip.</li>
</ol>
<div class="formula">N<sub>r</sub> = N<sub>s</sub>(1 − s) &nbsp;&nbsp;|&nbsp;&nbsp; rotor-current frequency f<sub>r</sub> = s·f</div>
<div class="box ex"><span class="label">Worked example — 6-pole motor</span>
50 Hz supply, 6 poles: N<sub>s</sub> = 120 × 50/6 = <code>1000 rpm</code>. At 3% slip, N<sub>r</sub> = 1000 × 0.97 = <code>970 rpm</code>, and the rotor current frequency = 0.03 × 50 = <code>1.5 Hz</code>. At start (s = 1) the rotor frequency equals the supply frequency, 50 Hz.
</div>
<div class="box mis"><span class="label">Fixing a common misconception</span>
'Induction motors run at synchronous speed' — no, that is a <b>synchronous</b> motor. An induction motor is called <em>asynchronous</em> because it always runs a few percent slower. Also, to reverse an induction motor you swap <em>any two</em> of the three supply leads — that reverses the direction the field rotates.
</div>
<h4 class="sub">Squirrel-cage vs wound (slip-ring) rotor — full comparison</h4>
<table>
<tr><th></th><th>Squirrel cage</th><th>Slip ring (wound rotor)</th></tr>
<tr><td>Rotor</td><td>laminated core with parallel slots; copper/aluminium bars short-circuited at each end by end rings</td><td>laminated core; insulated three-phase double-layer winding (star), open ends taken to three slip rings on the shaft</td></tr>
<tr><td>External resistance</td><td>impossible (bars permanently shorted)</td><td>added via brushes and slip rings, then cut out once the motor is up to speed</td></tr>
<tr><td>Cost</td><td>Low</td><td>High</td></tr>
<tr><td>Maintenance</td><td>Low (no brushes)</td><td>High (brushes wear)</td></tr>
<tr><td>Speed control</td><td>Poor</td><td>Good</td></tr>
<tr><td>Efficiency on start-up</td><td>Poor</td><td>Good</td></tr>
<tr><td>Efficiency during operation</td><td>Good</td><td>Poor</td></tr>
<tr><td>Heat regulation</td><td>Good</td><td>Poor</td></tr>
<tr><td>Inrush current and torque</td><td>High current, low starting torque</td><td>Low current, high starting torque</td></tr>
<tr><td>Applications</td><td>centrifugal pumps, conveyor drives, large blowers and fans, machine tools, lathes — and about 70–80% of all industrial induction motors</td><td>crushers, plunger pumps, cranes and hoists, elevators, compressors, conveyors — heavy, high-inertia loads that need high starting torque, low starting current or speed control</td></tr>
</table>
<div class="box why"><span class="label">Why external resistance helps at start</span>
Adding resistance to the rotor circuit at start (a) reduces the starting current and (b) improves the rotor power factor, which together raise the <em>starting torque</em> — a rare case where adding resistance gives more torque. Once at speed the resistance is removed (the brushes are short-circuited) so the motor runs efficiently like a squirrel-cage machine.
</div>
'''
