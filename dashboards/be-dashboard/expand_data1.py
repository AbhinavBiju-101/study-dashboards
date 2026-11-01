# Key-terms boxes + extra teaching content for Topic 1 (DC & AC Circuits)

TERMS1 = {
"a1": [
("Charge (Q)", "the basic electrical quantity, measured in coulombs (C)."),
("Current (I)", "rate of flow of charge, I = dQ/dt; unit ampere (A = C/s). Conventional direction = the way positive charge would move (from + to −)."),
("Voltage / potential difference (V)", "energy per unit charge between <em>two points</em>; unit volt (V = J/C)."),
("Resistance (R)", "opposition to current flow; unit ohm (Ω). For a wire, R = ρL/A (resistivity × length ÷ area)."),
("Conductance (G)", "reciprocal of resistance, G = 1/R; unit siemens (S). Makes parallel-circuit sums easier."),
("Power (P)", "rate of energy conversion, P = VI = I²R = V²/R; unit watt (W)."),
("Energy (W)", "power × time; unit joule (J). Electricity bills use the kilowatt-hour (1 kWh = 3.6 MJ)."),
("Ideal voltage source", "keeps its terminal voltage fixed whatever current it supplies (internal resistance = 0)."),
("Ideal current source", "forces a fixed current whatever voltage appears across it (internal resistance = ∞)."),
("Independent / dependent source", "independent: value set by itself. Dependent (controlled): value set by a voltage or current elsewhere in the circuit (drawn as a diamond)."),
("Active / passive element", "active elements (sources) can deliver energy; passive elements (R, L, C) only absorb, dissipate or store it."),
("Linear element", "an element whose V–I graph is a straight line through the origin (double V, double I)."),
("Short circuit / open circuit", "short: R = 0, V = 0, any current. Open: R = ∞, I = 0, any voltage."),
("Passive sign convention", "if current enters the <b>+</b> terminal of an element, then P = VI &gt; 0 means the element <em>absorbs</em> power; P &lt; 0 means it delivers power."),
],
"a2": [
("Node", "a point where two or more circuit elements join."),
("Essential node (junction)", "a node where <b>three or more</b> branches meet — the only nodes that need a KCL equation."),
("Branch", "a single element (or a series string of elements) connecting two nodes; it carries one current."),
("Loop", "any closed path that visits each node at most once."),
("Mesh", "a loop that contains no other loop inside it (a 'window' of the circuit)."),
("Voltage rise / drop", "going through a source from − to + is a rise; going through a resistor <em>along</em> the current is a drop."),
("Planar circuit", "a circuit that can be drawn on paper with no wires crossing — needed for mesh analysis."),
],
"a3": [
("Equivalent resistance (R<sub>eq</sub>)", "the single resistor that draws the same current as the whole network at the same voltage."),
("Series connection", "elements strung end-to-end so they carry the <em>same current</em>."),
("Parallel connection", "elements joined across the <em>same two nodes</em> so they share the <em>same voltage</em>."),
("Voltage divider", "series resistors splitting a supply voltage in proportion to their resistances."),
("Current divider", "parallel resistors splitting a supply current in inverse proportion to their resistances."),
("Series–parallel network", "a mix of both; reduce it step by step, innermost combination first."),
],
"a4": [
("Reference node (ground)", "the node chosen as 0 V; every other node voltage is measured relative to it."),
("Node voltage", "the voltage of a node with respect to the reference node."),
("Supernode", "two non-reference nodes joined by a voltage source; treated as one node for KCL, plus one extra equation from the source."),
("Conductance form", "writing branch current as G × (voltage difference) instead of (voltage difference)/R; gives a symmetric equation matrix."),
],
"a5": [
("Mesh current", "an imaginary current circulating round one mesh; real branch currents are built from these."),
("Shared (common) branch", "a branch belonging to two meshes; its real current = difference of the two mesh currents."),
("Supermesh", "two meshes sharing a current source; the source's branch is left out and one KVL is written round the combined outer loop."),
("Clockwise convention", "choosing every mesh current clockwise makes all the shared-resistor terms negative — a built-in error check."),
],
"a6": [
("Ideal source", "no internal resistance; the source transformation does <b>not</b> apply to an ideal source on its own."),
("Practical source", "an ideal source plus its internal resistance (in series for a voltage source, in parallel for a current source)."),
("Internal resistance", "the resistance inside a real source that makes its terminal voltage sag under load."),
("Equivalent sources", "two sources with identical open-circuit voltage and short-circuit current at the terminals."),
],
"a7": [
("Linear network", "a network whose elements obey superposition/proportionality; Thevenin's theorem holds only for these."),
("Terminals a–b", "the two points where the load will connect and from which we 'look into' the network."),
("Open-circuit voltage (V<sub>oc</sub>)", "voltage across a–b with nothing connected; equals V<sub>th</sub>."),
("Short-circuit current (I<sub>sc</sub>)", "current when a–b are shorted together; equals I<sub>N</sub>."),
("Thevenin resistance (R<sub>th</sub>)", "resistance seen at a–b with independent sources killed; also R<sub>th</sub> = V<sub>oc</sub>/I<sub>sc</sub>."),
("Norton equivalent", "current source I<sub>N</sub> in parallel with R<sub>N</sub> = R<sub>th</sub>."),
("Killing a source", "voltage source → replace by a short; current source → replace by an open circuit."),
],
"a8": [
("Load (R<sub>L</sub>)", "the element receiving power from the source network."),
("Matched load", "R<sub>L</sub> = R<sub>th</sub>; the condition for maximum power to the load."),
("Efficiency (η)", "η = power in load ÷ total power supplied = R<sub>L</sub>/(R<sub>th</sub> + R<sub>L</sub>)."),
("P<sub>max</sub>", "V<sub>th</sub>²/(4R<sub>th</sub>) — the peak of the power-vs-R<sub>L</sub> curve."),
],
"a9": [
("Independent source", "a source whose value does not depend on anything else in the circuit."),
("Response", "the voltage or current you are solving for."),
("Superposition", "total response = algebraic sum of responses to each independent source acting alone."),
("Dependent source (caution)", "stays <em>in</em> the circuit during superposition; only independent sources are killed."),
],
"b1": [
("Waveform", "the graph of a quantity against time."),
("Cycle", "one complete set of positive and negative values of the wave."),
("Alternation", "half a cycle (one positive <em>or</em> one negative loop)."),
("Period (T)", "time for one cycle; T = 1/f, in seconds."),
("Frequency (f)", "cycles per second; unit hertz (Hz). Indian mains = 50 Hz."),
("Angular frequency (ω)", "ω = 2πf, in rad/s. Mains: 2π × 50 ≈ 314 rad/s."),
("Instantaneous value", "the value at one particular time, e.g. v(t) = V<sub>m</sub> sin ωt."),
("Peak (maximum) value V<sub>m</sub>", "the amplitude — the largest instantaneous value."),
("Peak-to-peak value", "2V<sub>m</sub>, from the positive crest to the negative crest."),
("Phase angle (φ)", "the angular shift of a wave relative to a reference; v = V<sub>m</sub> sin(ωt + φ)."),
],
"b2": [
("RMS (root mean square)", "square it, average it over a period, take the root. Also called the <b>effective value</b> — the DC value that would heat a resistor equally."),
("Average (mean) value", "for a symmetrical AC wave the full-cycle mean is 0, so 'average' means the mean of the rectified half-cycle."),
("Form factor", "V<sub>rms</sub> / V<sub>avg</sub>. Sine wave: 1.11."),
("Peak factor (crest factor)", "V<sub>m</sub> / V<sub>rms</sub>. Sine wave: 1.414."),
("Rectified wave", "a wave with the negative half flipped (full-wave) or removed (half-wave)."),
("Effective value", "another name for RMS — it produces the same heating as the equal DC."),
],
"b3": [
("Phasor", "a complex number (magnitude + angle) representing a sinusoid at a known frequency."),
("Polar / rectangular form", "V∠θ  ↔  a + jb, where j = √−1 and a = V cos θ, b = V sin θ."),
("Impedance (Z)", "V/I for AC circuits; Z = R + jX, unit ohm (Ω)."),
("Reactance (X)", "the imaginary part of impedance: X<sub>L</sub> = ωL (inductive, +), X<sub>C</sub> = 1/(ωC) (capacitive, −)."),
("Inductor (L) / Capacitor (C)", "energy-storage elements: L stores energy in a magnetic field (henry, H); C in an electric field (farad, F)."),
("Leading / lagging", "'current lags voltage' means the current wave peaks <em>later</em> than the voltage wave."),
("Admittance (Y)", "Y = 1/Z = G + jB, unit siemens (S); B is <b>susceptance</b>, G is <b>conductance</b>."),
],
"b4": [
("Series RLC circuit", "R, L and C carrying the same current; total impedance Z = R + j(X<sub>L</sub> − X<sub>C</sub>)."),
("Inductive circuit", "X<sub>L</sub> &gt; X<sub>C</sub>: net reactance positive, current lags."),
("Capacitive circuit", "X<sub>C</sub> &gt; X<sub>L</sub>: net reactance negative, current leads."),
("Resonance", "X<sub>L</sub> = X<sub>C</sub>: reactances cancel, Z = R (minimum), current is maximum and in phase with V."),
("Resonant frequency (f<sub>0</sub>)", "f<sub>0</sub> = 1/(2π√(LC))."),
("Quality factor (Q)", "at resonance Q = X<sub>L</sub>/R; a big Q means a sharp, narrow resonance peak and large L and C voltages."),
("Voltage triangle", "V<sub>R</sub>, V<sub>X</sub> and V form a right triangle — the impedance triangle multiplied by I."),
],
"b5": [
("Instantaneous power p(t)", "p = v·i at each instant; it oscillates at twice the supply frequency."),
("Real (active) power P", "the average power actually converted to heat/work; unit watt (W)."),
("Reactive power Q", "power swapped back and forth with L and C; unit volt-ampere-reactive (VAR). Positive for inductive loads."),
("Apparent power S", "S = V<sub>rms</sub>I<sub>rms</sub>; unit volt-ampere (VA). What cables and transformers must be rated for."),
("Power factor (pf)", "cos φ = P/S, from 0 to 1."),
("Lagging / leading pf", "lagging = inductive load (motors); leading = capacitive load."),
("Unity power factor", "pf = 1: purely resistive; all the apparent power is real power."),
("Complex power", "<b>S</b> = P + jQ = V·I* (I* is the complex conjugate of the current phasor)."),
("Power-factor correction", "adding capacitance in parallel with an inductive load to cancel Q and raise pf."),
],
}

