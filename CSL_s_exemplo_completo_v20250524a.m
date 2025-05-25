% Exercicio Tente Implementar 5.1 
% Coletado do livro Nise 6a edição (2011)

%% sugestao do livro
clc, clear all
G1=tf(1,[1 1]);
G2=G1;G3=G1;
H1=tf(1,[1 0]);
H2=H1;H3=H1;
System=append (G1,G2,G3,H1,H2,H3);
input = 1 ; output = 3 ;
Q = [1 -4 0 0 0
     2 1 -5 0 0
     3 2 1 -5 -6
     4 2 0 0 0
     5 2 0 0 0
     6 3 0 0 0];
T=connect(System,Q, input, output);
T=tf(T); T=minreal(T)

%{
% resultado esperado ao exercutar

               s^3 + 2 s^2
  -------------------------------------
  s^5 + 3 s^4 + 5 s^3 + 6 s^2 + 4 s + 2
%}

%% solucao do Apendice modificada por interpretacao
'Tente Implementar 5.1'
G1=tf(1,[1 1]);
G2=G1;G3=G1;
H1=tf(1,[1 0]);
H2=H1;H3=H1;
sistema=append(G1,G2,G3,H1,H2,H3);
entrada=1;saida=3;
Q = [1 -4 0 0 0
2 1 -5 0 0
3 2 1 -5 -6
4 2 0 0 0
5 2 0 0 0
6 3 0 0 0]
T=connect(sistema,Q,entrada,saida);
T=tf(T);T=minreal(T)

% mesmo resultado
%{
% resultado esperado ao exercutar

               s^3 + 2 s^2
  -------------------------------------
  s^5 + 3 s^4 + 5 s^3 + 6 s^2 + 4 s + 2
%}

%% outra forma de fazer

%% solucao do Apendice modificada com outra interpretacao
'Tente Implementar 5.1'
G1=tf(1,[1 1]); G2=G1;G3=G1; H1=tf(1,[1 0]); H2=H1;H3=H1;
G4 = 1; % adicionado uma entrada ganho 1
sistema=append(G1,G2,G3,H1,H2,H3,G4);
% entrada=1;saida=3;
entrada=7;saida=3;
Q = [1 -4  7  0  0
     2  1 -5  0  0
     3  2  1 -5 -6
     4  2  0  0  0
     5  2  0  0  0
     6  3  0  0  0
     7  0  0  0  0];
T=connect(sistema,Q,entrada,saida);
T=tf(T);T=minreal(T)

%{
resultado esperado
T =
 
               s^3 + 2 s^2
  -------------------------------------
  s^5 + 3 s^4 + 5 s^3 + 6 s^2 + 4 s + 2

%}

%% outra forma sugerida
clc; clear all
s = tf('s');
G1=s; G2=s; G3=1/s; H1=1/s; H2=s; G6=1;
T = append (G1, G2, G3, H1, H2, G6)
input=6;
output = 3
q = [ 1 -2 -4 -5 6;
      2 1 0 0 0 
      3 2 4 0 0
      4 -2 -4 -5 6;
      5 3 0 0 0
      6 0 0 0 0];  % este a mais nao interfere
Ts = connect(T, q, input, output);
T = tf(Ts)
minreal(T)
minreal(T)*2/2

%{
 
  0.5 s^3 + 2.776e-15 s^2 - 6.661e-16 s + 0.5
  -------------------------------------------
       s^4 + 3.109e-15 s^3 + 0.5 s^2 + s
 
Que poderia ser simplificado e interpresentado como
 
     0.5 s^3 + 0.5                 2
  ---------------------  x      ---------
      s^4 + 0.5 s^2 + s            2

  s^3 + 1
  ----------------
  2s^4 + s^2 + 2s

Depois de eliminado os valores muito baixos
%}
[num, den] = tfdata(T, 'v');
tolerance = 1e-6;
num_clean = num .* (abs(num) > tolerance);
den_clean = den .* (abs(den) > tolerance);
sys_clean = tf(num_clean, den_clean);
sys_clean
sys_clean*2/2

%{
% limpo

       s^3 + 1
  -----------------
  2 s^4 + s^2 + 2 s

%}

%%
clc, clear all
G1=tf([0 1],[1 7]); %G1=1/s+7 input transducer
G2=tf([0 0 1],[1 2 3]); %G2=1/s^2+2s+3
G3=tf([0 1],[1 4]); %G3=1/s+4
G4=tf([0 1],[1 0]); %G4=1/s
G5=tf([0 5],[1 7]); %G5=5/s+7
G6=tf([0 0 1],[1 5 10]); %G6=1/s^2+5s+10
G7=tf([0 3],[1 2]); %G7=3/s+2
G8=tf([0 1],[1 6]); %G8=1/s+6
G9=tf([1],[1]); %Add G9=1 transducer at the input
T1=append(G1,G2,G3,G4,G5,G6,G7,G8,G9);
Q=[1 -2 -5 9
2 1 8 0
3 1 8 0
4 1 8 0
5 3 4 -6
6 7 0 0
7 3 4 -6
8 7 0 0];
inputs=9;
outputs=7;
Ts=connect(T1,Q,inputs,outputs);
T=tf(Ts)


%{
% Resultado esperado

 6 s^7 + 132 s^6 + 1176 s^5 + 5640 s^4 + 1.624e04 s^3 + 2.857e04 s^2 + 2.988e04 s + 1.512e04
 ----------------------------------------------------------------------------------
 s^10 + 33 s^9 + 466 s^8 + 3720 s^7 + 1.867e04 s^6 + 6.182e04 s^5 + 1.369e05 s^4 + 1.981e05 s^3 + 1.729e05 s^2 + 6.737e04 s - 1.044e04

%}
%%