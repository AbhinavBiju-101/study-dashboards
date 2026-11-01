# Physics MCQ Question Bank — Modules 2, 3 and 4

*Engineering Physics · Question Set 1*

**Scope:** Module 2 (vector spaces, Dirac notation, operators, Pauli matrices, commutators — full); Module 3 (observables, eigenvalues, expectation values, sequential Stern–Gerlach — Schrödinger equation excluded); Module 4 (particle in a 1D box — tunnelling and degeneracy excluded).

**Structure:** headers follow the topic order of your class slides and notes; every question is based on facts, formulas and worked examples stated in those materials. Each question has four options (A–D) and one correct answer, and Bloom's levels are mixed from Remember to Create.

**Question counts:** Module 2: 85; Module 3: 55; Module 4: 43; total: 183.

**Bloom's mix:** Remember 37, Understand 36, Apply 52, Analyze 29, Evaluate 26, Create 3.


## Contents


**Module 2 — Mathematical Foundations of Quantum Mechanics (Vector Spaces, Dirac Notation, Operators)**

* 2.1 Introduction to Linear Vector Spaces (6 questions)
* 2.2 Basis Vectors, Linear Independence and Span (6 questions)
* 2.3 Orthonormal Sets (6 questions)
* 2.4 Hilbert Space and Dirac Notation (6 questions)
* 2.5 Inner Product (7 questions)
* 2.6 Outer Product (6 questions)
* 2.7 Tensor Product of Vector Spaces (6 questions)
* 2.8 Linear Operators (6 questions)
* 2.9 Matrix Algebra (6 questions)
* 2.10 Hermitian Operators (6 questions)
* 2.11 Unitary and Projection Operators (6 questions)
* 2.12 Eigenvalues and Eigenvectors (6 questions)
* 2.13 Pauli Matrices (6 questions)
* 2.14 Commutation Relations (6 questions)

**Module 3 — Postulates of Quantum Mechanics and Sequential Stern–Gerlach Experiments**

* 3.1 Observables (5 questions)
* 3.2 Operators and Hermitian Operators (6 questions)
* 3.3 Eigenvalues and Eigenfunctions (6 questions)
* 3.4 Expectation Values (8 questions)
* 3.5 Sequential Stern–Gerlach: The Experiment and the Spin-½ Ket Description (7 questions)
* 3.6 Experiments 1 and 2: Repeated and Orthogonal Measurements (6 questions)
* 3.7 Experiment 3: Z–X–Z Successive Measurements (6 questions)
* 3.8 Experiment 4: One Beam versus Recombined Beams (6 questions)
* 3.9 Incompatible Observables and the Sock Analogy (5 questions)

**Module 4 — Particle in a One-Dimensional Box (Infinite Potential Well)**

* 4.1 The 1D Box: Potential and Physical Picture (5 questions)
* 4.2 Wavefunction and Boundary Conditions (5 questions)
* 4.3 Energy Eigenvalues (Quantisation) (5 questions)
* 4.4 Eigenfunctions and Normalisation (5 questions)
* 4.5 Zero-Point Energy and the Uncertainty Principle (5 questions)
* 4.6 Nodes, Antinodes and Probability Density (6 questions)
* 4.7 Inferences from the Box Solution (5 questions)
* 4.8 Numerical Problems on the 1D Box (7 questions)

---

## Module 2 — Mathematical Foundations of Quantum Mechanics (Vector Spaces, Dirac Notation, Operators)


### 2.1 Introduction to Linear Vector Spaces

*Sources: QM\_linear\_algebra §1.1–1.3; Module-2 Linear vector space slides*


**Q1 (Remember).** What does the closure condition require of a vector space?

* A. Every vector in the space must have unit norm
* B. The scalar product of any two vectors must be zero
* C. Adding any two vectors, or multiplying any vector by a scalar, gives another vector in the same space
* D. The space must contain no null element

**Answer: C**


**Q2 (Understand).** In the two-dimensional example, the same vector is written (2, 2) in the Cartesian basis and (2.4, 0.8) in a second basis. What does this show?

* A. The vector's magnitude changes when the basis changes
* B. The two bases describe two different vectors
* C. Only the Cartesian basis can describe a vector in a plane
* D. The components of a vector depend on the chosen basis, while the vector itself is unchanged

**Answer: D**


**Q3 (Apply).** For r₁ = 2i + 4j − 5k and r₂ = i + 2j + 3k, what is the unit vector parallel to r₁ + r₂?

* A. (3/7, 6/7, 2/7)
* B. (3/7, 6/7, −2/7)
* C. (3/√41, 6/√41, −2/√41)
* D. (2/7, 4/7, −5/7)

**Answer: B**


**Q4 (Analyze).** Which of the following is NOT a vector space according to the notes?

* A. The set of polynomials of degree n (exactly n)
* B. The space M\_mn of all m × n matrices
* C. The space P\_n of polynomials of degree at most n
* D. The space of all continuous functions

**Answer: A**


**Q5 (Evaluate).** A student says the cross product a × b can be used to multiply vectors in any vector space. Is this correct?

* A. No; the cross product can only be defined in three-dimensional vector spaces
* B. Yes; it is defined in every finite-dimensional space
* C. Yes; but only if the vectors are complex
* D. No; it is defined only in two-dimensional spaces

**Answer: A**


**Q6 (Understand).** Why is the scalar product a · b called basis-independent?

* A. It is always equal to zero in every basis
* B. It is always a vector along the first basis vector
* C. It is defined only for the Cartesian basis
* D. It is a single number whose value does not depend on the basis used to express the vectors

**Answer: D**


### 2.2 Basis Vectors, Linear Independence and Span

*Sources: Module-2 Linear vector space slides (Defs 3.1–3.15, worked examples); Numericals on LD/LID*


**Q1 (Remember).** How is a basis of Rᵐ defined?

* A. Any complete set of vectors, whether or not they are independent
* B. A set of vectors that add up to the null vector
* C. A set of linearly independent vectors that also form a complete set (span the space)
* D. Any two non-parallel vectors, in any space

**Answer: C**


**Q2 (Understand).** For a matrix B, which statement is equivalent to 'the columns of B are linearly independent'?

* A. The reduced row echelon form of B has a pivot in every row
* B. The system Bx = 0 has only the trivial solution x = 0
* C. The columns of B are mutually orthogonal
* D. The null space of B has dimension m

**Answer: B**


**Q3 (Apply).** For v₁ = (1,1,2), v₂ = (1,2,4), v₃ = (3,1,2) and v = (3,2,4), the solutions of Bx = v are x₁ = 4 − 5x₃ and x₂ = −1 + 2x₃. Which coefficients (x₁, x₂, x₃) result from choosing x₃ = 1?

* A. (−1, 1, 1)
* B. (4, −1, 1)
* C. (−1, 3, 1)
* D. (9, −3, 1)

**Answer: A**


**Q4 (Analyze).** For v₁ = (1,1,2), v₂ = (1,2,3), v₃ = (4,5,9), v₄ = (3,1,2), the row-reduced matrix has no pivot in the third column. What can be concluded?

* A. v₄ is a linear combination of v₁, v₂, v₃
* B. v₃ is a linear combination of the others, and v₁, v₂, v₄ are linearly independent
* C. All four vectors are independent because three columns have pivots
* D. Only v₁ and v₂ are independent

**Answer: B**


**Q5 (Evaluate).** A student claims f₁ = x² − x, f₂ = x² − 1, f₃ = x + 1 must be linearly dependent because they are three polynomials in P₂. Evaluate this claim.

* A. Correct; any three vectors in P₂ must be dependent because P₂ has dimension 2
* B. Correct; f₃ equals f₁ minus f₂
* C. Incorrect; comparing coefficients gives c₁ = c₂ = c₃ = 0, so they are linearly independent
* D. It cannot be decided without knowing the dimension of P₂

**Answer: C**


**Q6 (Apply).** Express f = 2x² + 4x − 5 as a combination of f₁ = x² − 1, f₂ = x − 1, f₃ = x.

* A. f = 2f₁ + 4f₂ − f₃
* B. f = 3f₁ + 2f₂ + f₃
* C. f = f₁ + 3f₂ + 2f₃
* D. f = 2f₁ + 3f₂ + f₃

**Answer: D**


### 2.3 Orthonormal Sets

*Sources: QM\_linear\_algebra §1.2.2, §2.2.1 (property 6), §2.8 Problems 2 and 5*


**Q1 (Remember).** What makes two vectors 'orthonormal'?

* A. They are parallel and each is a unit vector
* B. They are perpendicular but may have any length
* C. Their cross product is a unit vector
* D. They are perpendicular (orthogonal) and each is a unit vector

