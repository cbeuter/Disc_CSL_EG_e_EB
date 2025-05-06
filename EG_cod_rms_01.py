# -*- coding: utf-8 -*-
"""
Created on Thu May  1 12:33:11 2025

@author: chbeu
"""

import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o True RMS
def true_rms(signal):
    return np.sqrt(np.mean(np.square(signal)))

# Definindo o tempo e o intervalo
t = np.linspace(0, 1/60, 10000)  # 1 segundo, 10000 pontos
frequency = 60  # Frequência de 50 Hz

sine_wave = np.sin(2 * np.pi * frequency * t) # Sinal senoidal
square_wave = np.sign(np.sin(2 * np.pi * frequency * t)) # Sinal quadrado
triangle_wave = 2 * (t * frequency - np.floor(t * frequency + 0.5)) # Sinal triangular

# Cálculo do RMS simples para a senoide (para a onda senoidal, o RMS simples seria V_max / sqrt(2))
rms_sine_simple = np.max(np.abs(sine_wave)) / np.sqrt(2)

# Cálculo do True RMS para todas as ondas
rms_sine_true = true_rms(sine_wave)
rms_square_true = true_rms(square_wave)
rms_triangle_true = true_rms(triangle_wave)

# Plotando as ondas para visualização
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, label="Senoidal")
plt.title("Onda Senoidal")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, square_wave, label="Quadrada", color="r")
plt.title("Onda Quadrada")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, triangle_wave, label="Triangular", color="g")
plt.title("Onda Triangular")
plt.grid(True)

plt.tight_layout()
plt.savefig('fig-rms-01.png')

plt.show()

# Exibindo os resultados
print(f"RMS Simples da Onda Senoidal: {rms_sine_simple:.4f}")
print(f"True RMS da Onda Senoidal: {rms_sine_true:.4f}")
print(f"True RMS da Onda Quadrada: {rms_square_true:.4f}")
print(f"True RMS da Onda Triangular: {rms_triangle_true:.4f}")