EXTRA1 = {}

EXTRA1["a1"] = r'''
<h4 class="sub">Circuit elements at a glance</h4>
<table>
<tr><th>Element</th><th>Symbol idea</th><th>V–I relation</th><th>What it does</th></tr>
<tr><td>Resistor</td><td>zig-zag</td><td>v = iR</td><td>dissipates energy as heat</td></tr>
<tr><td>Inductor</td><td>coil</td><td>v = L di/dt</td><td>stores energy in a magnetic field; opposes <em>changes</em> in current</td></tr>
<tr><td>Capacitor</td><td>two plates</td><td>i = C dv/dt</td><td>stores energy in an electric field; opposes <em>changes</em> in voltage</td></tr>
<tr><td>Ideal voltage source</td><td>circle with ±</td><td>v fixed</td><td>supplies whatever current the circuit demands</td></tr>
<tr><td>Ideal current source</td><td>circle with arrow</td><td>i fixed</td><td>supplies whatever voltage the circuit demands</td></tr>
</table>
<div class="box mis"><span class="label">Fixing a common misconception</span>
<b>Short vs open circuit:</b> people mix these up. A <em>short</em> lets current flow freely with zero voltage across it (like a wire). An <em>open</em> circuit lets zero current flow with any voltage across it (like a switch turned off). A source is never 'shorted' safely unless it has internal resistance — a shorted ideal voltage source would demand infinite current.
</div>
<div class="box ex"><span class="label">Worked example — sign convention</span>
A 12 V battery drives 3 A <em>out of</em> its + terminal. Battery: current leaves the + terminal, so P = −VI = −36 W (it <b>delivers</b> 36 W). The resistor it drives: current enters its + terminal, so P = +36 W (it <b>absorbs</b> 36 W). Total power in the circuit = −36 + 36 = 0 — energy is conserved.
</div>
'''

