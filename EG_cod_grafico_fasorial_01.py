# -*- coding: utf-8 -*-
"""
Created on Thu May  1 12:06:47 2025

@author: chbeu
"""

import numpy as np
import matplotlib.pyplot as plt


# Definindo os valores para A = (-1 + j41)
x_A, y_A = -1, 41
# Definindo os valores para B = 18.16∠47.69°
r_B, theta_B = 18.16, 47.69  # Já calculado anteriormente
x_B = r_B * np.cos(np.radians(theta_B))
y_B = r_B * np.sin(np.radians(theta_B))

# Criando o gráfico para o diagrama fasorial
plt.figure(figsize=(6, 6))

# Plotando o vetor de A (-1 + j41)
plt.quiver(0, 0, x_A, y_A, angles='xy', scale_units='xy', scale=1, color="blue", label=r"$A = -1 + j41$")

# Plotando o vetor de B (18.16∠47.69°)
plt.quiver(0, 0, x_B, y_B, angles='xy', scale_units='xy', scale=1, color="red", label=r"$B = 18.16 \angle 47.69^\circ$")

# Adicionando os títulos e rótulos
plt.xlim(-50, 50)
plt.ylim(-50, 50)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginário')

# Adicionando legendas
plt.legend()

# Exibindo o gráfico
plt.title('Diagrama Fasorial')
plt.show()


#%%

# Criando o gráfico para o diagrama fasorial entre 0 e 180 graus
plt.figure(figsize=(6, 6))

# Plotando o vetor de A (-1 + j41)
plt.quiver(0, 0, x_A, y_A, angles='xy', scale_units='xy', scale=1, color="blue", label=r"$A = -1 + j41$")

# Plotando o vetor de B (18.16∠47.69°)
plt.quiver(0, 0, x_B, y_B, angles='xy', scale_units='xy', scale=1, color="red", label=r"$B = 18.16 \angle 47.69^\circ$")

# Definindo o limite de ângulos entre 0 e 180 graus
plt.xlim(-5, 15)
plt.ylim(0, 50)

# Adicionando os títulos e rótulos
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginário')

# Adicionando legendas
plt.legend()

# Exibindo o gráfico
plt.title('Diagrama Fasorial (0 a 180 graus)')
plt.savefig('fig-fasores-01.png')

plt.show()


#%%