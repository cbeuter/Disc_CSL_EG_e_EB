# -*- coding: utf-8 -*-
"""
Created on Thu May  1 09:07:16 2025

@author: chbeu
"""

import numpy as np
import matplotlib.pyplot as plt

# Parametros da senoide
Vm = 1  # Amplitude maxima
omega = 2 * np.pi  # Frequencia angular (1 ciclo completo)
T = 2 * np.pi / omega  # Periodo da onda (1 ciclo completo)
t = np.linspace(0, T, 1000)  # Vetor de tempo (1000 pontos no intervalo de 0 a T)

# Funcao senoide
v_t = Vm * np.sin(omega * t)

# Plotando o grafico
plt.plot(t, v_t)
plt.title('Ciclo da Senoide')
plt.xlabel('Tempo (t)')
plt.ylabel('Voltagem (v(t))')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.savefig('fig-ciclo-senoide.png')

plt.show()
