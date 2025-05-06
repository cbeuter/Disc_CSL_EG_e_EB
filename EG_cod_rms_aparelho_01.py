# -*- coding: utf-8 -*-
"""
Created on Fri May  2 05:15:03 2025

@author: chbeu
"""

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
frequencia = 10  # Hz
amplitude = 1  # V
taxa_de_amostragem = 100  # Hz
tempo_de_simulacao = 1  # s

# Gera o sinal
t = np.arange(0, tempo_de_simulacao, 1 / taxa_de_amostragem)
# sinal = amplitude * np.sin(2 * np.pi * frequencia * t)
sinal = amplitude * np.cos(2 * np.pi * frequencia * t)

# Calcula o valor RMS
rms = np.sqrt(np.mean(sinal**2))

print(f"Valor RMS: {rms:.2f}")

# Plota o sinal
plt.plot(t, sinal)
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (V)")
plt.title("Sinal Senoidal")
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
frequencia = 50  # Hz
amplitude = 1  # V
taxa_de_amostragem = 10000  # Hz
tempo_de_simulacao = .02  # s

# Gera o sinal fundamental
t = np.arange(0, tempo_de_simulacao, 1 / taxa_de_amostragem)
sinal_fundamental = amplitude * np.sin(2 * np.pi * frequencia * t)

# Adiciona a 3ª harmônica
amplitude_3h = 0.25  # V
sinal_3h = amplitude_3h * np.sin(2 * np.pi * 3 * frequencia * t)

# Adiciona a 5ª harmônica
amplitude_5h = 0.15  # V
sinal_5h = amplitude_5h * np.sin(2 * np.pi * 5 * frequencia * t)

# Sinal total
sinal_total = sinal_fundamental + sinal_3h + sinal_5h

# Calcula o valor RMS
rms_fundamental = np.sqrt(np.mean(sinal_fundamental**2))
rms_total = np.sqrt(np.mean(sinal_total**2))

print("-----------------------")
print(f"Valor RMS Fundamental: {rms_fundamental:.2f}")
print(f"Valor RMS Total: {rms_total:.2f}")

# Plota os sinais
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, sinal_fundamental, label="Fundamental")
plt.plot(t, sinal_total, label="Total")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (V)")
plt.title("Sinal Fundamental e Total")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, sinal_3h, label="3ª Harmônica")
plt.plot(t, sinal_5h, label="5ª Harmônica")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (V)")
plt.title("Harmônicas")
plt.legend()

plt.tight_layout()
plt.savefig('fig-rms-harmonicas-01.png')

plt.show()

#%%
'''
Resultados
Valor RMS Fundamental: 0.71
Valor RMS Total: 0.74
'''
#%%

