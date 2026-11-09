from sections import *
import diagrams_a as A

p1 = sec("p1", "P1. PN Junction Diode", "P and N regions, the depletion layer and barrier potential, forward/reverse bias, the diode equation and silicon vs germanium.",
 [("Semiconductor", "material between conductor and insulator (Si, Ge); conductivity set by doping."), ("P-type / N-type", "doped with acceptor / donor impurity; majority carriers holes / electrons."), ("Majority / minority carriers", "the dominant carrier type / the other type in a doped region."),
  ("Diffusion", "carriers moving from high to low concentration across the junction."), ("Depletion layer", "region near the junction emptied of free carriers, holding fixed ions."), ("Barrier potential (V₀)", "≈ 0.7 V (Si), 0.3 V (Ge)."),
  ("Forward / reverse bias", "+ on P and − on N / the opposite."), ("Saturation current (I<sub>s</sub>)", "tiny reverse current due to minority carriers."), ("Knee (cut-in) voltage", "forward voltage where current starts to rise rapidly.")],
 P("A junction diode has one half doped p-type (mobile holes) and the other n-type (mobile electrons). Holes diffuse into the n-side and electrons into the p-side; the region A near the junction on the p-side acquires an excess of negative charge and region B on the n-side a surplus of positive charge. These charges repel further migration and create a <b>potential barrier</b>.")
 + A.d_pn_junction() + A.d_pn_bias()
 + P("<b>Forward bias:</b> drift of holes toward the junction in the p-region and of electrons the other way in the n-region; they combine near the junction while the battery keeps supplying new carriers — current is hole flow in the p-region, electron flow in the n-region, and a mix near the junction. <b>Reverse bias:</b> holes and electrons are pulled away, widening the <em>depletion layer</em>, which behaves as an insulator; only a small current due to <em>minority carriers</em> (thermally generated electron–hole pairs, life ≈ 50 µs in Si, 100 µs in Ge) flows — the <em>saturation current</em>.")
 + A.d_diode_vi()
 + FM("i = I<sub>s</sub> ( e<sup>e v / kT</sup> − 1 ) &nbsp;&nbsp; e = 1.6×10⁻¹⁹ C, k = 1.38×10⁻²³ J/K, T = 273.15 + θ °C")
 + T(["Silicon vs germanium", ""],
     [["forward drop", "≈ double that of germanium (0.7 V vs 0.3 V)"], ["reverse current", "about 1/100 of germanium's at the same T and V"], ["max reverse voltage / temperature", "much higher; Si works to ≈150–200 °C, Ge to ≈75–90 °C"], ["reverse current vs temperature", "doubles every 8 °C in Si (10 °C in Ge)"]])
 + E("<b>1.</b> Si diode, I<sub>s</sub> = 10⁻¹² A, 300 K (kT/e = 25.9 mV), v = 0.6 V: i = 10⁻¹²(e<sup>0.6/0.0259</sup> − 1) = 10⁻¹² × 1.15×10¹⁰ ≈ <code>11.5 mA</code>.<br>"
     "<b>2.</b> 5 V source, 1 kΩ, Si diode forward: I = (5 − 0.7)/1000 = <code>4.3 mA</code>.<br>"
     "<b>3.</b> Reverse current 10 nA at 25 °C; at 57 °C (32 °C higher = 4 doublings) it is 10 × 2⁴ = <code>160 nA</code>."))

