from sections import *
import diagrams_a as A

B6 = sec("b6", "B6. Energy &amp; Electricity-Bill Calculations", "Energy = power × time, the kWh 'unit', and working out a household bill from appliance ratings.",
 [("Energy", "power × time; joules (J) or watt-hours. 1 kWh = 3.6 × 10⁶ J."), ("Unit (kWh)", "the billing unit: 1 kW used for 1 hour."), ("Rating", "the power (W) an appliance draws at rated voltage."),
  ("Load profile", "how long, and at what duty, each appliance runs."), ("Tariff", "the price per unit (₹/kWh); may be slab-based."), ("Energy meter", "an instrument that integrates P over time and shows kWh.")],
 D("<div class='formula'>E (kWh) = P (kW) × t (h) &nbsp;; &nbsp; for AC: E = V I cos φ × t</div>Only <em>real</em> power P = VI cos φ is billed to households; large industrial users are also charged for kVA demand / poor power factor (B5).")
 + E("Appliances: 4 LED bulbs of 10 W for 5 h; a 75 W fan for 10 h; a 1.5 kW AC for 6 h; a 150 W fridge that runs half the day (12 h).<br>"
     "Energy/day = 4×10×5 + 75×10 + 1500×6 + 150×12 = 200 + 750 + 9000 + 1800 = <code>11 750 Wh = 11.75 kWh</code>.<br>"
     "30 days: 352.5 kWh. At an assumed ₹6/unit the bill is <code>≈ ₹2115</code>. The AC alone is 77% of it — the heaviest load decides the bill.")
 + M("kW and kWh are different things: kW is a <em>rate</em> (power), kWh is an <em>amount</em> (energy). A 2 kW heater costs 2 units in one hour, but only 0.2 unit in 6 minutes."))

C7 = sec("c7", "C7. Single-Phase Induction Motor", "Why a single-phase induction motor cannot start by itself, and the five starting methods (split-phase, capacitor-start, CSCR, PSC, shaded-pole).",
 [("Pulsating field", "the field of one winding on single-phase AC: fixed axis, magnitude varying sinusoidally."), ("Forward / backward flux (φf, φb)", "the two equal, oppositely rotating halves of a pulsating field."),
  ("Main winding", "low resistance, high reactance winding that stays in circuit."), ("Auxiliary (starting) winding", "second winding, 90° away in space, used to make a rotating field at start."),
  ("Centrifugal switch", "disconnects the starting winding at about 70–80% of synchronous speed."), ("Capacitor-start / CSCR / PSC", "ways of making the auxiliary current lead the main current."),
  ("Shaded-pole", "copper rings on part of each pole delay the flux there, giving a weak rotating effect.")],
 P("Used where only single-phase supply exists: fans, hair-dryers, washing machines, vacuum cleaners, mixers, refrigerators, pumps. Rating is fractional kW. The rotor is a squirrel cage and the stator has a main winding and (except in shaded-pole types) an auxiliary winding in space quadrature; N<sub>s</sub> = 120f/P as before.")
 + W("A single winding on AC produces a field that merely pulsates along one axis. That pulsating field equals two fields φ<sub>f</sub> and φ<sub>b</sub> of half amplitude rotating in opposite directions. At standstill they produce equal and opposite torques, so the net starting torque is <b>zero</b> — the motor hums but does not turn. Once pushed in either direction, the rotor sees one component more than the other and keeps accelerating. So a <em>starting aid</em> is required.", "Why it is not self-starting")
 + T(["Type", "How the starting phase shift is made", "Notes / use"],
     [["Split-phase (resistance-start)", "auxiliary winding has high R, low X → its current is nearly in phase with V; the main winding lags; ≈30° phase difference", "low starting torque, 1.5–2× rated; fans, blowers, small pumps"],
      ["Capacitor-start", "capacitor C<sub>s</sub> in series with the auxiliary winding; currents ≈ 90° apart", "high starting torque; compressors, refrigerators; switch cuts C<sub>s</sub> out"],
      ["Capacitor-start capacitor-run (two-value)", "C<sub>s</sub> + C<sub>R</sub> in parallel at start; C<sub>s</sub> removed, small C<sub>R</sub> stays", "high starting torque and good running power factor"],
      ["Permanent-split capacitor (PSC)", "one capacitor permanently in series with the auxiliary winding; no switch", "uniform torque, quiet; fans, HVAC, small domestic equipment; low starting torque"],
      ["Shaded-pole", "shading ring delays flux in part of the pole", "tiny, cheap, low torque and efficiency; small fans, toys"]])
 + A.d_cap_start()
 + E("A 4-pole single-phase motor on a 50 Hz supply: N<sub>s</sub> = 120×50/4 = <code>1500 rpm</code>. At 1440 rpm the slip is (1500−1440)/1500 = <code>4%</code>. The starting winding is cut out near 70–80% of 1500, i.e. around 1050–1200 rpm."))