EXTRA1["a2"] = r'''
<h4 class="sub">Steps for applying KVL to a loop</h4>
<ol>
<li>Pick a direction (clockwise is conventional) and label current directions on each resistor.</li>
<li>Walk once round the loop. Going through a source from − to + is a <b>rise (+)</b>; through a resistor <em>with</em> the current is a <b>drop (−)</b>.</li>
<li>Write: Σ rises − Σ drops = 0.</li>
<li>If a solved current comes out negative, it simply flows opposite to the way you drew it.</li>
</ol>
<div class="box ex"><span class="label">Worked example — KCL at two nodes</span>
A node has 7 A entering along one wire, and leaves as 3 A and I<sub>x</sub>. KCL: 7 = 3 + I<sub>x</sub> ⟹ I<sub>x</sub> = 4 A. If I<sub>x</sub> then splits at the next node into 1 A and I<sub>y</sub>, I<sub>y</sub> = 4 − 1 = 3 A.
</div>
'''

EXTRA1["a3"] = r'''
<h4 class="sub">Useful shortcuts</h4>
<ul>
<li><b>n equal resistors in parallel:</b> R<sub>eq</sub> = R/n. Two 10 Ω in parallel give 5 Ω.</li>
<li><b>Conductance form:</b> G<sub>eq</sub> = G<sub>1</sub> + G<sub>2</sub> + … for parallel (conductances add just like series resistances do).</li>
<li><b>Parallel is always smaller</b> than the smallest branch — a quick sanity check on your answer.</li>
<li><b>Power</b> divides too: in series the larger R dissipates more (P = I²R); in parallel the smaller R dissipates more (P = V²/R).</li>
</ul>
<div class="box ex"><span class="label">Worked example — series–parallel reduction</span>
A 12 V source feeds 2 Ω in series with (6 Ω ∥ 3 Ω).<br>
Step 1: 6 ∥ 3 = 18/9 = <code>2 Ω</code>. Step 2: R<sub>total</sub> = 2 + 2 = <code>4 Ω</code>. Step 3: I = 12/4 = <code>3 A</code>.<br>
Voltage across the parallel pair = 3 × 2 = <code>6 V</code> ⟹ 6 Ω carries 1 A, 3 Ω carries 2 A (sum = 3 A ✓). Check the divider: I<sub>3Ω</sub> = 3 × 6/(6+3) = 2 A ✓.
</div>
'''