**Answer: D**


**Q2 (Understand).** What does the condition ⟨ψᵢ|ψⱼ⟩ = δᵢⱼ express for a basis set?

* A. All vectors in the set are identical
* B. All inner products are equal to 1
* C. Each vector is normalised (i = j gives 1) and different vectors are orthogonal (i ≠ j gives 0)
* D. The vectors are linearly dependent

**Answer: C**


**Q3 (Apply).** |Ψ⟩ = (1/√2, 1/√2) and |Φ⟩ = (1/√2, −1/√2). What is true of them?

* A. They are orthogonal, since ⟨Φ|Ψ⟩ = 1/2 − 1/2 = 0, and |Ψ⟩ is normalised
* B. They are orthogonal but |Ψ⟩ has norm 2
* C. They are not orthogonal because ⟨Φ|Ψ⟩ = 1
* D. They are parallel because their components have equal magnitude

**Answer: A**


**Q4 (Apply).** For |u⟩ = (x, 3x, −2x) with x real, which value of x makes |u⟩ normalised?

* A. x = ±1/√6
* B. x = ±1/√14
* C. x = ±1/14
* D. x = ±1/√10

**Answer: B**


**Q5 (Analyze).** Which 2D Hilbert-space vector is a physically valid state without further modification?

* A. (3, −2i)
* B. (i, −4)
* C. (1/√2)(1, −i)
* D. (2, 5)

**Answer: C**


**Q6 (Evaluate).** A student reports |⟨ψ|φ⟩|² = 1.4 for two normalised states. Evaluate this result.

* A. It is fine; probabilities may exceed 1 for complex vectors
* B. It is fine if the states are orthogonal
* C. It is impossible only if ⟨ψ|φ⟩ is real
* D. It is impossible, because 0 ≤ |⟨ψ|φ⟩|² ≤ 1 for normalised states

**Answer: D**


### 2.4 Hilbert Space and Dirac Notation

*Sources: QM\_linear\_algebra §2.1, §2.6–2.7; Module-2 Hilbert space and Dirac notation slides*


**Q1 (Remember).** What is a Hilbert space in quantum mechanics?

* A. A real vector space with no inner product
* B. A complete complex vector space equipped with an inner product, in which quantum states reside
* C. The set of all real-valued functions of position
* D. A space that contains only orthogonal vectors

**Answer: B**


**Q2 (Remember).** What is the bra corresponding to |Ψ⟩ = c₁|ψ₁⟩ + c₂|ψ₂⟩?

* A. ⟨Ψ| = c₁\*⟨ψ₁| + c₂\*⟨ψ₂|
* B. ⟨Ψ| = c₁⟨ψ₁| + c₂⟨ψ₂|
* C. ⟨Ψ| = c₁\*|ψ₁⟩ + c₂\*|ψ₂⟩
* D. ⟨Ψ| = c₂\*⟨ψ₁| + c₁\*⟨ψ₂|

**Answer: A**


**Q3 (Understand).** Why can c|Ψ⟩ (c a non-zero complex number) represent the same physical state as |Ψ⟩?

* A. Multiplying by c changes the state but not the energy
* B. Only real values of c are allowed
* C. The overall normalisation of a state vector does not change its information content
* D. Because |Ψ⟩ must always equal zero

**Answer: C**


**Q4 (Apply).** For the spin state |Ψ⟩ = (3, −2i) in the {|+⟩, |−⟩} basis, what is the bra ⟨Ψ|?

* A. (3, −2i)
* B. (3, 2i)
* C. (−3, 2i)
* D. (−2i, 3)

**Answer: B**


**Q5 (Analyze).** A particle in an infinite well has kets |1⟩, |2⟩, |3⟩, … forming a complete orthonormal set. What is the dimension of its state space?

* A. Infinite, because there is a ket |n⟩ for every n = 1, 2, 3, …
* B. 1
* C. 2
* D. 3, corresponding to |1⟩, |2⟩, |3⟩ only

**Answer: A**


**Q6 (Evaluate).** A student says c₁|ψ₁⟩ + c₂|ψ₂⟩ is not a valid state if c₁ and c₂ are complex. Evaluate this.

* A. Correct; coefficients must be real for a valid state
* B. Correct; only |ψ₁⟩ or |ψ₂⟩ alone can be states
* C. Incorrect, but only if c₁ = c₂
* D. Incorrect; any linear combination with complex coefficients is also an allowed state (superposition)

**Answer: D**


### 2.5 Inner Product

*Sources: QM\_linear\_algebra §2.2, §2.7–2.8 Problems 1 and 5; Dirac-notation slides*


**Q1 (Remember).** How is the inner product ⟨ψ|φ⟩ interpreted in quantum mechanics?

* A. As a probability itself, always between 0 and 1
* B. As the energy of the state |φ⟩
* C. As the commutator of |ψ⟩ and |φ⟩
* D. As a probability amplitude; its modulus squared gives a probability

**Answer: D**


**Q2 (Understand).** Why must a physically valid state be normalised so that ⟨ψ|ψ⟩ = 1?

* A. So that the state is orthogonal to itself
* B. So that the probabilistic interpretation of the state vector works
* C. So that its energy equals zero
* D. So that its components are all real

**Answer: B**


**Q3 (Apply).** For |A⟩ = (2, −7i, 1) and |B⟩ = (1+3i, 4, 8), what is ⟨A|B⟩?

* A. 10 + 34i
* B. 10 − 22i
* C. 10 − 34i
* D. 12 + 34i

**Answer: A**


**Q4 (Apply).** For |ψ⟩ = (1/√2)(1, −i) and |φ⟩ = (0, 1), what is the probability of finding |φ⟩ in the state |ψ⟩?

* A. 25%
* B. 100%
* C. 50%
* D. 0%

**Answer: C**


**Q5 (Analyze).** For |Ψ⟩ = 2i|a⟩ − 3|b⟩ + i|c⟩ and |Φ⟩ = 3|a⟩ − 2|b⟩ + 4|c⟩ in an orthonormal basis, what is ⟨Φ|Ψ⟩?

* A. 6 + 10i
* B. 6 − 10i
* C. −6 + 10i
* D. 6 + 2i

**Answer: A**


**Q6 (Evaluate).** Given ⟨Φ|Ψ⟩ = 6 + 10i, a student says ⟨Ψ|Φ⟩ must also equal 6 + 10i. Evaluate this.

* A. Correct; the inner product is symmetric
* B. Incorrect; it equals −6 − 10i
* C. Correct, because both states are normalised
* D. Incorrect; ⟨Ψ|Φ⟩ = ⟨Φ|Ψ⟩\*, so it equals 6 − 10i

**Answer: D**


**Q7 (Apply).** What is the squared norm ⟨A|A⟩ of |A⟩ = (2, −7i, 1)?

* A. 4
* B. 54
* C. 50
* D. √54

**Answer: B**


### 2.6 Outer Product

*Sources: QM\_linear\_algebra §2.3–2.4.3; Dirac-notation slides (ket-bra)*


**Q1 (Remember).** What is the (i, j) element of the outer product |ψ⟩⟨φ|?

* A. ψᵢ\* φⱼ
* B. ψᵢ φⱼ
* C. ψᵢ φⱼ\*
* D. ψⱼ φᵢ\*

**Answer: C**


**Q2 (Apply).** For |ψ⟩ = (2, 3) and |φ⟩ = (1, i), what is |ψ⟩⟨φ|?

* A. [[2, 2i], [3, 3i]]
* B. [[2, −2i], [3, −3i]]
* C. [[2, 3], [−2i, −3i]]
* D. [[2, −2i], [3, 3i]]

**Answer: B**


**Q3 (Understand).** What is special about |ψ⟩⟨ψ| for a normalised |ψ⟩?

* A. It is a Hermitian projection operator satisfying P² = P
* B. It is a scalar equal to 1
* C. It is an anti-Hermitian operator
* D. It has rank equal to the dimension of the space

**Answer: A**


**Q4 (Analyze).** Which expression writes a Hermitian operator A in terms of its eigenstates |aᵢ⟩ and eigenvalues aᵢ (spectral decomposition)?

* A. A = Σ aᵢ ⟨aᵢ|aᵢ⟩
* B. A = Σ |aᵢ⟩⟨aᵢ|
* C. A = Σ aᵢ |aᵢ⟩⟨aᵢ|
* D. A = Σ aᵢ |aᵢ⟩|aᵢ⟩

**Answer: C**


**Q5 (Evaluate).** Which is the correct density matrix for the Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2?