C8 = sec("c8", "C8. BLDC Motor (Brushless DC)", "Permanent-magnet rotor, stator coils switched electronically in a six-step sequence; no brushes or commutator.",
 [("BLDC", "brushless DC motor: DC-supplied, electronically commutated."), ("Permanent-magnet rotor", "rotor carries the magnets; no windings, no brushes."), ("Stator coils", "three coils (U, V, W) fixed on the stator."),
  ("Electronic commutation", "an inverter/driver switches coil currents using rotor-position information."), ("Hall sensors", "sense rotor position so the controller knows when to switch."), ("Six-step (120°) drive", "two of three coils energised at a time; six states per electrical revolution.")],
 P("In a brushed DC motor the commutator switches the <em>rotor</em> coils. In a BLDC the coils are on the <em>stator</em> and the permanent magnet turns, so the commutation is done by transistors. A 3-coil motor has six leads; usually three are joined, leaving three wires to the controller. Speed is set by the magnitude of the applied voltage (and switching), direction by the order of energising.")
 + A.d_bldc()
 + T(["Mode", "Energised", "Resultant flux"], [["1", "U → W", "↘"], ["2", "U → V", "↙"], ["3", "W → V", "←"], ["4", "W → U", "↖"], ["5", "V → U", "↗"], ["6", "V → W", "→"]])
 + T(["Advantages", "Limitations"],
     [["no brush wear → low maintenance and long life; low electrical and acoustic noise; high efficiency and power-to-size ratio; good thermal behaviour (heat in the stator); higher speed range; fast dynamic response (low rotor inertia)",
       "costly; needs an electronic controller and complex drive circuitry; needs position sensors (or sensorless algorithms)"]])
 + P("<b>Applications:</b> hard-disk drives, electric vehicles and e-bikes, drones, industrial robots and CNC machines, washing machines, compressors, fans, pumps and blowers."))

C9 = sec("c9", "C9. Stepper Motor", "A motor that turns in fixed steps for each pulse — precise position control without feedback.",
 [("Step angle", "the rotation per pulse; typically 0.9°–1.8° (200–400 steps/rev)."), ("Open-loop control", "pulses are counted; no position feedback."), ("PM / VR / hybrid", "permanent-magnet, variable-reluctance and hybrid stepper types."),
  ("Phase", "one stator winding set that is energised as a unit."), ("Missed step", "a step lost because of overload; undetectable in open loop."), ("Holding torque", "torque at standstill with the winding energised.")],
 P("A stator with several windings is energised in a programmed sequence by an electronic driver; the permanent-magnet (or toothed soft-iron) rotor aligns with the energised pole. Each pulse gives one step; rotor angle ∝ number of pulses, speed ∝ pulse frequency.")
 + A.d_stepper()
 + FM("step angle = 360° / (steps per revolution) &nbsp;; &nbsp; N (rpm) = (step angle × pulse rate) × 60 / 360")
 + E("A motor with 1.8° steps has 360/1.8 = <code>200 steps/rev</code>. At 1000 pulses per second: N = 1000 × 60/200 = <code>300 rpm</code>. The 2-phase, 2-pole PM example in the figure has a step of 360/(2×2) = 90°; energising two phases at once (half-stepping) reduces the step.")
 + T(["Advantages", "Disadvantages"],
     [["full torque at standstill; good response to start/stop/reverse; no brushes → reliable; angle ∝ input pulses; simple, cheap open-loop control; speed ∝ pulse frequency; 3–5% step accuracy, non-cumulative; safe, cheap compared with servos",
       "low efficiency; torque falls quickly with speed; no feedback — missed steps go unnoticed; low torque-to-inertia, cannot accelerate loads quickly; noisy"]])
 + P("<b>Applications:</b> 3D printers, CNC machines, robotics, automation, medical devices, camera and security systems, textile machinery, consumer electronics."))