p2 = sec("p2", "P2. Zener Diode", "A heavily doped diode designed to operate in reverse breakdown as a voltage reference.",
 [("Zener diode", "diode designed for use in reverse breakdown (4–75 V typical)."), ("Breakdown voltage V<sub>Z</sub>", "the nearly constant voltage across the diode after breakdown (reference voltage)."), ("Zener / avalanche effect", "the two breakdown mechanisms (Zener below ≈5 V, avalanche above)."),
  ("I<sub>Z(min)</sub> / I<sub>Z(max)</sub>", "minimum current to stay in regulation / maximum before power limit."), ("P<sub>Z</sub>", "maximum power rating of the Zener.")],
 P("<em>Special junction diode — voltage-regulator diode:</em> reverse breakdown voltage in the range of about 4 V to 75 V depending on the type. Forward-biased it behaves as a normal diode. As the reverse voltage rises, a value is reached where the current rises very rapidly because the increased velocity of the carriers causes ionisation. The voltage across the diode after breakdown is the <b>reference voltage</b> and stays practically constant over a wide range of current provided the maximum junction temperature is not exceeded. It is heavily doped, which gives a thin depletion layer and a sharp, low breakdown voltage.")
 + A.d_zener_vi()
 + T(["Feature", "PN junction diode", "Zener diode"], [["Main use", "rectification", "voltage regulation"], ["Forward bias", "conducts", "conducts"], ["Reverse bias", "blocks until breakdown", "conducts at V<sub>Z</sub>"], ["Breakdown voltage", "high, not controlled", "low, precisely set"], ["Doping", "normal", "heavily doped"]])
 + E("A 5.1 V, 500 mW Zener: maximum current I<sub>Z(max)</sub> = P/V<sub>Z</sub> = 0.5/5.1 ≈ <code>98 mA</code>. In use it must stay between I<sub>Z(min)</sub> (a few mA) and this limit.")
 + M("A Zener always works reverse-biased; a resistor is essential to limit the current — without it, the sharp breakdown current would destroy the device."))

p3 = sec("p3", "P3. Voltage Regulator (Zener shunt regulator)", "Series resistor + Zener across the load to hold a constant DC output despite supply or load changes.",
 [("Regulation", "keeping the output voltage constant."), ("Line regulation", "stability when the input voltage changes."), ("Load regulation", "stability when the load current changes."), ("R<sub>s</sub>", "series (current-limiting) resistor."), ("Shunt regulator", "regulating element in parallel with the load.")],
 P("R<sub>s</sub> is in series with the Zener to limit the current, V<sub>s</sub> being across the combination; the stabilised output is taken across the Zener (V<sub>out</sub> = V<sub>Z</sub>) and the load R<sub>L</sub> is in parallel with it. There is a <em>minimum</em> Zener current for which regulation is effective, so the Zener current must always stay above it; the upper limit depends on the power rating. With no load (I<sub>L</sub> = 0) all the circuit current passes through the Zener, which then dissipates its maximum power.")
 + A.d_zener_reg()
 + FM("I<sub>S</sub> = (V<sub>in</sub> − V<sub>Z</sub>)/R<sub>s</sub> = I<sub>Z</sub> + I<sub>L</sub> &nbsp;;&nbsp; R<sub>s</sub> ≤ (V<sub>in,min</sub> − V<sub>Z</sub>) / (I<sub>Z,min</sub> + I<sub>L,max</sub>)")
 + E("V<sub>in</sub> = 12 V, V<sub>Z</sub> = 5.1 V, I<sub>L</sub> up to 20 mA, I<sub>Z,min</sub> = 5 mA: R<sub>s</sub> ≤ (12 − 5.1)/(25 mA) = 276 Ω → choose <code>270 Ω</code>. At no load: I = 6.9/270 = 25.6 mA, P<sub>Z</sub> = 5.1 × 25.6 mA = 130 mW — safe for a 500 mW Zener. Power in R<sub>s</sub> = (25.6 mA)² × 270 = 177 mW (use a ¼ W resistor or larger).")
 + P("Related lab: <em>design and development of a 5 V charger</em> = transformer → rectifier (P6) → filter → Zener/regulator."))