EXTRA1["a4"] = r'''
<h4 class="sub">Steps</h4>
<ol>
<li>Mark all nodes; choose the one with the most branches as the reference (0 V).</li>
<li>Label the remaining node voltages V<sub>1</sub>, V<sub>2</sub>, …</li>
<li>At each unknown node write KCL: Σ (currents leaving) = 0, with each resistor current = (V<sub>node</sub> − V<sub>neighbour</sub>)/R.</li>
<li>Solve the n − 1 linear equations. Then find any branch current with Ohm's law.</li>
</ol>
<h4 class="sub">Matrix (conductance) form — spot the pattern</h4>
<p>For the A4 example (three 4 Ω resistors, G = 0.25 S each) the equations collapse to:</p>
<div class="formula">[ 0.5  −0.25 ; −0.25  0.5 ] · [V<sub>A</sub> ; V<sub>B</sub>] = [ 6 ; 0 ]</div>
<p>Diagonal = sum of conductances touching that node; off-diagonal = minus the conductance <em>between</em> the two nodes; right-hand side = current sources injected. You can write this by inspection — a real time-saver in exams.</p>
<div class="box why"><span class="label">Supernode — the only tricky case</span>
If a voltage source sits <em>between two non-reference nodes</em>, you cannot write a current through it (an ideal voltage source can carry any current). So merge the two nodes into a <b>supernode</b>: write one KCL for the pair, and add one extra equation V<sub>1</sub> − V<sub>2</sub> = V<sub>source</sub>.
</div>
'''