C10 = sec("c10", "C10. Alternator (Synchronous Generator)", "Stationary armature + rotating field: how an AC generator makes three-phase power at a fixed frequency.",
 [("Alternator", "AC generator: converts mechanical energy to AC electrical energy."), ("Prime mover", "the engine or turbine that turns the rotor."), ("Salient-pole rotor", "projecting poles; low speed (hydro, diesel)."),
  ("Cylindrical (non-salient) rotor", "smooth round rotor; high speed (steam turbines)."), ("Slip rings", "bring DC to the rotating field winding."), ("Synchronous speed", "N = 120f/P — the speed that gives frequency f.")],
 P("Unlike a DC generator, whose armature rotates, an alternator has its <b>armature winding on the stator</b> and its <b>field winding on the rotor</b>. The rotor field (DC through slip rings) rotates and cuts the stationary conductors; three windings 120° apart give a balanced three-phase output.")
 + A.d_alternator()
 + FM("f = P N / 120 &nbsp;(Hz) &nbsp;&nbsp;|&nbsp;&nbsp; N = 120 f / P")
 + E("A 4-pole alternator must turn at N = 120×50/4 = <code>1500 rpm</code> to give 50 Hz; a 2-pole turbo-alternator at 3000 rpm; a 24-pole hydro machine at 250 rpm.")
 + T(["Advantages over a DC generator", "Drawbacks"],
     [["output taken directly from stationary terminals — no brushes/slip rings in the power path, little sparking and maintenance; no brush voltage drop; higher efficiency and voltage; field excited by low DC voltage; lighter, compact, simple, cheaper; smooth high-speed running",
       "needs efficient cooling for large currents; needs a diode rectifier if DC is wanted (as in a car alternator)"]])
 + P("<b>Applications:</b> power stations, cars and locomotives, aircraft, standby/emergency sets, renewable energy (wind and hydro), marine use."))

D1 = sec("d1", "D1. Concepts of Power Electronics", "Switching devices that convert and control electrical power: rectifier, inverter, chopper; PWM and efficiency.",
 [("Power electronics", "use of semiconductor switches to convert and control electrical power."), ("Converter", "a circuit changing the form of electrical energy (AC/DC, voltage level, frequency)."),
  ("Rectifier / Inverter / Chopper", "AC→DC / DC→AC / DC→DC converters."), ("SCR (thyristor), MOSFET, IGBT", "common switching devices; the BJT and diode are also used."),
  ("PWM", "pulse-width modulation: varying the ON fraction (duty cycle) to control the average output."), ("Duty cycle D", "ON time ÷ period."), ("Harmonics", "unwanted extra frequencies produced by switching.")],
 P("Power electronics <em>manages and converts electrical energy using semiconductor devices</em>. The key idea is to run the devices as <b>switches</b> (fully ON or fully OFF), because an ideal switch dissipates almost no power: ON, it has ≈ 0 V across it; OFF, it carries ≈ 0 A. This is why converters are efficient.")
 + A.d_pe_block() + A.d_converters()
 + FM("Chopper (DC–DC step-down): V<sub>out</sub> = D · V<sub>in</sub> &nbsp;&nbsp;, &nbsp; D = t<sub>on</sub> / T")
 + E("From a 48 V battery a chopper with D = 0.25 gives 0.25 × 48 = <code>12 V</code> average. A linear regulator dropping 48 V to 12 V at 2 A would waste (48−12)×2 = 72 W of the 96 W drawn (η = 25%), whereas a switching converter loses only a few watts (η ≈ 90%+). The 'DC–DC buck converter speed control of a car wiper motor' lab uses exactly this.")
 + P("<b>Control methods:</b> PWM adjusts the width of switching pulses. <b>Side effect:</b> switching creates harmonic distortion in currents and voltages, which filters and good design must manage."))