p4 = sec("p4", "P4. Bipolar Junction Transistor (BJT)", "Three-layer NPN/PNP device; α, β, the CB/CE/CC configurations and characteristics.",
 [("BJT", "transistor whose operation depends on both electron and hole carriers; current-controlled."), ("Emitter / Base / Collector", "heavily doped injector / thin lightly doped control layer / collector."), ("NPN / PNP", "n-p-n and p-n-p layer orders."),
  ("α (alpha)", "ΔI<sub>C</sub>/ΔI<sub>E</sub> for common base (≈ 0.95–0.99)."), ("β (beta)", "ΔI<sub>C</sub>/ΔI<sub>B</sub> for common emitter (20–200)."), ("Cut-off / active / saturation", "OFF / amplifying / fully ON regions.")],
 P("A BJT has three regions and two junctions: <b>emitter</b>, <b>base</b>, <b>collector</b>. In normal (active) operation the emitter–base junction is forward-biased and the collector–base junction reverse-biased. The arrow on the emitter shows conventional emitter-current direction: <em>out</em> of an NPN, <em>in</em> to a PNP.")
 + A.d_bjt()
 + FM("I<sub>E</sub> = I<sub>B</sub> + I<sub>C</sub> &nbsp;;&nbsp; α = ΔI<sub>C</sub>/ΔI<sub>E</sub> &nbsp;;&nbsp; β = ΔI<sub>C</sub>/ΔI<sub>B</sub> &nbsp;;&nbsp; α = β/(1+β) &nbsp;;&nbsp; β = α/(1−α)")
 + A.d_bjt_curves()
 + T(["Feature", "Common base (CB)", "Common emitter (CE)", "Common collector (CC)"],
     [["Input / output", "emitter–base / collector–base", "base–emitter / collector–emitter", "base–collector / emitter–collector"], ["Current gain", "low (α ≈ 0.95)", "medium (β 20–200)", "high (β + 1)"], ["Voltage gain", "high", "high", "low (&lt; 1)"], ["Power gain", "medium", "high", "medium"],
      ["Input impedance", "low", "medium", "high"], ["Output impedance", "high", "medium", "low"], ["Phase shift", "none", "180°", "none"], ["Main use", "high-frequency (RF amplifiers)", "general amplification (audio)", "impedance matching / buffer (voltage follower)"]])
 + E("I<sub>B</sub> = 40 µA, β = 100: I<sub>C</sub> = βI<sub>B</sub> = <code>4 mA</code>, I<sub>E</sub> = 4.04 mA, α = 100/101 = <code>0.990</code>. As a switch: I<sub>B</sub> = 0 → cut-off (OFF); enough I<sub>B</sub> to reach the left edge of the curves → saturation (ON, V<sub>CE(sat)</sub> ≈ 0.2 V)."))