EXTRA1["a5"] = r'''
<h4 class="sub">Steps</h4>
<ol>
<li>Count meshes (windows). Draw a clockwise mesh current in each.</li>
<li>Write KVL round each mesh: (sum of R in the mesh) × own current − (shared R) × neighbour current = (source rise driving that mesh).</li>
<li>Solve the simultaneous equations.</li>
<li>Real current in a shared branch = difference of the two mesh currents (with sign showing direction).</li>
</ol>
<div class="box why"><span class="label">Supermesh — the only tricky case</span>
If a <em>current source</em> is a shared branch between two meshes, you can't write KVL across it (unknown voltage). Skip it: write one KVL round the big outer loop of the two meshes, and add the constraint I<sub>1</sub> − I<sub>2</sub> = I<sub>source</sub>.
</div>
<table>
<tr><th>Situation</th><th>Choose</th></tr>
<tr><td>Many current sources, few nodes</td><td>Node-voltage</td></tr>
<tr><td>Many voltage sources, few meshes</td><td>Mesh-current</td></tr>
<tr><td>Non-planar circuit</td><td>Node-voltage (mesh analysis needs planar)</td></tr>
</table>
'''

EXTRA1["a6"] = r'''
<div class="box mis"><span class="label">Two traps</span>
<b>1. Direction/polarity:</b> the current-source arrow must point <em>toward the + terminal</em> of the equivalent voltage source (the terminal the arrow leaves from is the + side).<br>
<b>2. Ideal sources:</b> a voltage source with <em>no</em> series resistance (or a current source with no parallel resistance) cannot be transformed. Also, a resistor in <em>parallel</em> with a voltage source, or in <em>series</em> with a current source, does not affect what the other elements see, so it can be dropped when analysing the rest of the circuit.
</div>
<div class="box ex"><span class="label">Worked example — going the other way</span>
A 2 A current source in parallel with 5 Ω ⟹ voltage source V = I·R = 2 × 5 = <code>10 V</code> in series with the same 5 Ω. Check: open-circuit voltage of the original = 2 × 5 = 10 V ✓; short-circuit current of the new one = 10/5 = 2 A ✓.
</div>
<p><b>Why bother?</b> Transform repeatedly to turn a ladder of mixed sources into one source with one resistor — often faster than writing any equation at all.</p>
'''

EXTRA1["a7"] = r'''
<h4 class="sub">Procedure</h4>
<ol>
<li>Remove the load; label terminals a–b.</li>
<li><b>V<sub>th</sub></b>: calculate the open-circuit voltage across a–b (any method).</li>
<li><b>R<sub>th</sub></b>: kill independent sources and find the resistance looking into a–b — <em>or</em> compute R<sub>th</sub> = V<sub>oc</sub>/I<sub>sc</sub>.</li>
<li>Draw V<sub>th</sub> in series with R<sub>th</sub>, reconnect the load, and solve the simple one-loop circuit.</li>
</ol>
<div class="box why"><span class="label">Why the second R<sub>th</sub> method works</span>
The Thevenin equivalent has an open-circuit voltage V<sub>th</sub> and, when shorted, delivers I<sub>sc</sub> = V<sub>th</sub>/R<sub>th</sub>. Rearranging gives R<sub>th</sub> = V<sub>oc</sub>/I<sub>sc</sub>. Useful when the network contains <b>dependent sources</b>: they must <em>not</em> be killed, so use V<sub>oc</sub>/I<sub>sc</sub> (or apply a test source) instead.
</div>
<div class="box ex"><span class="label">Worked example — using it to change the load</span>
With V<sub>th</sub> = 16 V and R<sub>th</sub> = 4 Ω (from above), what does a 12 Ω load draw?<br>
<code>I = 16/(4+12) = 1 A</code>, <code>V<sub>load</sub> = 12 V</code>. For a 4 Ω load: 2 A; for 28 Ω: 0.5 A. That is the power of Thevenin — solve the network once, then any load is a one-line calculation.
</div>
'''

