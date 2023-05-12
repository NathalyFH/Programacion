syms LC1 LC2 L1 L2 q1(t) q2(t) m1 m2 I1 I2
g =  9.81
qp1 = diff(q1,t)
qp2 = diff(q2,t)
x1 = LC1*sin(q1)
y1 = -LC1*cos(q1)


vx1 = diff(x1)
vy1 = diff(y1)

v1squared = vx1^2+vy1^2

x2 = L1*sin(q1)+LC2*sin(q1+q2)
y2 = -L1*cos(q1)-LC2*cos(q1+q2)

vx2 = diff(x2)
vy2 = diff(y2)

v2squared = vx2^2+vy2^2
EC = 1/2*(m1*v1squared +I1*diff(q1)^2 + m2*v2squared+I2*(diff(q1)+diff(q2))^2)
h1 = LC1*(1-cos(q1))
h2 = L1*(1-cos(q1))+LC2*(1-cos(q1+q2))

EP = g*(m1*h1 +m2*h2)


L = EC-EP

dLdq1p = diff(L,diff(q1))
dL1dt = diff(dLdq1p,t)

dLdq2p = diff(L,diff(q2))
dL2dt = diff(dLdq2p,t)


dLdq1 = diff(L, q1)
dLdq2 = diff(L, q2)


T1 = simplify(dL1dt - dLdq1)
T2 = simplify(dL2dt-dLdq2)