* A. ρ = ½(|00⟩ + |11⟩)(|00⟩ + |11⟩)
* B. ρ = (⟨00| + ⟨11|)/√2
* C. ρ = ½|00⟩⟨11|
* D. ρ = ½(|00⟩ + |11⟩)(⟨00| + ⟨11|)

**Answer: D**


**Q6 (Remember).** What is the rank of the matrix produced by an outer product |ψ⟩⟨φ| of non-zero vectors?

* A. 0
* B. 2
* C. Equal to the dimension of the space
* D. 1

**Answer: D**


### 2.7 Tensor Product of Vector Spaces

*Sources: QM\_linear\_algebra §2.5.1–2.5.7*


**Q1 (Remember).** If dim V = m and dim W = n, what is dim(V ⊗ W)?

* A. m + n
* B. mn
* C. mⁿ
* D. m − n

**Answer: B**


**Q2 (Understand).** Which set is the standard basis of the two-qubit space C² ⊗ C²?

* A. |00⟩, |01⟩, |10⟩, |11⟩
* B. |0⟩, |1⟩
* C. |00⟩, |11⟩
* D. |00⟩, |01⟩, |10⟩

**Answer: A**


**Q3 (Apply).** Using the Kronecker product, what is u ⊗ v for u = (2, 1) and v = (1, 3)?

* A. (2, 1, 6, 3)
* B. (3, 4)
* C. (2, 6, 1, 3)
* D. (2, 3, 1, 6)

**Answer: C**


**Q4 (Apply).** Given I ⊗ X (X the Pauli-X matrix), what is (I ⊗ X)|00⟩?

* A. |10⟩
* B. |00⟩
* C. |11⟩
* D. |01⟩

**Answer: D**


**Q5 (Analyze).** Which state cannot be written as a tensor product |v⟩ ⊗ |w⟩ (is entangled)?

* A. (|00⟩ + |11⟩)/√2
* B. |0⟩ ⊗ |1⟩
* C. |1⟩ ⊗ |1⟩
* D. ((|0⟩ + |1⟩)/√2) ⊗ |0⟩

**Answer: A**


**Q6 (Evaluate).** A student says a 2-level system combined with a 3-level system has a 5-dimensional state space. Evaluate this.

* A. Correct; dimensions add for composite systems
* B. Incorrect; the dimension is the product 2 × 3 = 6
* C. Incorrect; the dimension is 2³ = 8
* D. Incorrect; the dimension is 3

**Answer: B**


### 2.8 Linear Operators

*Sources: QM\_linear\_algebra §3.1–3.2, §3.8 Problems 3–4; Problems in Linear Operator*


**Q1 (Remember).** Which property defines a linear operator Â?

* A. Â|ψ⟩ = |ψ⟩ for all states
* B. Â|ψ⟩ = 0 for all states
* C. Â[c₁|ψ₁⟩ + c₂|ψ₂⟩] = c₁Â|ψ₁⟩ + c₂Â|ψ₂⟩
* D. ÂB̂ = B̂Â for all operators B̂

**Answer: C**


**Q2 (Understand).** Why is the order of operators important in quantum mechanics?

* A. Operators can only act on one state at a time
* B. Operators always commute but only in a fixed basis
* C. Operator products are undefined
* D. Operator multiplication is in general non-commutative, so ÂB̂ and B̂Â can differ

**Answer: D**


**Q3 (Apply).** In an orthonormal basis {|a⟩, |b⟩, |c⟩}, Â|a⟩ = 2|a⟩, Â|b⟩ = 3|a⟩ − i|c⟩, Â|c⟩ = −|b⟩. What is Â as a matrix?

* A. [[2, 0, 0], [3, 0, −i], [0, −1, 0]]
* B. [[2, 3, 0], [0, 0, −1], [0, −i, 0]]
* C. [[2, 3, 0], [0, 0, −1], [0, i, 0]]
* D. [[2, 0, 0], [0, 0, −1], [3, −i, 0]]

**Answer: B**


**Q4 (Apply).** For |Ψ⟩ = 2i|a⟩ − |b⟩ + 4i|c⟩ and Â = |a⟩⟨a| − 2i|b⟩⟨b| + |c⟩⟨c| (orthonormal basis), what is ⟨Â⟩ = ⟨Ψ|Â|Ψ⟩?

* A. 20 − 2i
* B. 20 + 2i
* C. 4 − 2i
* D. 16 − 2i

**Answer: A**


**Q5 (Evaluate).** Â|ψ⟩ = B̂|ψ⟩ holds for one particular state |ψ⟩. A student concludes Â = B̂. Evaluate this.

* A. Correct; one state is enough to prove equality
* B. Correct, provided |ψ⟩ is normalised
* C. Incorrect; operators are identical only if they act identically on all state vectors of the space
* D. Incorrect; operators can never be equal

**Answer: C**


**Q6 (Understand).** What is notable about the unit (identity) operator's matrix form?

* A. It is the identity matrix in every basis (Iᵢⱼ = δᵢⱼ)
* B. It changes form whenever the basis changes
* C. It has only off-diagonal elements
* D. It has all matrix elements equal to zero

**Answer: A**


### 2.9 Matrix Algebra

*Sources: Matrix algebra notes; Matrix algebra to Eigenvectors slides; QM\_linear\_algebra §3.6, §3.8 Problem 5*


**Q1 (Remember).** When is the matrix product AB defined, and what is (AB)ᵢⱼ?

