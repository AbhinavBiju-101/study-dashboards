"""Structure of the notes: modules -> topics -> subtopics.
Topic order follows the syllabus screenshot (Modules 2, 3, 4). Summaries are written for these notes.
Every subtopic id is an anchor that must exist on its module page (checked by scripts/verify.py)."""

MODULES = [
 dict(n=1, key="m1", title="Wave Particle Duality", short="Wave-particle duality", hours=8, color="#4d7c0f",
  scope="Covered fully against the syllabus line. The photoelectric effect, Davisson-Germer experiment and uncertainty principle are not in the syllabus line but are in your decks, so they are included and marked as extra.",
  syllabus="Dual nature of radiation – Young's double slit experiment – Blackbody radiation – Planck's hypothesis – de Broglie hypothesis – Wavefunction – Stern-Gerlach experiment.",
  topics=[
   dict(id="m1-1", title="Dual nature of radiation and Young's double slit", summary="Light shows interference (wave) yet comes in quanta (particle); Young's experiment is the wave evidence.", subs=[
     ("m1-1-1","Dual nature of radiation and matter","Wave and particle descriptions, linked by E = hν and λ = h/p."),
     ("m1-1-2","Wave characteristics and the travelling wave","λ, k, f, T, v = fλ and y = A cos(ωt − kx)."),
     ("m1-1-3","Superposition and interference","Waves add; in phase doubles the amplitude, in antiphase cancels."),
     ("m1-1-4","Young's double-slit experiment","Fringes at y = nλD/d; fringe width β = λD/d."),
   ]),
   dict(id="m1-2", title="Blackbody radiation", summary="The glow of a hot body, its laws, and the failure of classical theory.", subs=[
     ("m1-2-1","Thermal radiation, the blackbody and Kirchhoff's law","An ideal absorber is an ideal emitter."),
     ("m1-2-2","Features of the spectrum: Stefan's and Wien's laws","R = σT⁴ and λ_max T = 2.898×10⁻³ m·K."),
     ("m1-2-3","Rayleigh-Jeans law and the ultraviolet catastrophe","The classical curve diverges at short wavelength."),
   ]),
   dict(id="m1-3", title="Planck's hypothesis", summary="Oscillator energies come in steps of hν; this gives the radiation law that fits the data.", subs=[
     ("m1-3-1","Quantisation of oscillator energy","Eₙ = nhν, quanta E = hν."),
     ("m1-3-2","Planck's radiation law and its limits","Reduces to Rayleigh-Jeans at low ν and vanishes at high ν."),
   ]),
   dict(id="m1-4", title="The photoelectric effect (extra: in your decks, not in the syllabus line)", summary="Evidence for photons; Einstein's equation hf = W₀ + KE_max.", subs=[
     ("m1-4-1","Observations and the laws of photoelectric emission","Threshold frequency, stopping potential, instantaneous emission."),
     ("m1-4-2","Einstein's photoelectric equation","Photon energy splits into work function and kinetic energy."),
   ]),
   dict(id="m1-5", title="The de Broglie hypothesis and matter waves", summary="Particles have wavelength λ = h/p; wave packets, phase and group velocity.", subs=[
     ("m1-5-1","De Broglie wavelength","Forms for kinetic energy, accelerating voltage and temperature."),
     ("m1-5-2","Properties of matter waves","Not electromagnetic, independent of charge, probability waves."),
     ("m1-5-3","Wave packets, phase velocity and group velocity","v_g = v and v_p = c²/v for de Broglie waves."),
     ("m1-5-4","The Davisson-Germer experiment (extra)","Electrons diffract from a crystal."),
   ]),
   dict(id="m1-6", title="The Heisenberg uncertainty principle (extra: in your decks, not in the syllabus line)", summary="Position and momentum cannot both be sharp: Δx Δp ≥ ħ/2.", subs=[
     ("m1-6-1","Statement of the principle","Δx Δp ≥ h/4π and ΔE Δt ≥ h/4π."),
     ("m1-6-2","The microscope thought experiment","Short-wavelength photon: good position, big kick."),
     ("m1-6-3","Energy-time uncertainty and applications","Zero-point energy, line width and others."),
   ]),
   dict(id="m1-7", title="The wavefunction", summary="The state of a particle, its probability density, acceptable forms and the operators acting on it.", subs=[
     ("m1-7-1","Meaning of the wavefunction and probability density","|Ψ|² is the probability density."),
     ("m1-7-2","Acceptable wavefunctions and normalisation","Single-valued, finite, continuous; ∫|Ψ|²dV = 1."),
     ("m1-7-3","Operators, eigenfunctions and eigenvalues","p̂ = −iħ ∂/∂x and the eigenvalue equation."),
   ]),
   dict(id="m1-8", title="The Stern-Gerlach experiment", summary="Listed in the Module 1 syllabus; written up in full in Module 3.", subs=[
     ("m1-8-1","Where the Stern-Gerlach experiment is covered","Pointer to Module 3, Section 4."),
   ]),
 ]),

 dict(n=2, key="m2", title="Mathematical Foundations of Quantum Mechanics", short="Maths foundations", hours=10, color="#0f766e",
  scope="Covered fully.",
  syllabus="Introduction to linear vector space – Basis vectors – Orthonormal sets – Hilbert space – Representation of quantum states using Dirac notation – Inner and outer products – Tensor product of vector spaces – Linear operators – Matrix algebra – Hermitian, Unitary and Projection operators – Eigenvalues and eigenvectors – Pauli matrices – Commutation relations.",
  topics=[
   dict(id="m2-1", title="Linear vector spaces", summary="The arena: sets of objects you can add and scale, and how to describe them with a basis.", subs=[
     ("m2-1-1","Vector spaces and scalars","What makes a set a vector space, and why quantum mechanics needs complex scalars."),
     ("m2-1-2","Linear combinations and span","Building vectors from others; the span is everything reachable."),
     ("m2-1-3","Linear independence","No vector in the set is redundant; how to test it with a determinant or pivots."),
     ("m2-1-4","Basis vectors and dimension","A minimal complete set of vectors; coordinates depend on the basis chosen."),
     ("m2-1-5","Subspaces, column space and null space","Smaller spaces living inside a space; rank plus nullity equals the number of columns."),
   ]),
   dict(id="m2-2", title="Orthonormal sets and Hilbert space", summary="Perpendicular unit-length bases make coordinates easy; a Hilbert space adds the inner product.", subs=[
     ("m2-2-1","Orthogonality, normalisation and orthonormal sets","Unit vectors that are mutually perpendicular; coefficients come from inner products."),
     ("m2-2-2","Hilbert space","A complete complex vector space with an inner product; where quantum states live."),
   ]),
   dict(id="m2-3", title="Dirac notation, inner, outer and tensor products", summary="Bras, kets and the three ways of multiplying them.", subs=[
     ("m2-3-1","Kets and bras","A ket is a column vector, its bra is the conjugate transpose."),
     ("m2-3-2","Inner product","⟨a|b⟩ gives a complex number: norm, orthogonality, Schwarz inequality."),
     ("m2-3-3","Outer product","|a⟩⟨b| gives a matrix (an operator), the reverse order of the inner product."),
     ("m2-3-4","Tensor product of vector spaces","How two spaces combine into one of dimension n×m."),
   ]),
   dict(id="m2-4", title="Linear operators and matrix algebra", summary="Operators act on kets; in a chosen basis they are matrices. Hermitian, unitary and projection operators are the three special classes.", subs=[
     ("m2-4-1","Linear operators","Rules that map kets to kets while respecting addition and scaling."),
     ("m2-4-2","Matrix algebra and matrix representation","Matrix elements ⟨i|A|j⟩, products, transpose, dagger, trace."),
     ("m2-4-3","Hermitian operators","A = A†: real eigenvalues, orthogonal eigenvectors, the observables."),
     ("m2-4-4","Unitary operators","U†U = I: preserve norms; time evolution and gates."),
     ("m2-4-5","Projection operators","P = P† = P²: pick out a component; the tool for measurement probabilities."),
   ]),
   dict(id="m2-5", title="Eigenvalues and eigenvectors", summary="The directions an operator leaves unchanged, and the factors it stretches them by.", subs=[
     ("m2-5-1","The eigenvalue equation and how to solve it","Characteristic equation, then substitute back to find the vectors."),
     ("m2-5-2","Eigenvalues of Hermitian and unitary operators, and expansion in an eigenbasis","Real versus unit-modulus eigenvalues; expanding a state in eigenvectors."),
   ]),
   dict(id="m2-6", title="Pauli matrices", summary="Three 2×2 matrices that describe spin-½ and act as qubit gates.", subs=[
     ("m2-6-1","The three Pauli matrices and their properties","σx, σy, σz: Hermitian, unitary, traceless, eigenvalues ±1."),
     ("m2-6-2","Pauli eigenstates and products","Eigenvectors of each matrix and the multiplication rules."),
   ]),
   dict(id="m2-7", title="Commutation relations", summary="Whether the order of two operators matters, and what that means physically.", subs=[
     ("m2-7-1","Commutators, anticommutators and identities","[A,B] = AB − BA, and the rules for manipulating it."),
     ("m2-7-2","Key commutators and their physical meaning","[x,p] = iħ, angular momentum, Pauli; commuting means simultaneously measurable."),
   ]),
  ]),
 dict(n=3, key="m3", title="Postulates of Quantum Mechanics", short="Postulates", hours=8, color="#6d28d9",
  scope="Covered fully, including the time-dependent and time-independent Schrödinger equations.",
  syllabus="Observables – Expectation values – Measurement in Quantum Mechanics – Sequential Stern-Gerlach Experiment – Time-dependent and time-independent Schrödinger equations.",
  topics=[
   dict(id="m3-1", title="Observables and operators", summary="Every measurable quantity is a Hermitian operator; its eigenvalues are the possible results.", subs=[
     ("m3-1-1","What an observable is","Measurable property represented by a Hermitian operator, so results are real."),
     ("m3-1-2","The standard operators","Position, momentum, angular momentum, kinetic, potential and total energy operators."),
     ("m3-1-3","Where the momentum and energy operators come from","Differentiate a free-particle wave to read them off."),
     ("m3-1-4","The eigenvalue postulate and quantised results","Only eigenvalues are ever observed, so measured values can be discrete."),
   ]),
   dict(id="m3-2", title="Expectation values", summary="The probability-weighted average of many identical measurements.", subs=[
     ("m3-2-1","Meaning of an expectation value","An ensemble average, not necessarily a value you will see."),
     ("m3-2-2","Computing ⟨x⟩, ⟨p⟩ and ⟨E⟩","Sandwich the operator between ψ* and ψ and integrate."),
     ("m3-2-3","Shortcuts for real wavefunctions and ⟨p²⟩","⟨p⟩ = 0 for real ψ; ⟨p²⟩ = ħ²∫|ψ′|²dx."),
     ("m3-2-4","Uncertainty from expectation values","Δx and Δp from ⟨x²⟩ − ⟨x⟩² and checking the uncertainty principle."),
   ]),
   dict(id="m3-3", title="Measurement in quantum mechanics", summary="Outcomes are eigenvalues, probabilities come from projections, and the state collapses.", subs=[
     ("m3-3-1","Possible outcomes and definite states","Eigenvalues are outcomes; eigenvectors are states with a certain outcome."),
     ("m3-3-2","Probabilities from projection operators","Prob = ‖Pψ‖² = |⟨a|ψ⟩|² for a normalised state."),
     ("m3-3-3","Collapse and repeated measurement","After a measurement the state is the eigenvector found; repeating gives the same result."),
   ]),
   dict(id="m3-4", title="Sequential Stern-Gerlach experiment", summary="Chains of spin analysers reveal superposition, incompatibility and interference.", subs=[
     ("m3-4-1","The Stern-Gerlach apparatus and spin-½","A beam splits into two; kets label the beams."),
     ("m3-4-2","Experiment 1: z then z","A repeated identical measurement agrees with itself."),
     ("m3-4-3","Experiment 2: z then x","A 50/50 split: the state |+⟩ is a superposition of x-states."),
     ("m3-4-4","Experiment 3: z, x, then z","The x measurement erases the earlier z result: incompatible observables."),
     ("m3-4-5","Experiment 4: recombined beams","Adding amplitudes (not probabilities) restores the z result."),
     ("m3-4-6","Summary and the maths behind all four","Amplitude calculations that reproduce every count."),
   ]),
   dict(id="m3-5", title="Time-dependent and time-independent Schrödinger equations", summary="The wave equation of matter: how it is built from de Broglie's idea, and its two forms.", subs=[
     ("m3-5-1","Why a wave equation, and its assumptions","Classical mechanics fails for atoms, so Schrödinger gives matter a wave function Ψ."),
     ("m3-5-2","From the classical wave equation to a plane-wave starting point","Start from ∇²Ψ = (1/v²)∂²Ψ/∂t² with Ψ = Ψ₀e^{−iωt}."),
     ("m3-5-3","The time-independent equation","Put in λ = h/mv and E = V + ½mv² to get ∇²ψ + (2m/ħ²)(E − V)ψ = 0, i.e. Ĥψ = Eψ."),
     ("m3-5-4","The time-dependent equation","Eliminate E using E = ħω to get iħ ∂Ψ/∂t = ĤΨ."),
     ("m3-5-5","Hamiltonian, stationary states and how the two forms connect","Ψ = ψ(x)e^{−iEt/ħ}: the time factor only changes the phase."),
   ]),
  ]),
 dict(n=4, key="m4", title="Applications of Quantum Mechanics", short="1D box", hours=7, color="#b45309",
  scope="Covered fully: the 1D box, its 3D extension, degeneracy, and quantum tunnelling.",
  syllabus="Particle in a one-dimensional potential well – Extension to three-dimensional potential wells – Energy eigenvalues and eigenfunctions – Degeneracy of energy levels – Quantum tunneling phenomenon – Tunneling probability",
  topics=[
   dict(id="m4-1", title="The particle in a 1D box", summary="An infinite square well: the simplest system that shows quantisation.", subs=[
     ("m4-1-1","The setup: classical versus quantum","V = 0 inside, V = ∞ outside; what changes when the particle is a wave."),
     ("m4-1-2","The equation inside the box","ψ″ = −k²ψ with k² = 2mE/ħ², whose solutions are sines and cosines."),
     ("m4-1-3","Boundary conditions and the wavefunction","ψ(0) = ψ(L) = 0 forces B = 0 and kL = nπ."),
     ("m4-1-4","Energy eigenvalues","Eₙ = n²h²/(8mL²): quantised and growing as n²."),
     ("m4-1-5","Normalisation and the eigenfunctions","A = √(2/L), so ψₙ = √(2/L) sin(nπx/L)."),
   ]),
   dict(id="m4-2", title="What the solution tells us", summary="Reading physics from Eₙ and ψₙ.", subs=[
     ("m4-2-1","Quantisation, spacing and the quantum number","Levels are discrete and not equally spaced."),
     ("m4-2-2","Zero-point energy","n = 0 is impossible; confinement forces a minimum energy."),
     ("m4-2-3","Nodes, antinodes and probability density","|ψₙ|² has n − 1 interior nodes; probability is not uniform."),
     ("m4-2-4","Probability in a region and the correspondence principle","Integrate |ψ|² over an interval; large n looks classical."),
     ("m4-2-5","The standing-wave (de Broglie) picture","L = nλ/2 gives the same energies."),
   ]),
   dict(id="m4-3", title="Extension to two and three dimensions", summary="Separate the variables: the wavefunction is a product and the energies add.", subs=[
     ("m4-3-1","Separation of variables in a box","ψ = X(x)Y(y)Z(z) and E = Eₓ + E_y + E_z."),
     ("m4-3-2","Energy eigenvalues and eigenfunctions in 3D","Three quantum numbers, product of sines."),
     ("m4-3-3","Normalisation and probability in a 3D box","C = (2/L)^{3/2}; the probability in a slab is a product of three 1D integrals."),
   ]),
   dict(id="m4-4", title="Degeneracy of energy levels", summary="Different states sharing one energy, and why a symmetric box has so many.", subs=[
     ("m4-4-1","What degeneracy means","Several wavefunctions with one eigenvalue; the number of them is the degree."),
     ("m4-4-2","Counting the levels of a cubical box","List (nₓ,n_y,n_z) with the same n² sum; permutations give the degree."),
     ("m4-4-3","Symmetry and breaking the degeneracy","Unequal sides split a degenerate level into separate ones."),
   ]),
   dict(id="m4-5", title="Quantum tunnelling and tunnelling probability", summary="A particle can get through a barrier that classical mechanics says it cannot cross.", subs=[
     ("m4-5-1","Classical versus quantum behaviour at a barrier","Classically E < V₀ means total reflection; quantum mechanically a small part gets through."),
     ("m4-5-2","The barrier problem: regions, wave numbers and solutions","Three regions, k₁ = k₃ outside and a different k inside."),
     ("m4-5-3","Reflection and transmission probabilities","R = B*B/A*A, T = F*F/A*A, and R + T = 1."),
     ("m4-5-4","The wavefunction inside the barrier (E < V₀)","Real exponentials Ce^{κx} + De^{−κx}: it decays but does not vanish."),
     ("m4-5-5","Tunnelling probability","T ≈ 16(E/V₀)(1 − E/V₀)e^{−2κL}, or roughly e^{−2κL}."),
     ("m4-5-6","Analogy with wave optics","Frustrated total internal reflection between two prisms."),
     ("m4-5-7","Scanning tunnelling microscope","Tunnelling current depends exponentially on tip-surface distance."),
     ("m4-5-8","Alpha-particle decay","An alpha particle tunnels out through the Coulomb barrier of the nucleus."),
     ("m4-5-9","Other tunnelling phenomena","Tunnel diode, field emission, electrical breakdown of insulators."),
   ]),
  ]),

 dict(n=5, key="m5", title="Elements of Quantum Computing", short="Quantum computing", hours=10, color="#0e7490",
  scope="Covered fully against the syllabus line. S and T gates, SWAP, controlled-Z and Toffoli are only briefly covered because your deck marks them as not in the syllabus.",
  syllabus="Introduction to qubits – Single qubit states and the Bloch Sphere – Two-qubit systems – Quantum entanglement and Bell states – Single-qubit gates: Pauli and Hadamard – Two-qubit gates: CNOT – Generation of entangled states.",
  topics=[
   dict(id="m5-1", title="Qubits: from the bit to the quantum bit", summary="What a qubit is, how it is written as a vector, and what superposition and measurement mean.", subs=[
     ("m5-1-1","Classical bit versus qubit","A bit is 0 or 1; a qubit is a normalised superposition and gives one outcome on measurement."),
     ("m5-1-2","The qubit as a vector in Hilbert space","|0⟩ and |1⟩ as the columns (1,0) and (0,1); a general state (α, β)."),
     ("m5-1-3","Superposition, amplitudes and measurement","P(0) = |α|², P(1) = |β|², and the state collapses on measurement."),
     ("m5-1-4","Entanglement: a first look","Qubits whose joint state cannot be split into separate states."),
   ]),
   dict(id="m5-2", title="The Bloch sphere", summary="Every single-qubit state is a point on a sphere with |0⟩ and |1⟩ at the poles.", subs=[
     ("m5-2-1","What the Bloch sphere is","Poles are |0⟩ and |1⟩; gates are rotations of the state vector."),
     ("m5-2-2","Coordinates, the state formula and special points","|ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩ and the Bloch vector."),
   ]),
   dict(id="m5-3", title="Two-qubit systems", summary="Two qubits live in a 4-dimensional space built with the tensor product.", subs=[
     ("m5-3-1","The tensor product and the computational basis","|00⟩, |01⟩, |10⟩, |11⟩ as 4-component columns; n qubits need 2ⁿ amplitudes."),
     ("m5-3-2","General two-qubit state and measurement probabilities","Four amplitudes, P(ij) = |αᵢⱼ|², and collapse of one qubit."),
     ("m5-3-3","Notation: shorthand, encoded form and the x basis","|01⟩ = |0⟩|1⟩ = |1⟩², and the |±⟩ product basis."),
   ]),
   dict(id="m5-4", title="Entanglement and Bell states", summary="Which two-qubit states are entangled, the four maximally entangled Bell states, and their uses.", subs=[
     ("m5-4-1","Product states versus entangled states","A product state has α₀₀α₁₁ = α₀₁α₁₀; failing this means entangled."),
     ("m5-4-2","The four Bell states","Φ± = (|00⟩ ± |11⟩)/√2, Ψ± = (|01⟩ ± |10⟩)/√2; an orthonormal basis."),
     ("m5-4-3","Correlations, applications and experiments","Teleportation, QKD, superdense coding, error correction; Bell-inequality tests."),
   ]),
   dict(id="m5-5", title="Single-qubit quantum gates", summary="Unitary, reversible operations on one qubit: X, Y, Z and H.", subs=[
     ("m5-5-1","What a quantum gate is: unitary and reversible","U†U = I preserves probability; contrast with irreversible AND."),
     ("m5-5-2","Pauli-X gate (the quantum NOT)","Swaps the amplitudes of |0⟩ and |1⟩."),
     ("m5-5-3","Pauli-Y gate","A flip with phases: Y|0⟩ = i|1⟩, Y|1⟩ = −i|0⟩."),
     ("m5-5-4","Pauli-Z gate (phase flip)","Leaves |0⟩, sends |1⟩ to −|1⟩."),
     ("m5-5-5","Hadamard gate","Turns basis states into equal superpositions; H² = I."),
     ("m5-5-6","Gates as rotations on the Bloch sphere","X, Y, Z are π rotations; H takes the pole to the equator."),
   ]),
   dict(id="m5-6", title="Two-qubit gates and generating entanglement", summary="CNOT, its matrix, and the H + CNOT circuit that makes a Bell state.", subs=[
     ("m5-6-1","The CNOT gate","Flips the target when the control is |1⟩."),
     ("m5-6-2","The CNOT matrix and a matrix calculation","4×4 permutation matrix; worked as CNOT|10⟩ = |11⟩."),
     ("m5-6-3","Creating entanglement: H then CNOT","|00⟩ → (|00⟩ + |11⟩)/√2, with all four Bell states from the four inputs."),
     ("m5-6-4","Other multi-qubit gates (for information)","SWAP, controlled-Z and Toffoli; not in your deck's syllabus."),
   ]),
 ]),
]
