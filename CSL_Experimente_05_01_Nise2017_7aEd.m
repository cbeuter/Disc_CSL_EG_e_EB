% Experimente 5.1
% Nise 7a edicao p. 201

G1=tf(1,[1 1]);
G2=G1;G3=G1;
H1=tf(1,[1 0]);
H2=H1;H3=H1;
System=append (G1,G2,G3,H1,H2,H3);
input=1; output=3;
Q=[1 -4 0 0 0
   2 1 -5 0 0
   3 2 1 -5 -6
   4 2 0 0 0
   5 2 0 0 0
   6 3 0 0 0];
T=connect (System, Q,input,output);
T=tf(T);T=minreal(T)

syms s
[num, den] = tfdata(T);
eqn_top = poly2sym(num,s);
eqn_bot = poly2sym(den,s);
result = eqn_top/eqn_bot

pretty(result)