* A. Only when A and B have identical entries; (AB)ᵢⱼ = AᵢⱼBᵢⱼ
* B. Always; (AB)ᵢⱼ = Σₖ Aₖᵢ Bⱼₖ
* C. When the rows of A equal the columns of B; (AB)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
* D. When the number of columns of A equals the number of rows of B; (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ

**Answer: D**


**Q2 (Apply).** What is the adjoint (Hermitian conjugate) of A = [[1, i], [2, 3]]?

* A. [[1, 2], [i, 3]]
* B. [[1, 2], [−i, 3]]
* C. [[1, −i], [2, 3]]
* D. [[1, i], [2, 3]]

**Answer: B**


**Q3 (Apply).** For A = [[1, 2], [3, −4]], what are Tr A and det A?

* A. Tr A = −3 and det A = 10
* B. Tr A = 5 and det A = −10
* C. Tr A = −3 and det A = −10
* D. Tr A = 3 and det A = 2

**Answer: C**


**Q4 (Understand).** What does det(A) = 0 tell us about a matrix?

* A. A is invertible
* B. A is Hermitian
* C. A is the identity matrix
* D. A is singular, i.e. not invertible

**Answer: D**


**Q5 (Analyze).** In φⱼ = Σᵢ Aⱼᵢψᵢ with Aⱼᵢ ≡ ⟨ϕⱼ|Â|ϕᵢ⟩, what happens if the basis is changed?

* A. Both the equation and the matrix elements stay the same
* B. The operator changes into a different operator
* C. The operator equation is unchanged but the numerical matrix elements Aⱼᵢ change
* D. The state vectors become orthogonal

**Answer: C**


**Q6 (Evaluate).** A = [[1, 0, −3i], [3, 5, 0], [3i, 0, −2]] has real diagonal entries. A student calls it Hermitian. Evaluate this.

* A. Correct; real diagonal entries are sufficient
* B. Incorrect; A₂₁ = 3 but A₁₂\* = 0, so Aᵢⱼ ≠ Aⱼᵢ\* and A is not Hermitian
* C. Correct; A₁₃ = −3i and A₃₁ = 3i are conjugates, so all entries match
* D. Incorrect; a Hermitian matrix must be symmetric with real entries

**Answer: B**


### 2.10 Hermitian Operators

*Sources: Hermitian Operator and Pauli matrices notes; Unitary and Projection operators slides; QM\_linear\_algebra §3.5–3.6.1*


**Q1 (Remember).** What condition defines a Hermitian operator, and what is its matrix form?

* A. Â = Â†, i.e. Aᵢⱼ = Aⱼᵢ\*
* B. Â† = Â⁻¹, i.e. Aᵢⱼ = 1/Aⱼᵢ
* C. Â² = Â, i.e. Aᵢⱼ = Aᵢⱼ²
* D. ÂB̂ = B̂Â for every B̂

**Answer: A**


**Q2 (Understand).** Why are observables represented by Hermitian operators?

* A. Their eigenvalues are always integers
* B. They are always equal to the identity
* C. They have no eigenvectors
* D. Their eigenvalues are real, matching the real results of measurements

**Answer: D**


**Q3 (Remember).** Which is NOT a property of Hermitian operators?

* A. Their eigenvalues are real
* B. Eigenfunctions of distinct eigenvalues are orthogonal
* C. Their eigenvalues are always purely imaginary
* D. Their eigenfunctions form a complete set

**Answer: C**


**Q4 (Apply).** The 1D harmonic oscillator Hamiltonian is Ĥ = p̂²/2m + ½mω²x̂². Why is Ĥ Hermitian?

* A. Because it contains a factor of ½
* B. Because x̂ and p̂ are Hermitian
* C. Because it commutes with x̂
* D. Because its eigenvalues are complex

**Answer: B**


**Q5 (Analyze).** How is the Hadamard gate H = (1/√2)[[1, 1], [1, −1]] best classified?

* A. Both Hermitian (H† = H) and unitary (H†H = I)
* B. Hermitian but not unitary
* C. Unitary but not Hermitian
* D. Neither Hermitian nor unitary

**Answer: A**


**Q6 (Evaluate).** A student claims eigenfunctions of a Hermitian operator with different eigenvalues need not be orthogonal. Evaluate this.

* A. Incorrect; such eigenfunctions are orthogonal
* B. Correct; orthogonality holds only for degenerate eigenvalues
* C. Correct; orthogonality holds only for real operators
* D. Incorrect; they are always identical

**Answer: A**


### 2.11 Unitary and Projection Operators

*Sources: Unitary and Projection operators slides; Projection Operator Problems; QM\_linear\_algebra §3.4*


**Q1 (Remember).** What is the defining condition of a unitary operator?

* A. Û = Û†
* B. Û†Û = I, so the adjoint equals the inverse (Û† = Û⁻¹)
* C. Û² = Û
* D. Û|ψ⟩ = 0 for all |ψ⟩

**Answer: B**


**Q2 (Understand).** What does unitary evolution do to the total probability of a state, and where do its eigenvalues lie?

* A. It halves the probability; eigenvalues are real
* B. It preserves probability; eigenvalues are real and positive
* C. It preserves total probability; eigenvalues have the form e^{iθ}, lying on the unit circle
* D. It changes the probability; eigenvalues are zero

**Answer: C**


**Q3 (Remember).** Which two conditions define a projection operator P?

* A. P = −P† and P² = I
* B. P† = P⁻¹ and P² = P
* C. P = 0 and P² = P
* D. P = P† (Hermitian) and P² = P (idempotent)

**Answer: D**


**Q4 (Apply).** With P₊ = |z+⟩⟨z+| = [[1, 0], [0, 0]], what is P₋ = 1 − P₊?

* A. [[0, 0], [0, 1]]
* B. [[0, 1], [1, 0]]
* C. [[1, 0], [0, 1]]
* D. [[0, 0], [1, 0]]

**Answer: A**


**Q5 (Analyze).** For projectors Pᵢ = |i⟩⟨i| onto an orthonormal basis, which relations hold?

* A. PᵢPⱼ = Pᵢ for i ≠ j, and ΣPᵢ = 0
* B. PᵢPⱼ = 0 for i ≠ j, and ΣPᵢ = I (closure)
* C. PᵢPⱼ = I for i ≠ j, and ΣPᵢ = I
* D. PᵢPⱼ = 0 for all i, j, and ΣPᵢ = 0

**Answer: B**


**Q6 (Evaluate).** A student says measurement, like every quantum gate, is represented by a unitary matrix. Evaluate this.

* A. Correct; measurement is the most important unitary operation
* B. Correct; measurement is unitary because it preserves probability
* C. Incorrect; all qubit operations except measurement are unitary
* D. Incorrect; gates are non-unitary and measurement is unitary

**Answer: C**


### 2.12 Eigenvalues and Eigenvectors

*Sources: Matrix algebra to Eigenvectors slides (Examples 1–4); QM\_linear\_algebra §4; Eigenvalues and eigenvectors problems*


**Q1 (Remember).** How are the eigenvalues of a matrix A obtained?

* A. By solving det(A + λI) = 1
* B. By taking the trace of A
* C. By transposing A
* D. By solving the characteristic equation det(A − λI) = 0

**Answer: D**


**Q2 (Apply).** For A = [[1, 2], [3, −4]], the characteristic equation is λ² + 3λ − 10 = 0. What are the eigenvalues?

* A. λ = 5 and λ = −2
* B. λ = −5 and λ = 2
* C. λ = 1 and λ = −4
* D. λ = −5 and λ = −2

**Answer: B**


**Q3 (Apply).** For A = [[2, 2], [1, 3]] the eigenvalues are 4 and 1. Which is an eigenvector for λ = 1?

* A. (1, 1)
* B. (2, 1)
* C. (1, −2)
* D. (−2, 1)

**Answer: D**


**Q4 (Apply).** For A = [[1, 2], [−1, 4]] (eigenvalues 3 and 2), which eigenvector corresponds to λ = 2?

* A. (1, 1)
* B. (1, 2)
* C. (2, 1)
* D. (1, −1)

**Answer: C**


**Q5 (Analyze).** For A = [[2, −3, 0], [2, −5, 0], [0, 0, 3]], which is the set of eigenvalues?

* A. 1, −4 and 3
* B. 2, −5 and 3
* C. 1, 4 and 3
* D. −1, 4 and 3

**Answer: A**


**Q6 (Evaluate).** For [[2, 0, 0], [0, 3, 4], [0, 4, 9]], a student reads off eigenvalues 2, 3, 9 (the diagonal). Evaluate this.

* A. Correct; the eigenvalues are always the diagonal entries
* B. Incorrect; the eigenvalues are 1, 3 and 9
* C. Incorrect; the eigenvalues are 2, 4 and 9
* D. Incorrect; the matrix is not diagonal, and its eigenvalues are 1, 2 and 11

**Answer: D**


### 2.13 Pauli Matrices

*Sources: Hermitian Operator and Pauli matrices notes; Paulis matrices and Commutation relations slides; QM\_linear\_algebra §3.7*


**Q1 (Remember).** Which matrix is σ\_y?

* A. [[0, 1], [1, 0]]
* B. [[1, 0], [0, −1]]
* C. [[0, −i], [i, 0]]
* D. [[0, i], [−i, 0]]

**Answer: C**


**Q2 (Understand).** Which set lists the key properties of the Pauli matrices?

* A. Hermitian, unitary, traceless, and each squares to the identity
* B. Anti-Hermitian, non-unitary, trace 1, squares to zero
* C. Hermitian, non-unitary, trace 2, squares to −I
* D. Unitary only, with non-zero trace

**Answer: A**


**Q3 (Apply).** Using the Pauli product relations, what is σ\_zσ\_x?

* A. −iσ\_y
* B. iσ\_y
* C. iσ\_x
* D. σ\_y

**Answer: B**


**Q4 (Analyze).** What follows from [σ\_x, σ\_y] = 2iσ\_z ≠ 0?

* A. Spin components can always be measured together
* B. σ\_x and σ\_y have identical eigenvalues
* C. Spin components along different axes cannot be measured simultaneously with arbitrary precision
* D. σ\_z must equal zero

**Answer: C**


**Q5 (Analyze).** Given {σᵢ, σⱼ} = 2δᵢⱼ I, what is {σ\_x, σ\_y}?

* A. 0
* B. 2I
* C. 2iσ\_z
* D. I

**Answer: A**


**Q6 (Evaluate).** A student says σ\_y cannot be Hermitian because it has imaginary entries. Evaluate this.

* A. Correct; Hermitian matrices must be real
* B. Incorrect; σ\_y† = σ\_y, since the conjugate transpose restores the original matrix
* C. Correct; σ\_y is anti-Hermitian
* D. Incorrect; σ\_y is Hermitian only in the z-basis

**Answer: B**


### 2.14 Commutation Relations

*Sources: Paulis matrices and Commutation relations slides (rules, [x, p], H = p²/2μ + ½μω²x²); Commutation relations problems; QM\_linear\_algebra §3.3*


**Q1 (Remember).** How is the commutator of Â and B̂ defined?

* A. [Â, B̂] = ÂB̂ + B̂Â
* B. [Â, B̂] = ÂB̂ / B̂Â
* C. [Â, B̂] = Â + B̂
* D. [Â, B̂] = ÂB̂ − B̂Â

**Answer: D**


**Q2 (Remember).** What is the canonical commutation relation between x̂ and p̂ₓ?

* A. [x̂, p̂ₓ] = 0
* B. [x̂, p̂ₓ] = iħ
* C. [x̂, p̂ₓ] = ħ
* D. [x̂, p̂ₓ] = −ħ²

**Answer: B**


**Q3 (Apply).** Which product-rule identity holds for commutators?

* A. [Â, B̂Ĉ] = [Â, B̂][Â, Ĉ]
* B. [Â, B̂Ĉ] = B̂Ĉ[Â, 1]
* C. [Â, B̂Ĉ] = [Â, B̂]Ĉ + B̂[Â, Ĉ]
* D. [Â, B̂Ĉ] = [Â, B̂] − [Â, Ĉ]

**Answer: C**


**Q4 (Apply).** For H = p²/2μ + ½μω²x², what is xH − Hx = [x, H]?

* A. iħp/μ
* B. −iħp/μ
* C. iħμω²x
* D. 0

**Answer: A**


**Q5 (Analyze).** From [x̂ᵢ, p̂ⱼ] = iħδᵢⱼ, which commutator vanishes?

* A. [x̂, p̂ₓ]
* B. [ŷ, p̂\_y]
* C. [ẑ, p̂\_z]
* D. [x̂, p̂\_y]

**Answer: D**


**Q6 (Evaluate).** A student says two observables whose operators have a non-zero commutator can be measured simultaneously with arbitrary precision. Evaluate this.

* A. Incorrect; non-commuting observables are subject to the Heisenberg uncertainty principle
* B. Correct; only commuting operators are limited by uncertainty
* C. Correct; commutators only affect the energy
* D. Incorrect; non-commuting observables can never be measured at all

**Answer: A**


---

## Module 3 — Postulates of Quantum Mechanics and Sequential Stern–Gerlach Experiments


### 3.1 Observables

*Sources: Class 1\_Module 3\_Postulates of Quantum mechanics (slides 3–5); Module 3 Postulates of QM – General Material*


**Q1 (Remember).** In quantum mechanics, physical observables are represented by which mathematical objects?

* A. Real-valued functions of position only
* B. Hermitian operators acting on states in a Hilbert space
* C. Unitary matrices that preserve probability
* D. Fixed numbers fixed by the exact classical state

**Answer: B**


**Q2 (Remember).** Which set lists physical properties treated as observables in the notes?

* A. Wavefunction, probability, phase and amplitude
* B. Mass, charge, gravity and time
* C. Position, momentum, energy and angular momentum
* D. Bra, ket, operator and eigenvalue

**Answer: C**


**Q3 (Understand).** How does the quantum description of an observable differ from the classical one?

* A. The observable always has one exact value fixed before measurement
* B. The observable has no possible values at all
* C. The observable is replaced by the wavefunction's phase
* D. An operator acts on the state, and a measurement returns one of a set of allowed values with probabilities

**Answer: D**


**Q4 (Apply).** Which observable–operator pairing appears in the notes' correspondence table?

* A. Total energy ↔ Ĥ; position ↔ x̂; momentum ↔ P̂
* B. Total energy ↔ P̂; momentum ↔ Ĥ; position ↔ x̂
* C. Total energy ↔ x̂; position ↔ Ĥ; momentum ↔ P̂
* D. Total energy ↔ P̂; position ↔ P̂; momentum ↔ Ĥ

**Answer: A**


**Q5 (Evaluate).** A student argues observables could be represented by any operator. Why is that unsatisfactory?

* A. Only Hermitian operators have no eigenvalues
* B. Measured values must be real, so the operator must have real eigenvalues, which Hermitian operators guarantee
* C. Non-Hermitian operators cannot act on wavefunctions
* D. Observables must always have imaginary values

**Answer: B**


### 3.2 Operators and Hermitian Operators

*Sources: Postulates slides 4–6 (operator tables); Module 3 General Material (Hermitian Operators)*


**Q1 (Remember).** What is the position-space form of the momentum operator p̂?

* A. p̂ = +ħ d/dx
* B. p̂ = −ħ² d²/dx²
* C. p̂ = x
* D. p̂ = −iħ d/dx

**Answer: D**


**Q2 (Understand).** What does the eigenvalue form P̂ψ(x) = p ψ(x) tell us about p?

* A. p is the operator itself
* B. p is always the expectation of x
* C. p is the numerical momentum value measured in the lab if the system is in the state ψ(x)
* D. p is the normalisation constant of ψ

**Answer: C**


**Q3 (Apply).** What is the one-dimensional kinetic-energy operator T̂?

* A. T̂ = −(ħ²/2m) d²/dx²
* B. T̂ = +(ħ²/2m) d²/dx²
* C. T̂ = −iħ d/dx
* D. T̂ = x²/2m

**Answer: A**


**Q4 (Apply).** What is the time-independent Hamiltonian operator in one dimension?

* A. Ĥ = −iħ d/dx + V(x)
* B. Ĥ = −(ħ²/2m) d²/dx² + V(x)
* C. Ĥ = −(ħ²/2m) d/dx + V(x)
* D. Ĥ = V(x) only

**Answer: B**


**Q5 (Analyze).** Which observable–operator pairing is given in the notes' table?

* A. z-component of angular momentum ↔ −iħ ∂/∂x
* B. Kinetic energy ↔ −iħ ∂/∂x
* C. Position ↔ −ħ² ∂²/∂x²
* D. z-component of angular momentum ↔ −iħ ∂/∂φ

**Answer: D**


**Q6 (Understand).** In three dimensions, how does the kinetic-energy operator generalise?

* A. T̂ = −iħ(∂/∂x + ∂/∂y + ∂/∂z)
* B. T̂ = −(ħ²/2m) ∂²/∂x² only
* C. T̂ = −(ħ²/2m)(∂²/∂x² + ∂²/∂y² + ∂²/∂z²)
* D. T̂ = (ħ²/2m)(x² + y² + z²)

**Answer: C**


### 3.3 Eigenvalues and Eigenfunctions

*Sources: Postulates slides 7–9; Module 3 General Material (definite states, framework)*


**Q1 (Remember).** What does the eigenvalue equation Ĝψₙ = Gₙψₙ state?

* A. The operator is the inverse of ψₙ
* B. ψₙ is always a constant
* C. Acting with the operator on ψₙ returns the same function times a constant Gₙ
* D. Gₙ is always zero

**Answer: C**


**Q2 (Apply).** For ψ = e^{2x} and Ĝ = d²/dx², what is the eigenvalue?

* A. 4
* B. 2
* C. 8
* D. 1/4

**Answer: A**


**Q3 (Understand).** What does the postulate that only eigenvalues Gₙ are ever observed imply?

* A. Every observable can take any real value
* B. Values of dynamical variables are quantised
* C. Measurement never disturbs the system
* D. All observables have the same eigenvalue

**Answer: B**


**Q4 (Understand).** What is a 'definite state' of an observable?

* A. A superposition of all eigenstates with equal weights
* B. A state with zero energy
* C. A state whose wavefunction is not normalised
* D. An eigenstate in which the observable has a 100% certain value

**Answer: D**


**Q5 (Analyze).** According to the notes' framework, how do you find the possible measured values of an observable and the state for each value?

* A. Find the eigenvectors for the values, and the trace for the states
* B. Take the expectation value for both
* C. Differentiate the wavefunction twice
* D. Find the eigenvalues for the values, and the eigenvectors for the corresponding states

**Answer: D**


**Q6 (Evaluate).** A student says the eigenvalue of d²/dx² acting on e^{2x} is 2. Evaluate this.

* A. Incorrect; d²/dx² e^{2x} = 4e^{2x}, so the eigenvalue is 4
* B. Correct; the eigenvalue is the exponent
* C. Incorrect; the eigenvalue is 8
* D. Correct; second derivatives halve the exponent

**Answer: A**


### 3.4 Expectation Values

*Sources: Postulates slides 10–19 (average position, ⟨p⟩, ⟨p²⟩, harmonic-oscillator sample problem)*


**Q1 (Remember).** For a normalised wavefunction Ψ, how is ⟨x⟩ defined?

* A. ⟨x⟩ = ∫ Ψ dx
* B. ⟨x⟩ = ∫ x |Ψ|² dx over all space
* C. ⟨x⟩ = ∫ |Ψ|² dx
* D. ⟨x⟩ = x |Ψ|

**Answer: B**


**Q2 (Understand).** What does an expectation value represent experimentally?

* A. The single value obtained in every measurement
* B. The maximum possible result
* C. The average of the results of many identical measurements
* D. The value of the quantity at a single point

**Answer: C**


**Q3 (Apply).** For a free particle ψ(x) = Ae^{ipx/ħ}, what is ⟨p⟩?

* A. ⟨p⟩ = 0
* B. ⟨p⟩ = ħ²k²
* C. ⟨p⟩ = p = ħk = h/λ
* D. ⟨p⟩ = h/(λ²)

**Answer: C**


**Q4 (Apply).** For ψ(x) = √(2/L) sin(πx/L) in 0 < x < L, what is ⟨p⟩?

* A. ħπ/L
* B. 0
* C. ħ/2L
* D. iħ/L

**Answer: B**


**Q5 (Analyze).** Why is ⟨p⟩ = 0 for any real wavefunction?

* A. Because real functions have no derivative
* B. Because ħ = 0 for real functions
* C. Because ψ² is always a constant
* D. The integral reduces to (ħ/2i)ψ² evaluated at ±∞, which vanishes

**Answer: D**


**Q6 (Apply).** For the harmonic oscillator ground state, ⟨x²⟩ = 1/2A and ⟨p²⟩ = ħ²A/2 with ⟨x⟩ = ⟨p⟩ = 0. What is ΔxΔp?

* A. ħ/2
* B. ħ
* C. ħ/4
* D. 2ħ

**Answer: A**


**Q7 (Evaluate).** Using ψ = ax on 0 ≤ x ≤ 1, a student finds ⟨x⟩ = a²/4 without normalising. Evaluate this.

* A. It is correct for any value of a
* B. Normalisation requires a = 1, so ⟨x⟩ = 1/4
* C. It is only valid after normalising; requiring a²/3 = 1 gives a² = 3, so ⟨x⟩ = 3/4
* D. Normalisation is unnecessary for position

**Answer: C**


**Q8 (Analyze).** Integration by parts gives which form for ⟨p²⟩?

* A. ⟨p²⟩ = ħ² ∫ |dψ/dx|² dx
* B. ⟨p²⟩ = ħ² ∫ ψ² dx
* C. ⟨p²⟩ = −ħ² ∫ dψ/dx dx
* D. ⟨p²⟩ = ħ ∫ |dψ/dx| dx

**Answer: A**


### 3.5 Sequential Stern–Gerlach: The Experiment and the Spin-½ Ket Description

*Sources: Sequential S-G experiment slides; Stern Gerlac experiment\_sequential (§1.1–1.2)*


**Q1 (Remember).** What did Stern and Gerlach observe in 1922 when a silver-atom beam passed through an inhomogeneous magnetic field?

* A. A single undeflected beam
* B. The beam split into two distinct beams
* C. A continuous smear of deflections
* D. Three equally spaced beams

**Answer: B**


**Q2 (Understand).** Why does the two-beam result contradict the classical expectation?

* A. Classically the atoms would not be deflected at all
* B. Classically exactly two values are expected
* C. Classically the spin has no component along z
* D. Classically the spin component would range continuously from −|S| to +|S|, giving a continuous spread

**Answer: D**


**Q3 (Remember).** What gives a silver atom its net magnetic moment in this analysis?

* A. The lone 5s electron outside closed shells (47 electrons in total)
* B. The 47 protons alone
* C. All 60 or 62 neutrons
* D. The filled 4d shell

**Answer: A**


**Q4 (Apply).** What values of S\_z did the deflections correspond to, and what is ħ?

* A. S\_z = ±ħ, with ħ = 6.63 × 10⁻³⁴ J·s
* B. S\_z = ±ħ/2, with ħ = 1.0546 × 10⁻³⁴ J·s
* C. S\_z = 0 only
* D. S\_z = ±ħ/2, with ħ = 1.0546 × 10⁻¹⁹ J·s

**Answer: B**


**Q5 (Analyze).** The deflecting force is F\_z ∝ S\_z ∂B\_z/∂z. What does the deflection therefore measure?

* A. The total spin magnitude only
* B. The spin component perpendicular to the gradient
* C. The mass of the atom
* D. The component of the spin along the z-axis, the direction of the field gradient

**Answer: D**


**Q6 (Understand).** What do the kets |+⟩ and |−⟩ represent for a z-oriented analyzer?

* A. Two different atomic masses
* B. The magnetic field direction
* C. States of atoms leaving the upper port (S\_z = +ħ/2) and lower port (S\_z = −ħ/2)
* D. Unnormalised probability counts

**Answer: C**


**Q7 (Evaluate).** Is the z-axis special for the experiment's results?

* A. No; nothing is special about the z-axis, and any axis gives the same behaviour
* B. Yes; only the z-axis gives two beams
* C. Yes; other axes give continuous beams
* D. No; any axis gives three beams

**Answer: A**


### 3.6 Experiments 1 and 2: Repeated and Orthogonal Measurements

*Sources: Sequential S-G slides; Stern Gerlac experiment\_sequential (§1.1.1–1.1.2, Figs. 1.3–1.4)*


**Q1 (Remember).** In Experiment 1, two analyzers measure S\_z in succession. What is seen at the second analyzer?

* A. Half the atoms exit each port
* B. No atoms ever exit its lower port; all atoms from the first analyzer's upper port exit its upper port
* C. All atoms exit the lower port
* D. The atoms are randomly distributed among three ports

**Answer: B**


**Q2 (Understand).** What role does the first analyzer play in Experiment 1?

* A. It absorbs the atoms
* B. It changes the magnitude of the spin
* C. It prepares the state (a state-preparation device) for the second analyzer
* D. It converts atoms into photons

**Answer: C**


**Q3 (Apply).** In Experiment 2 (z then x), 50 atoms enter the x-analyzer. How many exit each port on average?

* A. 50 from the upper port and 0 from the lower
* B. 0 from the upper port and 50 from the lower
* C. 10 and 40
* D. 25 from each port

**Answer: D**


**Q4 (Analyze).** Would Experiment 2's results change if the lower port of the first analyzer were used instead?

* A. Yes; all atoms would exit the upper port
* B. No; the results would be unchanged, with 50% in each port
* C. Yes; no atoms would exit
* D. Yes; the ratio would become 25:75

**Answer: B**


**Q5 (Understand).** What can be said about which port a given atom exits in Experiment 2?

* A. Only probabilities can be given: a 50% chance for each port, with random arrival sequences
* B. The exit port can be predicted exactly
* C. The exit port depends on the atom's mass
* D. Every atom exits the lower port

**Answer: A**


**Q6 (Evaluate).** A hidden-variable proposal says each atom carries a pre-determined set of instructions to explain the randomness. What does the text report?

* A. Bell proved local hidden-variable theories are fully correct
* B. Stern and Gerlach proved hidden variables in 1922
* C. John Bell proved that local hidden-variable theories are not consistent with quantum mechanics
* D. Hidden variables were shown to explain all experiments without probability

**Answer: C**


### 3.7 Experiment 3: Z–X–Z Successive Measurements

*Sources: Sequential S-G slides; Stern Gerlac experiment\_sequential (§1.1.3, Fig. 1.5)*


**Q1 (Remember).** In Experiment 3, what is the sequence of analyzers?

* A. Z, then Z, then X
* B. X, then X, then X
* C. Z, then Z, then Z
* D. Z, then X, then Z

**Answer: D**


**Q2 (Apply).** With 500 atoms entering, 250 pass the X analyzer's selected port. How many exit the upper port of the final Z analyzer?

* A. 125
* B. 250
* C. 0
* D. 62

**Answer: A**


**Q3 (Understand).** What would classical reasoning predict for the third measurement, and what is found?

* A. Classically 50/50; quantum gives all up
* B. Both predict all up
* C. Both predict all down
* D. Classically S\_z = +ħ/2 (all up); quantum mechanics gives 50% in each port

**Answer: D**


**Q4 (Analyze).** What does Experiment 3 show about S\_x and S\_z?

* A. They are always measured together exactly
* B. They are incompatible observables, so their values cannot be known simultaneously
* C. They are identical observables
* D. S\_x always equals S\_z

**Answer: B**


**Q5 (Evaluate).** What key feature of quantum mechanics is demonstrated by the 'forgotten' first result?

* A. Measurement never changes the system
* B. Atoms permanently remember all measurements
* C. A measurement disturbs the system
* D. The analyzers are faulty

**Answer: C**


**Q6 (Apply).** What fraction of the original 500 atoms exit the final analyzer's upper port?

* A. 50%
* B. 12.5%
* C. 5%
* D. 25%

**Answer: D**


### 3.8 Experiment 4: One Beam versus Recombined Beams

*Sources: Sequential S-G slides; Stern Gerlac experiment\_sequential (§1.1.4, Fig. 1.6, Young double-slit analogy)*


**Q1 (Remember).** How does Experiment 4b differ from 4a?

* A. Both beams are blocked
* B. The lower beam is blocked and the third analyzer is removed
* C. The upper beam of the second analyzer is blocked and only the lower beam goes to the third
* D. The analyzers are rotated to the y-axis

**Answer: C**


**Q2 (Apply).** In Experiment 4a, 100 atoms enter. How many exit each port of the third analyzer?

* A. 50 and 0
* B. 25 from the upper port and 25 from the lower port
* C. 100 and 0
* D. 0 and 100

**Answer: B**


**Q3 (Understand).** In Experiment 4c, what does classical probability predict at the third analyzer, and what does quantum mechanics give?

* A. Classical: 50% per port; quantum: all atoms exit the upper port and none the lower
* B. Classical: all in the upper port; quantum: 50% each
* C. Both predict 25% per port
* D. Both predict none exit

**Answer: A**


**Q4 (Analyze).** What is odd about the lower port of the third analyzer in 4c compared with 4a/4b?

* A. More atoms emerge there than in 4a
* B. The same 25% emerge
* C. No atoms emerge there, although 25% did when only one path was open
* D. It becomes the only open port

**Answer: C**


**Q5 (Evaluate).** Which explanation does the text give via the double-slit analogy?

* A. Probabilities are added directly
* B. Amplitudes are added first and then squared, allowing interference
* C. The atoms are absorbed by the second analyzer
* D. The third analyzer is defective

**Answer: B**


**Q6 (Create).** To make every atom exit the upper port of the third analyzer, which modification of Experiment 3 would work?

* A. Recombine both beams from the second analyzer properly (Experiment 4c)
* B. Block the upper beam of the second analyzer
* C. Rotate the third analyzer to the x-axis
* D. Add a fourth analyzer along the y-axis

**Answer: A**


### 3.9 Incompatible Observables and the Sock Analogy

*Sources: Stern Gerlac experiment\_sequential (Prologue on Erwin's socks; §1.1.3)*


**Q1 (Remember).** What name is given to pairs like S\_x and S\_z whose values cannot be known simultaneously?

* A. Commuting observables
* B. Identical observables
* C. Conserved observables
* D. Incompatible observables

**Answer: D**


**Q2 (Understand).** What happens in the Erwin's-socks analogy after sorting by colour, then by length, then by colour again?

* A. The colour stays the same
* B. All socks become black
* C. The colour measured first has become random, as if the socks forgot the first measurement
* D. The socks change in length

**Answer: C**


**Q3 (Analyze).** Are all pairs of quantum-mechanical observables incompatible?

* A. Yes; all pairs are incompatible
* B. No; some experiments can be done without disturbing certain other observables
* C. Yes, but only for spin
* D. No; none are incompatible

**Answer: B**


**Q4 (Understand).** Why must the recombination of the two beams in Experiment 4c be done 'properly'?

* A. To avoid disturbing the beams
* B. To make the beams brighter
* C. To convert spin-up atoms into spin-down atoms
* D. To block the lower beam

**Answer: A**


**Q5 (Evaluate).** Can a cleverer experiment avoid disturbing the system when measuring S\_x after S\_z?

* A. Yes; a better analyzer removes it
* B. Yes; a colder beam removes it
* C. Yes; shorter magnets remove it
* D. No; the incompatibility between S\_x and S\_z is fundamental

**Answer: D**


---

## Module 4 — Particle in a One-Dimensional Box (Infinite Potential Well)


### 4.1 The 1D Box: Potential and Physical Picture

*Sources: Class 6 Particle in 1D box (slides 3–4); Extra Problems on 1D box*


**Q1 (Remember).** What is the potential energy V(x) for a particle in a 1D box of width L?

* A. V = ∞ inside and 0 outside
* B. V = 0 everywhere
* C. V = 0 for 0 < x < L and V = ∞ outside the box
* D. V = −∞ at the walls only

**Answer: C**


**Q2 (Understand).** How does the quantum picture differ from the classical picture of a particle in a box?

* A. Classically the particle can be anywhere; quantum mechanically it is described by a wavefunction with some regions more probable than others
* B. Quantum: the particle sits at rest at one point
* C. Classical: the wavefunction has nodes
* D. There is no difference

**Answer: A**


**Q3 (Apply).** What is the particle's potential energy inside the box?

* A. Infinite
* B. Zero
* C. Equal to E₁
* D. Negative and equal to −E\_n

**Answer: B**


**Q4 (Understand).** Why is V = 0 a convenient choice inside the box?

* A. Because the walls exert a force inside
* B. Because energy must be negative
* C. Because the particle has no mass
* D. No force acts inside (F = −dV/dx = 0), so the potential is constant and can be set to zero

**Answer: D**


**Q5 (Evaluate).** A student says the 1D box is an exact model of a real atom's potential. Evaluate this.

* A. Incorrect; it is an idealised model that approximates some situations such as an electron confined in a wire or metal piece
* B. Correct; real atoms have flat infinite walls
* C. Correct; it is exact for hydrogen
* D. Incorrect; it cannot approximate anything

**Answer: A**


### 4.2 Wavefunction and Boundary Conditions

*Sources: Class 6 Particle in 1D box (slides 4–6)*


**Q1 (Remember).** What general solution applies inside the box?

* A. ψ(x) = A e^{−x}
* B. ψ(x) = A x + B
* C. ψ(x) = A/x
* D. ψ(x) = A sin kx + B cos kx, with k² = 2mE/ħ²

**Answer: D**


**Q2 (Understand).** Why must ψ vanish at the walls?

* A. The wave equation cannot be solved there
* B. The energy is zero at the walls
* C. The potential is infinite outside, so the particle cannot be found there and ψ must be zero at x = 0 and x = L
* D. The wavefunction is always 1 at the walls

**Answer: C**


**Q3 (Apply).** What does ψ(0) = 0 imply for the constants?

* A. A = 0
* B. B = 0, leaving ψ = A sin kx
* C. A = B
* D. k = 0

**Answer: B**


**Q4 (Apply).** What does ψ(L) = 0 imply?

* A. cos kL = 0
* B. kL = 0 only
* C. sin kL = 0, so kL = nπ
* D. k = nπL

**Answer: C**


**Q5 (Analyze).** Why is n = 0 excluded as an allowed quantum number?

* A. It gives k = 0 and ψ = 0 everywhere, meaning no particle in the box
* B. It gives infinite energy
* C. It gives a wavefunction with a node at every point
* D. It violates the condition kL = nπ

**Answer: A**


### 4.3 Energy Eigenvalues (Quantisation)

*Sources: Class 6 Particle in 1D box (slides 6, 9–13); Extra Problems on 1D box*


**Q1 (Remember).** What are the allowed energies of a particle in a 1D box of width L?

* A. Eₙ = nh²/(8mL²)
* B. Eₙ = n²h/(8mL)
* C. Eₙ = h²/(8mnL²)
* D. Eₙ = n²h²/(8mL²), n = 1, 2, 3, …

**Answer: D**


**Q2 (Understand).** How does Eₙ scale with n, and what does this say about the spacing of levels?

* A. Eₙ ∝ n, so levels are equally spaced
* B. Eₙ ∝ n², so levels are not equally spaced
* C. Eₙ ∝ 1/n², so levels bunch up
* D. Eₙ is independent of n

**Answer: B**


**Q3 (Apply).** If the ground-state energy is E₁, what is the energy of the n = 3 state?

* A. 3E₁
* B. 6E₁
* C. 9E₁
* D. 27E₁

**Answer: C**


**Q4 (Analyze).** What is the energy gap E\_{n+1} − Eₙ in terms of E₁?

* A. 2nE₁
* B. (2n + 1)E₁
* C. (n + 1)E₁
* D. nE₁

**Answer: B**


**Q5 (Evaluate).** A student says the box allows any energy, as in classical mechanics. Evaluate this.

* A. Correct; any energy is allowed
* B. Correct; only the ground state is restricted
* C. Incorrect; no energy is allowed
* D. Incorrect; boundary conditions restrict energies to the discrete set Eₙ

**Answer: D**


### 4.4 Eigenfunctions and Normalisation

*Sources: Class 6 Particle in 1D box (slides 7–8); Extra Problems with solutions (P1)*


**Q1 (Remember).** What are the normalised wavefunctions for a box of width L?

* A. ψₙ(x) = √(2/L) sin(nπx/L)
* B. ψₙ(x) = (2/L) sin(nπx/L)
* C. ψₙ(x) = √(L/2) sin(nπx/L)
* D. ψₙ(x) = √(2/L) cos(nπx/L)

**Answer: A**


**Q2 (Apply).** Normalising ψ = A sin(πx/L) over 0 to L requires what value of A?

* A. A = 2/L
* B. A = √(2/L)
* C. A = √(L/2)
* D. A = 1/L

**Answer: B**


**Q3 (Apply).** What is the ground-state wavefunction for a well extending from x = 0 to x = 2L?

* A. ψ = √(2/L) sin(πx/L)
* B. ψ = √(2/L) sin(πx/2L)
* C. ψ = √(1/L) sin(2πx/L)
* D. ψ = √(1/L) sin(πx/2L)

**Answer: D**


**Q4 (Understand).** What is the relationship between Eₙ and ψₙ?

* A. Eₙ are eigenfunctions and ψₙ eigenvalues
* B. They are unrelated
* C. ψₙ are the eigenfunctions and Eₙ the corresponding eigenvalues of the Hamiltonian
* D. ψₙ = Eₙ

**Answer: C**


**Q5 (Create).** Construct the normalised ground state for a box of width a = 25 Å.

* A. ψ₁(x) = √(2/a) sin(πx/a)
* B. ψ₁(x) = √(a/2) sin(πx/a)
* C. ψ₁(x) = (2/a) cos(πx/a)
* D. ψ₁(x) = √(2/a) sin(2πx/a)

**Answer: A**


### 4.5 Zero-Point Energy and the Uncertainty Principle

*Sources: Class 6 Particle in 1D box (slides 9–11)*


**Q1 (Remember).** What is the lowest energy of the particle in the box?

* A. Zero
* B. E₀ = h²/(2mL²)
* C. Infinite
* D. E₁ = h²/(8mL²), the zero-point energy

**Answer: D**


**Q2 (Understand).** Why cannot the lowest energy be zero?

* A. Zero energy would make Δx zero
* B. Zero energy is forbidden by Newton's laws
* C. Zero energy means p = 0, so Δp = 0 and Δx → ∞, which contradicts confinement within L (Heisenberg principle)
* D. The box has no ground state

**Answer: C**


**Q3 (Apply).** Which state is the first excited state?

* A. n = 2
* B. n = 1
* C. n = 3
* D. n = 0

**Answer: A**


**Q4 (Analyze).** What happens to E₁ if the box width L is halved?

* A. It becomes half
* B. It becomes four times larger (E₁ ∝ 1/L²)
* C. It becomes twice
* D. It stays the same

**Answer: B**


**Q5 (Evaluate).** A student says confining the particle more tightly should lower its minimum energy. Evaluate this.

* A. Incorrect; tighter confinement raises the minimum energy, since E₁ ∝ 1/L²
* B. Correct; E₁ decreases with L
* C. Correct; E₁ is independent of L
* D. Incorrect; E₁ becomes negative

**Answer: A**


### 4.6 Nodes, Antinodes and Probability Density

*Sources: Class 6 Particle in 1D box (slides 11–12); Extra Problems with solutions (P3); Class 7 Problems (Problem 2)*


**Q1 (Remember).** For n = 1, 2, 3, how many nodes and antinodes does ψₙ have (nodes counted including the walls)?

* A. n = 1: 1 node, 2 antinodes; n = 2: 2 nodes, 3 antinodes; n = 3: 3 nodes, 4 antinodes
* B. n = 1: 2 nodes, 1 antinode; n = 2: 3 nodes, 2 antinodes; n = 3: 4 nodes, 3 antinodes
* C. All states have 2 nodes and 1 antinode
* D. n = 1: 0 nodes; n = 2: 1 node; n = 3: 2 nodes

**Answer: B**


**Q2 (Apply).** Following this pattern, how many nodes (including walls) does the n = 5 state have?

* A. 5
* B. 4
* C. 7
* D. 6

**Answer: D**


**Q3 (Understand).** For n = 2, what is |ψ|² at x = L/2?

* A. Maximum
* B. Equal to 2/L
* C. Zero, because there is a node at the centre
* D. Undefined

**Answer: C**


**Q4 (Apply).** For n = 2, what is the probability of finding the particle between x = 0 and x = 0.25L?

* A. 1/2
* B. 1/8
* C. 1/4
* D. 1/3

**Answer: C**


**Q5 (Apply).** For n = 1 in a box of width 25 Å, the probability of finding the electron in a 5 Å region at the centre is approximately (using |ψ|²Δx)

* A. 0.2
* B. 0.04
* C. 0.8
* D. 0.4

**Answer: D**


**Q6 (Analyze).** What does the probability density show that differs from the classical picture?

* A. Some positions (nodes) are never occupied and the most probable positions depend on the level
* B. The particle is equally likely anywhere in every state
* C. The particle is always at the centre
* D. The particle never reaches the walls' interior

**Answer: A**


### 4.7 Inferences from the Box Solution

*Sources: Class 6 Particle in 1D box (slide 13); Extra Problems on 1D box (adjacent-level problem)*


**Q1 (Remember).** Which quantity gives the spacing between adjacent levels?

* A. E\_{n+1} − Eₙ = nh²/(8mL²)
* B. E\_{n+1} − Eₙ = (2n + 1)h²/(8mL²)
* C. E\_{n+1} − Eₙ = h²/(8mL²) for all n
* D. E\_{n+1} − Eₙ = 0

**Answer: B**


**Q2 (Apply).** In units of E₁, what is the gap between n = 3 and n = 4?

* A. 5E₁
* B. 7E₁
* C. 9E₁
* D. 16E₁

**Answer: B**


**Q3 (Understand).** What happens to the spectrum for very large n?

* A. The relative spacing shrinks, approaching a continuous (classical) behaviour
* B. The levels become more widely spaced relatively
* C. The levels become equal
* D. The levels vanish

**Answer: A**


**Q4 (Analyze).** Which adjacent pair has three times the gap between n = 3 and n = 4?

* A. E₇ and E₈
* B. E₂₁ and E₂₂
* C. E₁₀ and E₁₁
* D. E₃ and E₄

**Answer: C**


**Q5 (Evaluate).** Is there an adjacent pair with twice the gap between n = 3 and n = 4?

* A. Yes; n = 6
* B. Yes; n = 7
* C. Yes; n = 13
* D. No; (2n + 1) = 14 gives no integer n

**Answer: D**


### 4.8 Numerical Problems on the 1D Box

*Sources: Class 7 Module 1 QM 1D Problems (Problems 4, 5, 8); Extra Problems on 1D box (Problem 3)*


**Q1 (Apply).** An electron in an infinite well of width 2.5 × 10⁻¹⁰ m. What are the lowest three energies?

* A. About 3 eV, 12 eV and 27 eV
* B. About 6 eV, 12 eV and 18 eV
* C. About 6 eV, 24 eV and 54 eV
* D. About 12 eV, 48 eV and 108 eV

**Answer: C**


**Q2 (Apply).** For an electron in a 1 nm well, what are the de Broglie wavelengths of the n = 1, 2, 3 states (λ = 2L/n)?

* A. 20 Å, 10 Å and 6.67 Å
* B. 10 Å, 5 Å and 3.33 Å
* C. 20 Å, 40 Å and 60 Å
* D. 2 Å, 1 Å and 0.67 Å

**Answer: A**


**Q3 (Apply).** For the 1 nm well, which energies do n = 1, 2, 3 have?

* A. About 0.38 eV, 0.76 eV and 1.14 eV
* B. About 3.8 eV, 15 eV and 34 eV
* C. About 38 eV, 150 eV and 340 eV
* D. About 0.38 eV, 1.5 eV and 3.4 eV

**Answer: D**


**Q4 (Analyze).** In a 0.2 nm well the n = 5 energy is 230 eV, giving E₁ = 9.2 eV. Why is 1 keV not an allowed level?

* A. Because 1 keV is larger than E₁
* B. n² = 1000/9.2 ≈ 108.7, which gives n ≈ 10.4, not an integer
* C. Because n must be even
* D. Because energies must be below 500 eV

**Answer: B**


**Q5 (Apply).** An electron in a 250 pm well is excited from its first to its third excited state (Eₙ ≈ 6.03 eV × n²). What energy is required?

* A. About 36.2 eV
* B. About 48.2 eV
* C. About 96.5 eV
* D. About 72.4 eV

**Answer: D**


**Q6 (Apply).** It then de-excites from n = 4 directly to n = 1. What wavelength is emitted?

* A. About 29.4 nm
* B. About 13.7 nm
* C. About 68.5 nm
* D. About 1.37 nm

**Answer: B**


**Q7 (Create).** You want an electron-in-a-box model with lowest energy about 6 eV. Which width works, using Eₙ = n²h²/8ma²?

* A. About 2.5 × 10⁻¹⁰ m
* B. About 1 × 10⁻¹⁰ m
* C. About 1 × 10⁻⁹ m
* D. About 5 × 10⁻¹⁰ m

**Answer: A**