EXTRA1["a8"] = r'''
<div class="box why"><span class="label">Efficiency vs power</span>
The current is I = V<sub>th</sub>/(R<sub>th</sub> + R<sub>L</sub>), so
<div class="formula">η = P<sub>load</sub>/P<sub>total</sub> = I²R<sub>L</sub> / [I²(R<sub>th</sub> + R<sub>L</sub>)] = R<sub>L</sub>/(R<sub>th</sub> + R<sub>L</sub>)</div>
At R<sub>L</sub> = R<sub>th</sub>, η = 1/2 = 50%. As R<sub>L</sub> → ∞, η → 100% but the power delivered drops to zero (almost no current). There's the trade-off.
</div>
<table>
<tr><th>R<sub>L</sub> (Ω) with V<sub>th</sub>=16 V, R<sub>th</sub>=4 Ω</th><th>I (A)</th><th>P<sub>load</sub> (W)</th><th>η</th></tr>
<tr><td>1</td><td>3.2</td><td>10.2</td><td>20%</td></tr>
<tr><td>2</td><td>2.67</td><td>14.2</td><td>33%</td></tr>
<tr><td><b>4 (matched)</b></td><td>2</td><td><b>16</b></td><td>50%</td></tr>
<tr><td>8</td><td>1.33</td><td>14.2</td><td>67%</td></tr>
<tr><td>16</td><td>0.8</td><td>10.2</td><td>80%</td></tr>
</table>
<p>Notice the symmetry: R<sub>L</sub> = 1 Ω and 16 Ω give the same power (R<sub>L</sub> and R<sub>th</sub>²/R<sub>L</sub> always pair up), with the peak between them.</p>
'''

EXTRA1["a9"] = r'''
<h4 class="sub">Steps</h4>
<ol>
<li>Keep one independent source; kill all the others (short voltage sources, open current sources).</li>
<li>Solve for the required voltage/current — label it with a subscript for that source.</li>
<li>Repeat for each source.</li>
<li>Add the individual responses <b>algebraically</b> (watch signs and reference directions).</li>
</ol>
<div class="box mis"><span class="label">Fixing a common misconception</span>
Superposition applies to <b>voltage and current</b>, not to <b>power</b>. Power is quadratic (I²R), and (I<sub>1</sub> + I<sub>2</sub>)² ≠ I<sub>1</sub>² + I<sub>2</sub>². Find the total current by superposition first, <em>then</em> compute the power.
<br>Quick proof: with I<sub>1</sub> = 3 A and I<sub>2</sub> = 1 A through 2 Ω, adding the separate powers gives 18 + 2 = 20 W but the real power is (4)²·2 = 32 W.
</div>
'''

EXTRA1["b1"] = r'''
<div class="box def"><span class="label">General form with phase</span>
<div class="formula">v(t) = V<sub>m</sub> sin(ωt + φ) &nbsp; ; &nbsp; T = 1/f &nbsp; ; &nbsp; ω = 2πf</div>
φ &gt; 0 means the wave starts <em>ahead</em> (leads the reference sin ωt); φ &lt; 0 means it lags.
</div>
<div class="box ex"><span class="label">Worked example — reading a waveform equation</span>
For v = 325 sin(314t + 30°): peak V<sub>m</sub> = <code>325 V</code>; ω = 314 rad/s ⟹ f = 314/2π = <code>50 Hz</code>; T = 1/50 = <code>20 ms</code>; phase = <code>+30°</code> (leads sin 314t by 30°); V<sub>rms</sub> = 325/√2 ≈ <code>230 V</code>; and at t = 0 the instantaneous value is 325 sin 30° = <code>162.5 V</code>.
</div>
<h4 class="sub">Lead and lag in one line</h4>
<p>Two waves of the same frequency are compared by the <em>angle between their zero-crossings or peaks</em>. The one that reaches its peak earlier <b>leads</b>. Phase difference is only meaningful when frequencies are equal.</p>
'''

