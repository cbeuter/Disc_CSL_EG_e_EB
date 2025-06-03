% Experimente 5.2
% p.203 do Nise 7a Edicao

clear all
%%
a=2;
nung=16;
deng=poly([0 -a]);
G=tf(nung,deng);
T=feedback(G,1);
[numt,dent]= tfdata(T,'v');
wn = sqrt(dent(3))
z=dent(2)/(2*wn)
Ts=4/(z*wn)
Tp=pi/(wn*sqrt(1-z^2))
pos=exp(-z*pi/sqrt(1-z^2))*100
Tr=(1.76*z^3-0.417*z^2+1.039*z+1)/wn
step(T)
