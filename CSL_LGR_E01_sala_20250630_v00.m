% LGR exemplificado em sala
clc, clear all, close all

%%
% g = (s+3)/(s*(s+1)*(s+2)*(s+4));
numh = [poly([-3])];
demh = [poly([0 -1 -2 -4])];
g = tf(numh,demh)
rlocus(g)
saveas(gcf,'fig-LGR-E01-sala-20250630.png')