p5 = sec("p5", "P5. MOSFET", "Voltage-controlled transistor with an insulated gate; enhancement vs depletion, regions of operation, BJT vs MOSFET.",
 [("MOSFET", "metal-oxide-semiconductor field-effect transistor; also called IGFET."), ("Source / Gate / Drain / Substrate", "the terminals and the body (joined to source internally)."), ("Enhancement mode", "channel absent at V<sub>GS</sub> = 0; gate voltage creates it."),
  ("Depletion mode", "channel present at V<sub>GS</sub> = 0 (ON by default); gate voltage depletes it."), ("Threshold voltage V<sub>T</sub>", "gate voltage at which the channel forms."), ("Ohmic / saturation / cut-off", "regions of the I<sub>D</sub>–V<sub>DS</sub> characteristic."), ("Transconductance g<sub>m</sub>", "ΔI<sub>D</sub>/ΔV<sub>GS</sub>.")],
 P("The metal gate is insulated from the semiconductor by a SiO₂ layer, so the input impedance is extremely high and the device is <em>voltage-controlled</em> (V<sub>GS</sub> controls I<sub>D</sub>), unlike the current-controlled BJT. <b>N-channel enhancement:</b> source and drain are heavily doped N on a P substrate; majority carriers are electrons; source and drain are physically separate until the gate voltage forms a channel. <b>P-channel:</b> the opposite doping, majority carriers holes. In <b>depletion</b> types a thin strip of channel material already joins source and drain.")
 + A.d_mosfet() + A.d_mosfet_curves()
 + UL(["<b>Cut-off:</b> no current; MOSFET is OFF.", "<b>Ohmic region:</b> drain current rises with V<sub>DS</sub>.", "<b>Saturation:</b> drain current constant for further V<sub>DS</sub> (beyond pinch-off, V<sub>DS</sub> ≥ V<sub>GS</sub> − V<sub>T</sub>).",
       "<b>Depletion mode:</b> ON by default; negative gate voltage = depletion, positive = enhancement.", "<b>Enhancement mode:</b> positive gate voltage makes it conduct."])
 + T(["Feature", "BJT", "MOSFET"],
     [["Control", "base current I<sub>B</sub> controls I<sub>C</sub>", "gate voltage V<sub>GS</sub> controls I<sub>D</sub>"], ["Input impedance", "low", "very high"], ["Switching speed", "moderate", "high"], ["Control power", "continuous base current", "very low (charges gate capacitance only)"],
      ["Thermal stability", "less stable", "better"], ["Gain", "current gain β (20–200)", "transconductance g<sub>m</sub>"], ["On-state", "V<sub>CE(sat)</sub> ≈ 0.2–1 V", "R<sub>DS(on)</sub> very small (mΩ in power MOSFETs)"], ["Best for", "low-frequency analog, audio", "high-speed switching, power electronics, digital logic, motor drivers"]])
 + E("Enhancement MOSFET with k = 0.5 mA/V², V<sub>T</sub> = 2 V, V<sub>GS</sub> = 4 V in saturation: I<sub>D</sub> = k(V<sub>GS</sub> − V<sub>T</sub>)² = 0.5 × 2² = <code>2 mA</code>.")
 + M("<b>Heads-up on a slide detail:</b> your slide says the ohmic region is used as an amplifier and saturation as a switch. Most textbooks state it the other way round — saturation for <em>amplification</em>, and cut-off (OFF) with the ohmic region (ON, small R<sub>DS(on)</sub>) for <em>switching</em>. Follow your lecturer's wording in the exam, but know the standard picture.", "Check with your lecturer"))

