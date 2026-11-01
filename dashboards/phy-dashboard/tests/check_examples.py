"""Independent numeric checks of the worked examples printed in the notes (run: python tests/check_examples.py)."""
import math, cmath
from fractions import Fraction as F
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def dag(A): return [[A[j][i].conjugate() if isinstance(A[j][i],complex) else A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def close(a,b,t=1e-9): return abs(a-b)<t
ok=lambda name,c: print(("PASS " if c else "FAIL ")+name)
# 1.3 dependence
d=1*(1*6-5*0)-4*(2*6-5*3)+... if False else None
import itertools
M=[[1,2,4],[2,1,5],[3,0,6]]
det=M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
ok("1.3 det=0",det==0)
ok("1.3 v3=2v1+v2",[2*a+b for a,b in zip((1,2,3),(2,1,0))]==[4,5,6])
# 1.5 null space
A=[[1,2,3],[2,4,6]]
for v in [(-2,1,0),(-3,0,1)]: ok(f"1.5 A{v}=0",all(sum(r[i]*v[i] for i in range(3))==0 for r in A))
# 2.1 orthonormal
s=1/math.sqrt(2); e=[(s,s,0),(s,-s,0),(0,0,1)]; v=(3,1,2)
c=[sum(a*b for a,b in zip(x,v)) for x in e]; ok("2.1 parseval",close(sum(x*x for x in c),14))
# 2.2 integrals
N=200000; L=1.0
def integ(f,a,b,n=N): h=(b-a)/n; return sum(f(a+(i+.5)*h) for i in range(n))*h
ok("2.2 orthog sin",abs(integ(lambda x: math.sin(math.pi*x)*math.sin(2*math.pi*x),0,1))<1e-9)
ok("2.2 norm sqrt30 x(1-x)",close(integ(lambda x: 30*(x*(1-x))**2,0,1),1,1e-6))
# 3.2 inner
a=(1,1j,2); b=(2,1,1j)
ip=lambda u,w: sum(x.conjugate()*y if isinstance(x,complex) else x*y for x,y in zip(u,w))
ok("3.2 <a|b>=2+i",close(ip(a,b),2+1j)); ok("3.2 <b|a>=2-i",close(ip(b,a),2-1j))
ok("3.2 norms 6,6",close(ip(a,a).real,6) and close(ip(b,b).real,6)); ok("3.2 schwarz",abs(ip(a,b))**2<=36)
# 3.3 outer
oa=(1,1j); ob=(2,1); O=[[oa[i]*ob[j] for j in range(2)] for i in range(2)]
ok("3.3 outer matrix",O==[[2,1],[2j,1j]]); ok("3.3 O(1,1)=(3,3i)",[O[0][0]+O[0][1],O[1][0]+O[1][1]]==[3,3j])
# 3.4 tensor
t=[x*y for x in (1,2) for y in (3,1)]; ok("3.4 tensor",t==[3,1,6,2] and sum(x*x for x in t)==50)
# 4.2
A=[[1,2],[0,1]];B=[[1,0],[3,1]]; ok("4.2 AB",mm(A,B)==[[7,2],[3,1]] and mm(B,A)==[[1,2],[3,7]])
# 4.3 hermitian
H=[[2,1-1j],[1+1j,3]]; ok("4.3 H=H†",dag(H)==H)
ok("4.3 eig 1,4",close(5**2-4*4,9) and close(((5+3)/2),4) and close(((5-3)/2),1))
u1=(-1+1j,1); u4=(1-1j,2); ok("4.3 orthogonal",close(ip(u1,u4),0))
def app(M,v): return tuple(sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M)))
ok("4.3 Hu1=u1",all(close(x,y) for x,y in zip(app(H,u1),u1))); ok("4.3 Hu4=4u4",all(close(x,4*y) for x,y in zip(app(H,u4),u4)))
# 4.4 unitary
U=[[s,s],[s,-s]]; UU=mm(dag(U),U); ok("4.4 U†U=I",all(close(UU[i][j],1 if i==j else 0) for i in range(2) for j in range(2)))
Uv=app(U,(3,4)); ok("4.4 norm 25",close(sum(x*x for x in Uv),25)); ok("4.4 Uv=(7,-1)/rt2",close(Uv[0],7*s) and close(Uv[1],-1*s))
# 4.5 projection
P=[[.5,.5],[.5,.5]]; ok("4.5 P^2=P",mm(P,P)==P); Pv=app(P,(3,1)); ok("4.5 Pv=(2,2)",Pv==(2,2)); ok("4.5 prob .8",close(ip((3,1),Pv)/10,.8))
# 5.1
A=[[2,-1j],[1j,2]]; v=(-1j,1); ok("5.1 A v=3v",all(close(x,3*y) for x,y in zip(app(A,v),v)))
v1=(1j,1); ok("5.1 eig1 v=(i,1)",all(close(x,1*y) for x,y in zip(app(A,v1),v1)))
# 5.2
sz=[[1,0],[0,-1]]; psi=(3/5,4j/5); ok("5.2 <sz>=-7/25",close(sum(abs(psi[i])**2*sz[i][i] for i in range(2)),-7/25))
# 6
X=[[0,1],[1,0]];Y=[[0,-1j],[1j,0]];Z=[[1,0],[0,-1]]
ok("6 XY=iZ",mm(X,Y)==[[1j*Z[i][j] for j in range(2)] for i in range(2)])
ok("6 Y^2=I",mm(Y,Y)==[[1,0],[0,1]])
ok("6 Y(1,i)=(1,i)",app(Y,(1,1j))==(1,1j))
# 7 commutator
A=[[0,1],[0,0]];B=[[0,0],[1,0]];AB=mm(A,B);BA=mm(B,A); ok("7 [A,B]=diag(1,-1)",[[AB[i][j]-BA[i][j] for j in range(2)] for i in range(2)]==[[1,0],[0,-1]])
ZX=mm(Z,X);XZ=mm(X,Z); ok("7 [Z,X]=2iY",[[ZX[i][j]-XZ[i][j] for j in range(2)] for i in range(2)]==[[2j*Y[i][j] for j in range(2)] for i in range(2)])
# M3 expectation example
Ex2=integ(lambda x: 30*x*x*(x*(1-x))**2,0,1); ok("M3 <x^2>=2/7",close(Ex2,2/7,1e-6))
Ep2=integ(lambda x: 30*(1-2*x)**2,0,1); ok("M3 <p2>/hbar2=10",close(Ep2,10,1e-6))
print("   dx*dp/hbar =",math.sqrt((2/7-1/4)*10))
# M4 box
h=6.626e-34; m=9.109e-31; L=0.5e-9; eV=1.602e-19
E1=h*h/(8*m*L*L); print("   E1 (0.5nm) eV=",E1/eV, " E2,E3=",4*E1/eV,9*E1/eV)
print("   lambda(2->1) nm=",1239.84/(3*E1/eV))
Pr=integ(lambda x: 2*math.sin(math.pi*x)**2,1/3,2/3); print("   P(L/3..2L/3,n=1)=",Pr," formula=",1/3+math.sqrt(3)/(2*math.pi))
dxdp=math.pi*math.sqrt(1/12-1/(2*math.pi**2)); print("   box n=1 dxdp/hbar=",dxdp)
a=1e-10; E=h*h/(8*m*a*a); print("   1 Angstrom E1 =",E,"J =",E/eV,"eV")
print("   0.25nm well E1 =",h*h/(8*m*(2.5e-10)**2)/eV)