EXTRA1["b2"] = r'''
<div class="box why"><span class="label">Why RMS is called the 'effective' value</span>
Heat in a resistor is P = i²R, so the <em>average</em> heating of an AC current is R × mean(i²). A DC current I<sub>dc</sub> gives I<sub>dc</sub>²R. Setting them equal: I<sub>dc</sub> = √mean(i²) = I<sub>rms</sub>. So a 5 A rms AC current heats a heater exactly like 5 A DC — that is why all AC ratings quote RMS.
</div>
<h4 class="sub">Same recipe, other waveforms (peak = V<sub>m</sub>)</h4>
<table>
<tr><th>Waveform</th><th>V<sub>avg</sub></th><th>V<sub>rms</sub></th><th>Form factor</th><th>Peak factor</th></tr>
<tr><td>Sine (full-cycle rectified average)</td><td>0.637 V<sub>m</sub></td><td>0.707 V<sub>m</sub></td><td>1.11</td><td>1.414</td></tr>
<tr><td>Full-wave rectified sine</td><td>0.637 V<sub>m</sub></td><td>0.707 V<sub>m</sub></td><td>1.11</td><td>1.414</td></tr>
<tr><td>Half-wave rectified sine</td><td>0.318 V<sub>m</sub></td><td>0.5 V<sub>m</sub></td><td>1.57</td><td>2</td></tr>
<tr><td>Square wave (±V<sub>m</sub>)</td><td>V<sub>m</sub></td><td>V<sub>m</sub></td><td>1</td><td>1</td></tr>
</table>
<p>The half-wave numbers (0.318 and 0.5) are the same ones that appear in the rectifier formulas I<sub>dc</sub> = I<sub>m</sub>/π and I<sub>rms</sub> = I<sub>m</sub>/2 later in the course.</p>
<div class="box ex"><span class="label">Worked example — reading an instrument</span>
A moving-coil (average-responding) meter calibrated in RMS assumes form factor 1.11. If it reads 10 V on a sine wave, V<sub>avg</sub> = 10/1.11 = 9.0 V. If the same meter is used on a square wave whose V<sub>avg</sub> is actually 9.0 V, the true RMS is 9.0 × 1 = 9.0 V — but the meter still shows 10 V, an 11% error. Lesson: form factor depends on waveform shape.
</div>
'''

EXTRA1["b3"] = r'''
<h4 class="sub">The three elements in the AC world</h4>
<table>
<tr><th></th><th>Resistor</th><th>Inductor</th><th>Capacitor</th></tr>
<tr><td>Impedance</td><td>R</td><td>jωL = jX<sub>L</sub></td><td>1/(jωC) = −jX<sub>C</sub></td></tr>
<tr><td>Reactance vs f</td><td>constant</td><td>rises with f</td><td>falls with f</td></tr>
<tr><td>Phase</td><td>V, I in phase</td><td>I lags V by 90°</td><td>I leads V by 90°</td></tr>
<tr><td>At DC (f = 0)</td><td>R</td><td>acts as a short</td><td>acts as an open circuit</td></tr>
<tr><td>At very high f</td><td>R</td><td>acts like an open circuit</td><td>acts like a short</td></tr>
</table>
<p><b>Memory aid:</b> <em>ELI the ICE man</em> — in an inductor (L), voltage E leads current I; in a capacitor (C), current I leads voltage E.</p>
<h4 class="sub">Converting between forms</h4>
<div class="formula">a + jb → magnitude √(a² + b²), angle tan⁻¹(b/a) &nbsp;&nbsp;|&nbsp;&nbsp; V∠θ → V cos θ + j V sin θ</div>
<div class="box ex"><span class="label">Worked example — one impedance, both forms</span>
Z = 3 + j4 Ω = 5∠53.13° Ω. A current of 2∠0° A gives V = Z·I = 10∠53.13° V, i.e. the voltage leads the current by 53.13°. Divide back: V/I = 5∠53.13° ✓. For a 50 Hz supply, X<sub>L</sub> = 4 Ω means L = X<sub>L</sub>/ω = 4/314 = 12.7 mH.
</div>
<div class="box mis"><span class="label">Fixing a common misconception</span>
Reactance is <em>not</em> resistance: a pure inductor or capacitor dissipates no real power. Reactance limits current and shifts phase, but the energy is stored and returned each cycle, not turned into heat.
</div>
'''