p6 = sec("p6", "P6. Rectifiers", "Half-wave, centre-tap full-wave and bridge rectifiers; I<sub>dc</sub>, I<sub>rms</sub>, efficiency, ripple and PIV.",
 [("Rectification", "obtaining unidirectional current/voltage from alternating."), ("Half-wave / full-wave", "conducts on one / both half-cycles."), ("Centre tap", "midpoint connection of the transformer secondary."), ("PIV", "peak inverse voltage a diode must withstand."),
  ("Ripple", "AC component left on the DC output; ripple factor γ = I<sub>ac,rms</sub>/I<sub>dc</sub>."), ("Rectification efficiency η", "DC output power ÷ AC input power.")],
 P("A diode lets current flow in one direction only, so a load in series with it conducts on alternate half-cycles — the load current (and voltage) is unidirectional, i.e. 'direct' but pulsating.")
 + A.d_halfwave()
 + FM("<b>Half-wave:</b> I<sub>dc</sub> = I<sub>m</sub>/π = 0.318 I<sub>m</sub> &nbsp;;&nbsp; I<sub>rms</sub> = I<sub>m</sub>/2 = 0.5 I<sub>m</sub> &nbsp;;&nbsp; η<sub>max</sub> = 0.405 (40.5%)")
 + A.d_fullwave_ct()
 + P("<b>Centre-tap full-wave:</b> C is the centre tap of the secondary; when A is positive w.r.t. C, D₁ conducts and D₂ is off; when the polarities reverse D₂ conducts and D₁ is off. Each diode conducts on alternate half-cycles, passing current through the load in the <em>same</em> direction.")
 + FM("<b>Full-wave:</b> I<sub>dc</sub> = 2I<sub>m</sub>/π = 0.637 I<sub>m</sub> &nbsp;;&nbsp; I<sub>rms</sub> = I<sub>m</sub>/√2 = 0.707 I<sub>m</sub> &nbsp;;&nbsp; η = 8/π² = 0.81 (81%)")
 + A.d_bridge()
 + P("<b>Bridge:</b> the centre-tap circuit uses each half of the secondary only half the time. In the bridge, when A is positive D₁ and D₃ (slide labelling) conduct, when B is positive D₂ and D₄ conduct; the load current direction is the same and the same full-wave expressions apply. No centre tap is needed.")
 + T(["", "Half-wave", "Centre-tap FW", "Bridge"], [["Diodes", "1", "2", "4"], ["Ripple frequency", "f", "2f", "2f"], ["Efficiency", "40.5%", "81%", "81%"], ["PIV per diode", "V<sub>m</sub>", "2V<sub>m</sub>", "V<sub>m</sub>"], ["Transformer", "plain", "centre-tapped", "plain"], ["Ripple factor", "1.21", "0.48", "0.48"]])
 + E("Secondary 12 V rms into R<sub>L</sub> = 100 Ω (ideal diodes): V<sub>m</sub> = 12√2 = 16.97 V.<br>Half-wave: V<sub>dc</sub> = V<sub>m</sub>/π = <code>5.40 V</code>, I<sub>dc</sub> = 54 mA. Full-wave: V<sub>dc</sub> = 2V<sub>m</sub>/π = <code>10.8 V</code>, I<sub>dc</sub> = 108 mA.<br>"
     "With a filter capacitor C = 1000 µF on the full-wave output: ripple ≈ I<sub>dc</sub>/(2fC) = 0.108/(100×0.001) ≈ <code>1.08 V</code> peak-to-peak (lab: 'full-wave rectifier with and without capacitor filter'). A real bridge loses about 1.4 V in two silicon diodes."))

p7 = sec("p7", "P7. Operational Amplifiers", "Ideal op-amp properties, virtual earth, inverting, non-inverting and summing amplifiers.",
 [("Op-amp", "high-gain DC-coupled differential amplifier IC."), ("Inverting / non-inverting input", "the − / + terminals; output is out of / in phase with the signal on them."), ("Open-loop gain", "gain without feedback; typically 10⁵."), ("Negative feedback", "feeding a fraction of the output back to the − input to stabilise gain."),
  ("Virtual earth (virtual short)", "with feedback, v<sub>+</sub> ≈ v<sub>−</sub>; so for the inverting amp the − input sits at ≈ 0 V."), ("Closed-loop gain A<sub>v</sub>", "gain with feedback; set by resistors."), ("Saturation", "output clipped near the supply rails.")],
 P("Properties of the common IC op-amp: an <b>inverting</b> and a <b>non-inverting</b> input; very <b>high input impedance</b> (assumed infinite) at both; <b>low output impedance</b>; very large voltage gain without feedback (typically 10⁵) that is constant over a wide frequency range; little drift (output zero when input is zero); good stability. Uses go beyond linear amplification into digital logic systems.")
 + A.d_opamp_inv()
 + W("Input current is zero and the − input is held at ≈ 0 V, so the current through R₁ is v<sub>i</sub>/R₁; all of it must flow through R<sub>f</sub>, so v<sub>o</sub> = −R<sub>f</sub>(v<sub>i</sub>/R₁). Hence <b>A<sub>v</sub> = −R<sub>f</sub>/R₁</b>.", "Derivation — inverting amplifier")
 + A.d_opamp_noninv() + FM("Non-inverting: v<sub>−</sub> = v<sub>i</sub> (virtual short) &nbsp;⟹&nbsp; v<sub>i</sub> = v<sub>o</sub> R₁/(R₁+R<sub>f</sub>) &nbsp;⟹&nbsp; A<sub>v</sub> = 1 + R<sub>f</sub>/R₁")
 + A.d_opamp_sum()
 + E("<b>Inverting:</b> R₁ = 10 kΩ, R<sub>f</sub> = 100 kΩ, v<sub>i</sub> = 0.2 V → A<sub>v</sub> = −10, v<sub>o</sub> = <code>−2 V</code>.<br><b>Non-inverting:</b> R<sub>f</sub> = 90 kΩ, R₁ = 10 kΩ → A<sub>v</sub> = 10; v<sub>i</sub> = 0.5 V → <code>5 V</code>. A voltage follower is R<sub>f</sub> = 0, R₁ = ∞ → gain 1.<br>"
     "<b>Summing:</b> R<sub>A</sub> = R<sub>B</sub> = R<sub>C</sub> = R<sub>f</sub>, inputs 1 V, 2 V, 3 V → v<sub>o</sub> = −(1+2+3) = <code>−6 V</code>.<br>With ±12 V supplies, a gain of 10 and a 2 V input would try to give 20 V, so the output <em>saturates</em> near ±11 V."))