# ---- checks added for Modules 1, 4 (sections 3.3-5) and 5 ----
def _new_checks():
    import math, itertools
    import numpy as np
    h = 6.626e-34; c = 2.998e8; e = 1.602e-19; me = 9.109e-31; k = 1.381e-23
    ok = lambda name, cond: print(("PASS  " if cond else "FAIL  ") + name) or cond
    res = []
    # Module 4: degeneracy counts
    def deg(N): return sum(1 for t in itertools.product(range(1, 12), repeat=3) if sum(x * x for x in t) == N)
    res.append(ok("degeneracy 6,9,11,12,14,17,21,27 = 3,3,3,1,6,3,6,4", [deg(n) for n in (6, 9, 11, 12, 14, 17, 21, 27)] == [3, 3, 3, 1, 6, 3, 6, 4]))
    res.append(ok("slab probability n=1,2,3 for L/4", all(abs((0.25 - math.sin(n * math.pi / 2) / (2 * n * math.pi)) - v) < 1e-3 for n, v in ((1, .091), (2, .25), (3, .303)))))
    res.append(ok("z-slab L/3, n=1 -> 0.196", abs(1 / 3 - math.sin(2 * math.pi / 3) / (2 * math.pi) - 0.196) < 1e-3))
    # Module 4: tunnelling numbers
    kap = math.sqrt(2 * me * 3 * e) / (h / 2 / math.pi)
    res.append(ok("kappa(E=2,V0=5 eV) = 8.87 /nm", abs(kap * 1e-9 - 8.87) < 0.01))
    k1 = math.sqrt(2 * me * 2 * e) / (h / 2 / math.pi)
    T12 = 16 * 0.4 * 0.6 * math.exp(-2 * kap * 0.2e-9)
    Tex = 1 / (1 + 25 * math.sinh(kap * 0.2e-9) ** 2 / (4 * 2 * 3))
    res.append(ok("T(0.2 nm): slide-12 form 0.110, exact 0.105", abs(T12 - 0.110) < 0.002 and abs(Tex - 0.105) < 0.002))
    # Module 5: gates
    X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]); H = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    I2 = np.eye(2); CN = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    res.append(ok("X,Y,Z,H unitary and square to I", all(np.allclose(U.conj().T @ U, I2) and np.allclose(U @ U, I2) for U in (X, Y, Z, H))))
    res.append(ok("Y Hermitian", np.allclose(Y, Y.conj().T)))
    res.append(ok("HZH = X", np.allclose(H @ Z @ H, X)))
    ket = lambda s: np.array([1.0 if i == int(s, 2) else 0.0 for i in range(2 ** len(s))])
    bell = {"00": [1, 0, 0, 1], "01": [0, 1, 1, 0], "10": [1, 0, 0, -1], "11": [0, 1, -1, 0]}
    res.append(ok("H then CNOT maps 00,01,10,11 to Phi+,Psi+,Phi-,Psi-", all(np.allclose(CN @ np.kron(H, I2) @ ket(s), np.array(v) / math.sqrt(2)) for s, v in bell.items())))
    res.append(ok("CNOT|10> = |11>", np.allclose(CN @ ket("10"), ket("11"))))
    a = np.array([3 / 5, 4 / 5]); Ha = H @ a
    res.append(ok("H(3/5,4/5): P = 0.98, 0.02 and HH = I", np.allclose(Ha ** 2, [0.98, 0.02]) and np.allclose(H @ Ha, a)))
    th, ph = 2 * math.pi / 3, math.pi
    res.append(ok("Bloch theta=2pi/3, phi=pi: P0 = 0.25, vector (-0.866,0,-0.5)", abs(math.cos(th / 2) ** 2 - 0.25) < 1e-9 and np.allclose([math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)], [-0.866, 0, -0.5], atol=1e-3)))
    psi = np.array([1, 1, 1, 0]) / math.sqrt(3)
    res.append(ok("(|00>+|01>+|10>)/sqrt3: P(first=0) = 2/3, entangled", abs(psi[0] ** 2 + psi[1] ** 2 - 2 / 3) < 1e-9 and abs(psi[0] * psi[3] - psi[1] * psi[2]) > 1e-3))
    # Module 1
    res.append(ok("Young: beta = 1.8 mm", abs(600e-9 * 1.5 / 0.5e-3 - 1.8e-3) < 1e-9))
    E = h * c / 400e-9 / e
    res.append(ok("photoelectric 400 nm, W0 = 2 eV: KE 1.10 eV, v 6.2e5, lambda0 620 nm", abs(E - 2 - 1.10) < 0.01 and abs(math.sqrt(2 * (E - 2) * e / me) - 6.2e5) < 1e4 and abs(h * c / (2 * e) * 1e9 - 620) < 1))
    res.append(ok("Planck avg energy (5.6e12 Hz, 330 K) ~ 2.9e-21 J", abs(h * 5.6e12 / math.expm1(h * 5.6e12 / (k * 330)) - 2.95e-21) < 0.1e-21))
    res.append(ok("de Broglie: 12.26/sqrt(400)=0.613; proton 2200 m/s = 1.80 A", abs(12.26 / 20 - 0.613) < 1e-3 and abs(h / (1.67e-27 * 2200) * 1e10 - 1.80) < 0.01))
    res.append(ok("thermal neutron 300 K: 3kT/2 -> 1.46 A, kT -> 1.78 A", abs(h / math.sqrt(3 * 1.67e-27 * k * 300) * 1e10 - 1.46) < 0.01 and abs(h / math.sqrt(2 * 1.67e-27 * k * 300) * 1e10 - 1.78) < 0.01))
    res.append(ok("normalise x(1-x): A = sqrt(30)", abs(1 / 3 - 1 / 2 + 1 / 5 - 1 / 30) < 1e-12))
    assert all(res), "a new check failed"

_new_checks()