EXTRA1["b4"] = r'''
<div class="box ex"><span class="label">Worked example — series RC</span>
R = 3 Ω, X<sub>C</sub> = 4 Ω, V = 50 V rms. Z = 3 − j4 ⟹ |Z| = 5 Ω, φ = −53.13° (current <b>leads</b> the voltage). I = 50/5 = <code>10 A</code>. V<sub>R</sub> = 30 V, V<sub>C</sub> = 40 V, and these add as a right triangle: √(30² + 40²) = 50 V ✓ — <em>not</em> 30 + 40 = 70 V.
</div>
<div class="box ex"><span class="label">Worked example — series RLC</span>
R = 4 Ω, X<sub>L</sub> = 9 Ω, X<sub>C</sub> = 6 Ω, V = 100 V.<br>
Net reactance X = 9 − 6 = <code>3 Ω</code> (inductive). Z = 4 + j3 ⟹ |Z| = 5 Ω, φ = tan⁻¹(3/4) = <code>36.87° lagging</code>. I = 100/5 = <code>20 A</code>. cos φ = 0.8.<br>
Individual voltages: V<sub>R</sub> = 80 V, V<sub>L</sub> = 180 V, V<sub>C</sub> = 120 V. Note V<sub>L</sub> and V<sub>C</sub> can each be <em>larger than the supply</em> — they partially cancel (180 − 120 = 60 V), and √(80² + 60²) = 100 V ✓.
</div>
<h4 class="sub">Resonance in detail</h4>
<div class="box why"><span class="label">Why f<sub>0</sub> = 1/(2π√(LC))</span>
X<sub>L</sub> = X<sub>C</sub> ⟹ ωL = 1/(ωC) ⟹ ω² = 1/(LC) ⟹ ω<sub>0</sub> = 1/√(LC), so f<sub>0</sub> = ω<sub>0</sub>/2π.
</div>
<ul>
<li>At resonance: Z = R (minimum), I = V/R (maximum), φ = 0, pf = 1.</li>
<li>V<sub>L</sub> and V<sub>C</sub> are equal and opposite, each = Q × V (can be many times the supply).</li>
<li>Below f<sub>0</sub> the circuit is capacitive; above f<sub>0</sub> it is inductive.</li>
</ul>
@@RESONANCE_SVG@@
'''

EXTRA1["b5"] = r'''
<h4 class="sub">How each element handles power</h4>
<table>
<tr><th>Element</th><th>P (real)</th><th>Q (reactive)</th></tr>
<tr><td>Resistor</td><td>I²R</td><td>0</td></tr>
<tr><td>Inductor</td><td>0</td><td>+I²X<sub>L</sub> (absorbs VARs)</td></tr>
<tr><td>Capacitor</td><td>0</td><td>−I²X<sub>C</sub> (supplies VARs)</td></tr>
</table>
<p>Complex power gathers everything: <b>S</b> = P + jQ, with |S| = VI. Because inductive and capacitive Q have opposite signs, a capacitor can 'cancel' an inductor's Q — the basis of power-factor correction.</p>
<div class="box ex"><span class="label">Worked example — power-factor correction</span>
A motor-like load draws P = 300 W at pf 0.6 lagging (from the B5 example: S = 500 VA, Q = 400 VAR). We want pf 0.8 lagging.<br>
New angle: cos φ₂ = 0.8 ⟹ tan φ₂ = 0.75 ⟹ Q₂ = P tan φ₂ = 300 × 0.75 = <code>225 VAR</code>.<br>
Capacitor must supply Q<sub>C</sub> = 400 − 225 = <code>175 VAR</code>.<br>
Effect on current: before, S = 500 VA ⟹ I = 10 A at 50 V. After, S₂ = P/cos φ₂ = 300/0.8 = 375 VA ⟹ I = 7.5 A. The supply now carries 25% less current for the <em>same</em> 300 W of useful power.
</div>
<div class="box mis"><span class="label">Fixing a common misconception</span>
Power in AC is <b>not</b> simply V × I with rms values — that is only the <em>apparent</em> power. Multiply by the power factor to get the real power that does the work. Also, add P's arithmetically and Q's algebraically; <b>never add S's directly</b> — S is the length of a vector.
</div>
'''