p8 = sec("p8", "P8. Electromagnetic Spectrum", "The full range of EM radiation from radio to gamma; c = fλ and E = hf.",
 [("EM wave", "oscillating E and B fields perpendicular to each other and to the direction of travel; needs no medium."), ("Wavelength λ", "distance of one wave cycle."), ("Frequency f", "cycles per second (Hz)."), ("c", "speed of light, 3×10⁸ m/s in vacuum."), ("Photon energy", "E = hf, proportional to frequency."), ("Band", "range of the spectrum with similar behaviour/use.")],
 A.d_em_spectrum()
 + UL(["<b>Radio waves:</b> longest wavelength, lowest frequency; broadcasting and communication.", "<b>Microwaves:</b> ovens, radar, satellite.", "<b>Infrared:</b> felt as heat; thermal imaging, remote controls.", "<b>Visible light:</b> the narrow band the eye sees, red to violet.",
       "<b>Ultraviolet:</b> shorter wavelength, higher energy than visible; can cause sunburn.", "<b>X-rays:</b> pass through soft tissue; medical imaging.", "<b>Gamma rays:</b> shortest wavelength, highest frequency; radioactive sources."])
 + FM("c = f λ &nbsp;&nbsp;;&nbsp;&nbsp; E = h f &nbsp;&nbsp; (h = 6.63×10⁻³⁴ J·s) &nbsp;&nbsp;; wavelength and frequency are inversely related")
 + E("FM radio at 100 MHz: λ = 3×10⁸/10⁸ = <code>3 m</code>. Wi-Fi at 2.4 GHz: λ = <code>12.5 cm</code>. Green light at 550 nm: f = 3×10⁸/550×10⁻⁹ = <code>5.5×10¹⁴ Hz</code>, photon energy 6.63×10⁻³⁴ × 5.5×10¹⁴ = 3.6×10⁻¹⁹ J (2.3 eV)."))