D2 = sec("d2", "D2. Industrial Applications of Electrical Drives", "An electric drive = source + power converter + motor + load with sensing and control; VFDs for speed control of pumps, fans, robots, EVs.",
 [("Electric drive", "system that converts electrical energy to controlled mechanical motion."), ("VFD (variable-frequency drive)", "converter that varies the frequency and voltage fed to an AC motor to control its speed."),
  ("V/f control", "keeping voltage ∝ frequency so the motor flux stays constant."), ("Regenerative braking", "the motor acts as a generator, returning energy to the supply/battery."), ("Affinity laws", "for fans and pumps: flow ∝ N, pressure ∝ N², power ∝ N³."),
  ("Feedback loop", "sensor → control unit → converter, so the drive follows the reference.")],
 A.d_drive_block()
 + P("A <b>VFD</b> rectifies the supply, then inverts it to AC of adjustable frequency and voltage; since N<sub>s</sub> = 120f/P, changing f changes the motor speed smoothly. Keeping V/f constant keeps the flux (and torque capability) constant.")
 + E("4-pole motor, 400 V at 50 Hz: N<sub>s</sub> = 1500 rpm. At 30 Hz: N<sub>s</sub> = 120×30/4 = <code>900 rpm</code> and V = 400×30/50 = <code>240 V</code> (V/f constant).<br>"
     "Energy saving: a 10 kW fan run at 80% speed needs 10 × 0.8³ = <code>5.12 kW</code> — about half the power for 20% less flow, which is why VFDs are used on pumps and fans instead of throttling.")
 + UL(["<b>Manufacturing and automation:</b> conveyors, pumps, fans — speed matched to the process, saving energy and giving better control.", "<b>Robotics:</b> precise, dynamic speed and position control of joints.",
       "<b>Electric vehicles:</b> battery DC → AC for the motor; regenerative braking recovers energy.", "<b>Others:</b> lifts, escalators, industrial mixers, cranes."]))

