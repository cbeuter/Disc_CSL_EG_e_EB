# -*- coding: utf-8 -*-
"""
Created on Thu May  1 13:43:29 2025

@author: chbeu
"""

import numpy as np
import matplotlib.pyplot as plt

# Funcao para calcular o True RMS
def true_rms(signal):
    return np.sqrt(np.mean(np.square(signal)))

# Definindo o tempo e o intervalo
t = np.linspace(0, 1/60, 10000)  # 1 segundo, 10000 pontos
frequencia = 60  # Frequencia de 60 Hz

# Gerando as ondas principais
onda_senoidal = np.sin(2 * np.pi * frequencia * t)  # Sinal senoidal
onda_quadrada = np.sign(np.sin(2 * np.pi * frequencia * t))  # Sinal quadrado
onda_triangular = 2 * (t * frequencia - np.floor(t * frequencia + 0.5))  # Sinal triangular

# Gerando o ruido aleatorio
ruido = np.abs(np.random.normal(0, 0.15, len(t)))  # Ruido com media 0 e desvio padrao 0.5

# Somando o ruido as ondas principais
onda_senoidal_com_ruido = onda_senoidal + ruido
onda_quadrada_com_ruido = onda_quadrada + ruido
onda_triangular_com_ruido = onda_triangular + ruido

# Calculo do True RMS para as ondas principais
rms_senoidal_true = true_rms(onda_senoidal)
rms_quadrada_true = true_rms(onda_quadrada)
rms_triangular_true = true_rms(onda_triangular)

# Calculo do True RMS para as ondas com ruido
rms_senoidal_com_ruido = true_rms(onda_senoidal_com_ruido)
rms_quadrada_com_ruido = true_rms(onda_quadrada_com_ruido)
rms_triangular_com_ruido = true_rms(onda_triangular_com_ruido)

# Plotando as ondas para visualizacao
plt.figure(figsize=(10, 12))

# Onda Senoidal com ruido
plt.subplot(3, 1, 1)
plt.plot(t, onda_senoidal, label='Senoidal Original', color='b')
plt.plot(t, onda_senoidal_com_ruido, label='Senoidal com Ruido', color='orange')
plt.title('Onda Senoidal com Ruido')
plt.grid(True)

# Onda Quadrada com ruido
plt.subplot(3, 1, 2)
plt.plot(t, onda_quadrada, label='Quadrada Original', color='r')
plt.plot(t, onda_quadrada_com_ruido, label='Quadrada com Ruido', color='purple')
plt.title('Onda Quadrada com Ruido')
plt.grid(True)

# Onda Triangular com ruido
plt.subplot(3, 1, 3)
plt.plot(t, onda_triangular, label='Triangular Original', color='g')
plt.plot(t, onda_triangular_com_ruido, label='Triangular com Ruido', color='brown')
plt.title('Onda Triangular com Ruido')
plt.grid(True)

plt.tight_layout()
plt.savefig('fig-rms-ruido.png')

# Exibindo o grafico
plt.show()

# Exibindo os resultados
print(f'True RMS da Onda Senoidal: {rms_senoidal_true:.4f}')
print(f'True RMS da Onda Quadrada: {rms_quadrada_true:.4f}')
print(f'True RMS da Onda Triangular: {rms_triangular_true:.4f}')

print(f'True RMS da Onda Senoidal com Ruido: {rms_senoidal_com_ruido:.4f}')
print(f'True RMS da Onda Quadrada com Ruido: {rms_quadrada_com_ruido:.4f}')
print(f'True RMS da Onda Triangular com Ruido: {rms_triangular_com_ruido:.4f}')	