p9 = sec("p9", "P9. Elements of a Communication System", "Source, transducers, transmitter, channel, noise, receiver, destination; why modulation is needed.",
 [("Source", "origin of the information."), ("Transducer", "converts between a physical quantity and an electrical signal (microphone ↔ speaker)."), ("Transmitter", "converts the information into a signal suited to the channel (modulates, amplifies)."), ("Channel", "the wired or wireless medium."),
  ("Noise", "unwanted signals that distort the message."), ("Receiver", "reverses the transmitter's process."), ("Destination", "final recipient."), ("Modulation", "impressing the message on a high-frequency carrier."), ("SNR", "signal-to-noise ratio, in dB = 10 log₁₀(P<sub>s</sub>/P<sub>n</sub>).")],
 A.d_comm_block()
 + UL(["<b>Source:</b> origin of the information.", "<b>Input transducer:</b> converts the source's information into an electrical signal (e.g. a microphone for voice).", "<b>Transmitter:</b> converts the information into a signal suitable for transmission.",
       "<b>Channel:</b> medium (wired or wireless) the signal travels through; <b>noise</b> enters here and can distort the message.", "<b>Receiver:</b> reverses the transmitter's process, recovering a form the destination understands.", "<b>Output transducer:</b> electrical signal back to a perceivable form (a speaker).", "<b>Feedback:</b> signal from receiver to source indicating success of the communication."])
 + W("An antenna needs a length of about λ/4. A 3 kHz audio tone has λ = c/f = 3×10⁸/3000 = 100 km (λ/4 = 25 km!) — impractical. Modulating a 1 MHz carrier (λ = 300 m, λ/4 = 75 m) is far more practical; modulation also allows many stations to share the air (different carriers) and improves noise immunity.", "Why modulate?")
 + E("Signal power 2 mW, noise power 0.02 mW: SNR = 100 = 10 log₁₀100 = <code>20 dB</code>.")
 + P("<b>Types of modulation:</b> amplitude (AM), frequency (FM), phase (PM) for analog messages; digital schemes for data. <b>Duplex modes:</b> simplex (one way), half-duplex (both ways, one at a time), full-duplex (both at once)."))

p10 = sec("p10", "P10. Overview of Cellular Communication", "Cells, base stations, frequency reuse, handoff and the generations of mobile networks.",
 [("Cell", "the small coverage area served by one base station."), ("Base station", "transmitter/receiver (tower) serving a cell."), ("MSC", "mobile switching centre connecting cells and the public network."), ("Frequency reuse", "using the same frequencies in cells that are far apart."),
  ("Cluster (N)", "group of cells that together use all the available channels once."), ("Handoff", "passing an ongoing call from one cell to the next as the user moves."), ("Roaming", "using the network away from one's home network.")],
 M("This topic is in the syllabus ('overview of cellular communication') but was not in the slides you shared, so it is written from the standard textbook treatment — check it against your lecturer's slides.", "Source note")
 + A.d_cellular()
 + P("The service area is divided into <b>cells</b>, each with its own low-power base station. Low power lets the same frequencies be <b>reused</b> in distant cells, so a limited spectrum serves very many users. When a mobile moves out of a cell, a <b>handoff</b> passes the call to the next base station without interruption; the <b>MSC</b> coordinates this and links to the telephone network.")
 + FM("co-channel reuse distance: D / R = √(3N) &nbsp;&nbsp; (R = cell radius, N = cluster size)")
 + E("N = 7: D/R = √21 = <code>4.58</code>, so co-channel cells are about 4.6 cell radii apart. Smaller N gives more capacity per cell but more interference.")
 + T(["Generation", "Technology (typical)", "Main step forward"], [["1G", "analog (AMPS)", "mobile voice"], ["2G", "digital (GSM, CDMA)", "better voice quality, SMS"], ["3G", "UMTS / WCDMA", "mobile data, internet"], ["4G", "LTE (all-IP)", "broadband speeds, video"], ["5G", "NR: sub-6 GHz and mm-wave", "very high speed, low latency, many devices"]]))