E1 = sec("e1", "E1. Earthing", "Earthing gives fault current a low-resistance path to the ground; plate, rod and pipe earthing; earthing vs grounding.",
 [("Earthing", "connecting exposed metal parts of an installation to the general mass of earth through a low-resistance conductor."), ("Fault current", "abnormal current from a leak or short circuit."), ("Earth electrode", "plate, rod or pipe buried in the ground."),
  ("Touch voltage", "the voltage a person touching a faulty metal body would experience."), ("Equipotential", "all metal parts held at nearly the same potential, so no dangerous voltage difference."), ("Protective device", "fuse, MCB, ELCB/RCCB that disconnects the supply on a fault.")],
 D("The <b>principle of earthing</b> is to provide a <em>low-resistance path to earth for fault currents</em>. If a live wire leaks or shorts to a metal case, the current then runs safely into the ground, harming nobody, and the large current operates the protective device.")
 + A.d_earthing()
 + E("Without earthing, a metal body at 230 V stays live until someone touches it; a body of 1 kΩ then carries 230 mA — in the fatal range (E2). With a 1 Ω earth wire in parallel with the person (1000 Ω), the current divider (A3) sends 1000/1001 ≈ <code>99.9%</code> of the fault current through the earth wire; the large fault current blows the fuse / trips the MCB.")
 + T(["Type", "Description"],
     [["Plate earthing", "copper or galvanised-iron plate buried in the ground, connected to the system by an earthing conductor"], ["Rod earthing", "most common: a metal rod driven vertically into the ground, joined by an earthing conductor"],
      ["Pipe earthing", "galvanised-steel or copper pipe driven deeper than other electrodes, for lower resistance"]])
 + T(["Earthing", "Grounding (as given in the slides)"],
     [["protects people and equipment by giving fault currents an equipotential path to earth", "stabilises the electrical system, preventing voltage fluctuations and giving proper current flow to devices"],
      ["connects the system/equipment directly to the Earth (soil)", "connects a system to a reference point, usually Earth, to stabilise potentials"],
      ["focused on safety — prevents shock, discharges faults", "stabilises voltage levels, avoids over-voltage"], ["applied to all metallic parts and appliances", "applied mainly to electrical circuits, esp. neutral conductors"]])
 + M("The earth pin of a plug is longer and thicker on purpose: it connects first and breaks last, so the body is earthed whenever the appliance is live. Never remove it, and never rely on the neutral as a substitute for the earth wire.")
 + F("The 'measurement of earth resistance' lab experiment checks exactly this: an electrode's resistance should be as low as practicable so that the fault current is large enough to trip the protective device."))

E2 = sec("e2", "E2. Electrical Hazards &amp; Safety", "Shock, burns, arc, explosion, fire; effect of current levels; the five ways accidents are prevented.",
 [("Electric shock", "current passing through the body."), ("Burns", "heating of tissue by current or by an arc."), ("Arc (arc flash)", "a sudden discharge through air that releases intense heat and light."), ("Fibrillation", "uncontrolled twitching of the heart that stops circulation."),
  ("Insulation", "non-conducting covering that keeps live parts from contact."), ("Fuse / MCB", "devices that interrupt a circuit on overcurrent."), ("PPE", "personal protective equipment: insulating gloves, shoes, mats, face shield.")],
 UL(["<b>Shock</b>", "<b>Burns</b>", "<b>Arc</b>", "<b>Explosions</b>", "<b>Fires</b>"])
 + P("<b>Common causes of electrocution:</b> touching overhead lines; maintenance on live equipment; damaged equipment (extension leads, plugs, sockets); equipment affected by rain or water.")
 + A.d_current_zones()
 + T(["AC current (mA)", "Effect on the human body"],
     [["1", "slight tingling"], ["2–9", "small shock"], ["10–24", "muscles contract, you 'freeze' to the conductor"], ["25–74", "respiratory muscles can be paralysed; pain; exit burns often visible"],
      ["75–300", "usually fatal — ventricular fibrillation"], ["&gt; 300", "death almost certain; if survived, badly burnt organs, possible amputation"]])
 + E("Body resistance depends on skin condition: dry ≈ 100 kΩ, wet or sweaty only ≈ 1 kΩ. At 230 V: dry skin → 2.3 mA (a tingle), wet skin → 230 mA (fatal). The same supply is harmless or deadly depending on the circuit through the body — which is why water and electricity are such a dangerous combination.")
 + H("Preventing electrical accidents")
 + UL(["<b>Insulation</b> on all live conductors.", "<b>Electrical protective devices</b> — fuses, circuit breakers, earth-leakage devices (RCCB/ELCB) that cut the supply in milliseconds.",
       "<b>Guarding</b> — live parts enclosed so accidental contact is impossible.", "<b>Earthing &amp; grounding</b> (E1).", "<b>Personal protective equipment</b> — gloves, insulated shoes and mats, tools."])
 + M("A fuse or MCB protects the <em>wiring and equipment</em> from overload and short circuit; it does <em>not</em> reliably protect a person, because a fatal 100 mA is far below its rating. Personal protection needs an earth-leakage device (which trips at about 30 mA)."))

SECTIONS = [B6, C7, C8, C9, C10, D1, D2, E1, E2]