p11 = sec("p11", "P11. Fundamentals of Satellite Communication", "Uplink/downlink, transponder, orbits (LEO, MEO, GEO) and delay.",
 [("Satellite", "an orbiting repeater that relays signals between ground stations."), ("Uplink / downlink", "ground-to-satellite / satellite-to-ground links."), ("Transponder", "receiver-transmitter combination on the satellite that receives, amplifies, shifts frequency and retransmits."),
  ("TWT amplifier", "travelling-wave-tube power amplifier."), ("LEO / MEO / GEO", "low (≈160–2000 km), medium and geostationary (≈35 786 km) Earth orbit."), ("Ground control station", "monitors and maintains the satellite's position and health.")],
 P("<b>Principle:</b> a ground station transmits (uplink) to the satellite, which, acting as a repeater, receives, amplifies and retransmits the signal back to Earth (downlink). <b>Components:</b> transmitting earth station; satellite with transponders; receiving earth station; ground control station.")
 + A.d_satellite() + A.d_transponder()
 + P("Uplink frequencies are higher than downlink frequencies to prevent interference (C-band: 5.9–6.4 GHz up, 3.7–4.2 GHz down). In the transponder: 6 GHz − 2.2 GHz local oscillator ≈ 3.8 GHz, inside the downlink band.")
 + T(["Orbit", "Altitude", "Notes"], [["LEO", "≈ 160–2000 km", "short delay; needs many satellites (e.g. internet constellations)"], ["MEO", "≈ 2000–35 786 km", "navigation (GPS ≈ 20 200 km)"], ["GEO", "35 786 km", "period 24 h → appears fixed; ≈ 3 satellites cover the globe; TV broadcast, weather"]])
 + E("Geostationary delay: ground → satellite → ground = 2 × 35 786 km = 71 572 km; at 3×10⁵ km/s that is <code>≈ 0.24 s</code> one way (a 'hello' and its reply take about half a second)."))

p12 = sec("p12", "P12. Fundamentals of Radar", "Radio detection and ranging: range from echo time, Doppler for speed.",
 [("Radar", "Radio Detection And Ranging."), ("Echo", "reflected portion of the transmitted wave."), ("Duplexer", "switch letting one antenna transmit and receive."), ("Doppler effect", "frequency shift of the echo due to target motion; gives velocity."), ("PRF / PRI", "pulse repetition frequency / interval."), ("Unambiguous range", "c·PRI/2 — longest range without confusing echoes.")],
 P("A radar <em>transmits electromagnetic energy and receives the echo</em> reflected off an object. <b>Transmission:</b> a transmitter sends high-power pulses (or continuous waves). <b>Reflection:</b> part of the signal returns. <b>Reception:</b> a sensitive receiver, often sharing the antenna through a duplexer, picks up the weak echo. <b>Processing:</b> a computer extracts the object's characteristics.")
 + A.d_radar()
 + FM("range R = c t / 2 &nbsp;&nbsp;; &nbsp; direction = antenna orientation at echo &nbsp;&nbsp;; &nbsp; Doppler f<sub>d</sub> = 2 v f₀ / c")
 + E("Echo returns after t = 200 µs: R = 3×10⁸ × 200×10⁻⁶ / 2 = <code>30 km</code>. A 10 GHz radar sees a target closing at 30 m/s: f<sub>d</sub> = 2×30×10¹⁰/3×10⁸ = <code>2000 Hz</code>.")
 + P("<b>Applications:</b> air-traffic control, weather, speed guns, ships, wind sensing, automotive collision avoidance."))

SECTIONS = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
CHECKLIST = ["Explain the depletion layer and the barrier potential, and sketch the diode V–I curve for forward and reverse bias.", "Apply the diode equation and the Si/Ge differences (knee voltage, temperature behaviour).",
             "Explain why a Zener is used reverse-biased and design the series resistor of a Zener regulator.", "Define α and β, state α = β/(1+β), and compare CB, CE and CC.",
             "Contrast BJT and MOSFET; describe enhancement vs depletion and the three regions of operation.", "Derive I<sub>dc</sub>, I<sub>rms</sub> and efficiency for half-wave and full-wave rectifiers; compare bridge and centre-tap.",
             "Derive the gain of the inverting and non-inverting op-amp and solve a summing-amplifier problem.", "Use c = fλ for the EM spectrum and name the bands in order.", "Draw and label a communication block diagram and explain why modulation is needed.",
             "Explain frequency reuse and handoff in a cellular network.", "Describe the satellite uplink/downlink and transponder, and compare LEO/MEO/GEO.", "Find the range and Doppler shift in a radar problem."]
