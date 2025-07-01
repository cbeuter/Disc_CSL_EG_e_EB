# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 20:06:01 2025

@author: CB
"""


import numpy as np
import matplotlib.pyplot as plt

# Definindo parâmetros
V = 1  # Amplitude das tensões
omega = 2 * np.pi  # Frequência angular (assumindo 1 Hz para simplificação)
t = np.linspace(0, 2, 1000)  # Tempo de 0 a 2 segundos (2 períodos)

# Calculando as tensões em cada fase
v_a = V * np.sin(omega * t)
v_b = V * np.sin(omega * t - 2 * np.pi / 3)
v_c = V * np.sin(omega * t + 2 * np.pi / 3)

# Plotando o gráfico das tensões
plt.figure(figsize=(10, 6))
plt.plot(t, v_a, label=r'$v_a(t)$', color='blue')
plt.plot(t, v_b, label=r'$v_b(t)$', color='red')
plt.plot(t, v_c, label=r'$v_c(t)$', color='green')

# Adicionando títulos e rótulos
#plt.title("Tensões Trifásicas no Domínio do Tempo", fontsize=14)
plt.xlabel("Tempo (s)", fontsize=12)
plt.ylabel("Tensão (V)", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()

#%%

# Definindo as tensões fasoriais para o diagrama de fase e neutro
V_a_fasor = V * np.exp(1j * 0)  # V_a na fase 0º
V_b_fasor = V * np.exp(1j * -2 * np.pi / 3)  # V_b na fase -120º
V_c_fasor = V * np.exp(1j * 2 * np.pi / 3)  # V_c na fase +120º

# Calculando as tensões entre as fases (fase-fase)
V_ab_fasor = V_a_fasor - V_b_fasor  # V_ab = V_a - V_b
V_bc_fasor = V_b_fasor - V_c_fasor  # V_bc = V_b - V_c
V_ca_fasor = V_c_fasor - V_a_fasor  # V_ca = V_c - V_a

# Plotando o diagrama fasorial
plt.figure(figsize=(8, 8))

# Diagrama de fase e neutro
plt.quiver(0, 0, np.real(V_a_fasor), np.imag(V_a_fasor), angles='xy', scale_units='xy', scale=1, color='blue', label=r'$V_a$')
plt.quiver(0, 0, np.real(V_b_fasor), np.imag(V_b_fasor), angles='xy', scale_units='xy', scale=1, color='red', label=r'$V_b$')
plt.quiver(0, 0, np.real(V_c_fasor), np.imag(V_c_fasor), angles='xy', scale_units='xy', scale=1, color='green', label=r'$V_c$')

# Diagrama de fase e fase
plt.quiver(0, 0, np.real(V_ab_fasor), np.imag(V_ab_fasor), angles='xy', scale_units='xy', scale=1, color='purple', label=r'$V_{ab}$')
plt.quiver(0, 0, np.real(V_bc_fasor), np.imag(V_bc_fasor), angles='xy', scale_units='xy', scale=1, color='orange', label=r'$V_{bc}$')
plt.quiver(0, 0, np.real(V_ca_fasor), np.imag(V_ca_fasor), angles='xy', scale_units='xy', scale=1, color='brown', label=r'$V_{ca}$')

# Ajustando o gráfico
plt.xlim(-1.5, 2.2)
plt.ylim(-2.0, 1.2)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
# plt.title("Diagrama Fasorial das Tensões Trifásicas", fontsize=14)
plt.xlabel("Parte Real", fontsize=12)
plt.ylabel("Parte Imaginária", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True)
plt.tight_layout()

# Exibindo o gráfico
plt.show()

#%%


import matplotlib.pyplot as plt
import numpy as np

# Definindo a fase dos sinais
theta = 0
V_an = 1  # Tensão de linha para o primeiro ponto
V_bn = 1  # Tensão de linha para o segundo ponto
V_cn = 1  # Tensão de linha para o terceiro ponto

# Impedância, considerando a impedância unitária para simplificação
Z_a = 1
Z_b = 1
Z_c = 1

# Correntes para cada fase
I_a_angle = theta  # Fase de A
I_b_angle = theta + 120  # Fase de B
I_c_angle = theta - 120  # Fase de C

I_a = V_an / Z_a * np.exp(1j * np.radians(I_a_angle))
I_b = V_bn / Z_b * np.exp(1j * np.radians(I_b_angle))
I_c = V_cn / Z_c * np.exp(1j * np.radians(I_c_angle))

# Plotando o diagrama fasorial
plt.figure(figsize=(6, 6))

# Fazendo os vetores das correntes
plt.quiver(0, 0, np.real(I_a), np.imag(I_a), angles='xy', scale_units='xy', scale=1, color='r', label='$I_a$')
plt.quiver(0, 0, np.real(I_b), np.imag(I_b), angles='xy', scale_units='xy', scale=1, color='g', label='$I_b$')
plt.quiver(0, 0, np.real(I_c), np.imag(I_c), angles='xy', scale_units='xy', scale=1, color='b', label='$I_c$')

# Trazendo as linhas para o gráfico
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

# Adicionando a legenda
plt.legend()

# Adicionando título
# plt.title('Diagrama Fasorial - Circuito Elétrico Trifásico com Ligação em Estrela')

# Mostrando o gráfico
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()

#%%

# Dados fornecidos
V_LN = 380  # Tensão de linha em volts
Z = 15 * np.exp(1j * np.radians(30))  # Impedância de cada fase (15 < 30°)
I_L = V_LN / Z  # Corrente de linha

# Tensões de fase (igual à tensão de linha em um sistema \Delta)
V_A = V_LN * np.exp(1j * np.radians(0))  # Fase A, com ângulo 0°
V_B = V_LN * np.exp(1j * np.radians(-120))  # Fase B, com ângulo -120°
V_C = V_LN * np.exp(1j * np.radians(120))  # Fase C, com ângulo +120°

# Correntes de linha (iguais às tensões de fase, pois a ligação é em \Delta)
I_A = I_L * np.exp(1j * np.radians(0))  # Corrente na fase A
I_B = I_L * np.exp(1j * np.radians(-120))  # Corrente na fase B
I_C = I_L * np.exp(1j * np.radians(120))  # Corrente na fase C

# Preparando os dados para o gráfico fasorial
tensoes = [V_A, V_B, V_C]
correntes = [I_A, I_B, I_C]
labels_tensao = ['$V_A$', '$V_B$', '$V_C$']
labels_corrente = ['$I_A$', '$I_B$', '$I_C$']

# Plotando o diagrama fasorial completo
plt.figure(figsize=(8, 8))

# Plotando as tensões
for i in range(3):
    plt.quiver(0, 0, np.real(tensoes[i]), np.imag(tensoes[i]), angles='xy', scale_units='xy', scale=1, label=labels_tensao[i], color='b')

# Plotando as correntes
for i in range(3):
    plt.quiver(0, 0, np.real(correntes[i]), np.imag(correntes[i]), angles='xy', scale_units='xy', scale=1, label=labels_corrente[i], color='r')

# Ajustando os limites do gráfico
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

# Adicionando a legenda
plt.legend()

# Título do gráfico
plt.title('Diagrama Fasorial - Tensão e Corrente de uma Carga Trifásica em Delta')

# Mostrando o gráfico
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()


#%%

from sympy import symbols, I, exp, pi

# Definindo as variáveis simbólicas
V_ab, V_bc, V_ca = symbols('V_ab V_bc V_ca')  # Tensão entre as fases
Z_ab, Z_bc, Z_ca = symbols('Z_ab Z_bc Z_ca')  # Impedâncias
theta = symbols('theta')  # Ângulo de fase

# Correntes de linha com as fases indicadas
I_ab = (V_ab / Z_ab) * exp(I * theta)  # Corrente I_ab
I_bc = (V_bc / Z_bc) * exp(I * (theta + 2*pi/3))  # Corrente I_bc
I_ca = (V_ca / Z_ca) * exp(I * (theta - 2*pi/3))  # Corrente I_ca

# Correntes de fase
I_a = I_ab - I_ca
I_b = I_bc - I_ab
I_c = I_ca - I_bc

I_a, I_b, I_c  # Resultados simbólicos das correntes de fase


#---
from sympy import symbols, I, exp, pi

# Definindo as variáveis simbólicas
V_ab, V_bc, V_ca = symbols('V_ab V_bc V_ca')  # Tensão entre as fases
Z_ab, Z_bc, Z_ca = symbols('Z_ab Z_bc Z_ca')  # Impedâncias
theta = symbols('theta')  # Ângulo de fase

# Correntes de linha com as fases indicadas
I_ab = (V_ab / Z_ab) * exp(I * theta)  # Corrente I_ab
I_bc = (V_bc / Z_bc) * exp(I * (theta + 2*pi/3))  # Corrente I_bc
I_ca = (V_ca / Z_ca) * exp(I * (theta - 2*pi/3))  # Corrente I_ca

# Correntes de fase
I_a = I_ab - I_ca
I_b = I_bc - I_ab
I_c = I_ca - I_bc

I_a, I_b, I_c  # Resultados simbólicos das correntes de fase

#%%


import matplotlib.pyplot as plt
import numpy as np

def plot_phasor(ax, magnitude, angle_deg, color, label_text, line_style='-', is_voltage=False):
    """
    Função para plotar um fasor.
    ax: o objeto Axes do matplotlib
    magnitude: a magnitude do fasor
    angle_deg: o ângulo do fasor em graus
    color: a cor do fasor
    label_text: o rótulo para o fasor (e.g., '$V_{AB}$')
    line_style: estilo da linha (e.g., '-', '--')
    is_voltage: Booleano para indicar se é uma tensão (ajusta o sufixo no rótulo)
    """
    angle_rad = np.deg2rad(angle_deg)
    x = magnitude * np.cos(angle_rad)
    y = magnitude * np.sin(angle_rad)

    # Ajuste dinâmico para head_width e head_length baseado na magnitude máxima para melhor proporção
    # Para tensões, use um valor maior; para correntes, um valor menor.
    if is_voltage:
        head_width = 0.02 * ax.get_xlim()[1] # % do alcance do eixo
        head_length = 0.03 * ax.get_xlim()[1]
    else:
        head_width = 0.03 * ax.get_xlim()[1] # % do alcance do eixo
        head_length = 0.04 * ax.get_xlim()[1]

    ax.arrow(0, 0, x, y, head_width=head_width, head_length=head_length, fc=color, ec=color, linestyle=line_style, linewidth=1.5)

    # Formatação do texto do rótulo
    unit = 'V' if is_voltage else 'A'
    full_label = f'{label_text}\n{magnitude:.2f}{unit} $\\angle${angle_deg}°'

    # Posição do texto com um offset para evitar sobreposição com a seta e o fasor
    # Ajuste o offset de acordo com a magnitude e a legibilidade
    offset_factor = 1.15 if is_voltage else 1.3 # Maior offset para correntes para evitar colisões
    text_x = magnitude * np.cos(angle_rad) * offset_factor
    text_y = magnitude * np.sin(angle_rad) * offset_factor

    # Ajustes para o alinhamento do texto dependendo do quadrante
    ha = 'center'
    va = 'center'
    if 45 <= angle_deg < 135: # Acima (1º e 2º quadrantes superior)
        va = 'bottom'
    elif 135 <= angle_deg < 225: # Esquerda (2º e 3º quadrantes)
        ha = 'right'
    elif 225 <= angle_deg < 315: # Abaixo (3º e 4º quadrantes inferior)
        va = 'top'
    else: # Direita (0-45, 315-360, 4º e 1º quadrantes)
        ha = 'left'

    ax.text(text_x, text_y, full_label, color=color, ha=ha, va=va, fontsize=9)


# --- Dados do Sistema ---
# Tensões Fase-Fase (V)
V_AB_mag = 380
V_AB_ang = 0
V_BC_mag = 380
V_BC_ang = -120 # Ou 240
V_CA_mag = 380
V_CA_ang = 120

# Correntes de Fase (A)
I_AB_mag = 25.33
I_AB_ang = -30
I_BC_mag = 25.33
I_BC_ang = -150
I_CA_mag = 25.33
I_CA_ang = 90

# Correntes de Linha (A)
I_A_mag = 43.87
I_A_ang = -60
I_B_mag = 43.87
I_B_ang = -180
I_C_mag = 43.87
I_C_ang = 60

# --- Configuração do Plot ---
fig, ax = plt.subplots(figsize=(10, 10))

# Adicionar os fasores de Tensão
plot_phasor(ax, V_AB_mag, V_AB_ang, 'blue', '$V_{AB}$', is_voltage=True)
plot_phasor(ax, V_BC_mag, V_BC_ang, 'blue', '$V_{BC}$', is_voltage=True)
plot_phasor(ax, V_CA_mag, V_CA_ang, 'blue', '$V_{CA}$', is_voltage=True)

# Adicionar os fasores de Corrente de Fase (linha tracejada para diferenciar)
plot_phasor(ax, I_AB_mag, I_AB_ang, 'green', '$I_{AB}$', line_style='--')
plot_phasor(ax, I_BC_mag, I_BC_ang, 'green', '$I_{BC}$', line_style='--')
plot_phasor(ax, I_CA_mag, I_CA_ang, 'green', '$I_{CA}$', line_style='--')

# Adicionar os fasores de Corrente de Linha
plot_phasor(ax, I_A_mag, I_A_ang, 'red', '$I_{A}$')
plot_phasor(ax, I_B_mag, I_B_ang, 'red', '$I_{B}$')
plot_phasor(ax, I_C_mag, I_C_ang, 'red', '$I_{C}$')

# Configurações adicionais do plot
max_magnitude_volt = max(V_AB_mag, V_BC_mag, V_CA_mag)
max_magnitude_amp = max(I_A_mag, I_B_mag, I_C_mag)
# Define o limite máximo para os eixos baseado na maior magnitude de tensão
# e adiciona uma margem para os rótulos.
plot_lim = max_magnitude_volt * 1.5
ax.set_xlim([-plot_lim, plot_lim])
ax.set_ylim([-plot_lim, plot_lim])

ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_title('Diagrama Fasorial do Sistema Trifásico em $\\Delta$', fontsize=16)
ax.set_xlabel('Componente Real', fontsize=12)
ax.set_ylabel('Componente Imaginária', fontsize=12)

# Desenhar eixos cartesianos
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)

# Mostrar o plot
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

def plot_phasor(ax, magnitude, angle_deg, color, label_text, unit, line_style='-', is_main_phasor=True):
    """
    Função para plotar um fasor.
    ax: o objeto Axes do matplotlib
    magnitude: a magnitude do fasor
    angle_deg: o ângulo do fasor em graus
    color: a cor do fasor
    label_text: o rótulo para o fasor (e.g., '$V_{AB}$')
    unit: a unidade do fasor ('V' ou 'A')
    line_style: estilo da linha (e.g., '-', '--')
    is_main_phasor: Booleano para ajustar o tamanho da seta e do texto
    """
    angle_rad = np.deg2rad(angle_deg)
    x = magnitude * np.cos(angle_rad)
    y = magnitude * np.sin(angle_rad)

    # Ajuste dinâmico para head_width e head_length baseado na magnitude máxima para melhor proporção
    # e se é um fasor "principal" (e.g., linha sólida) ou secundário (e.g., tracejado)
    if is_main_phasor:
        head_width_factor = 0.025
        head_length_factor = 0.04
        text_offset_factor = 1.2
        fontsize = 10
    else: # Para fasores secundários (correntes de fase)
        head_width_factor = 0.02
        head_length_factor = 0.03
        text_offset_factor = 1.35 # Maior offset para evitar sobreposição com correntes de linha
        fontsize = 9

    # Use o limite maior do eixo para calcular o tamanho da seta
    max_axis_limit = max(abs(ax.get_xlim()[0]), abs(ax.get_xlim()[1]))
    head_width = head_width_factor * max_axis_limit
    head_length = head_length_factor * max_axis_limit

    ax.arrow(0, 0, x, y, head_width=head_width, head_length=head_length, fc=color, ec=color, linestyle=line_style, linewidth=1.5)

    # Formatação do texto do rótulo
    full_label = f'{label_text}\n{magnitude:.2f}{unit} $\\angle${angle_deg}°'

    # Posição do texto com um offset para evitar sobreposição com a seta e o fasor
    text_x = magnitude * np.cos(angle_rad) * text_offset_factor
    text_y = magnitude * np.sin(angle_rad) * text_offset_factor

    # Ajustes para o alinhamento do texto dependendo do quadrante
    ha = 'center'
    va = 'center'
    # Arredondar o ângulo para evitar problemas de ponto flutuante em limites de quadrante
    angle_deg_rounded = angle_deg % 360
    if angle_deg_rounded < 0:
        angle_deg_rounded += 360

    if 45 <= angle_deg_rounded < 135: # Acima (1º e 2º quadrantes superior)
        va = 'bottom'
    elif 135 <= angle_deg_rounded < 225: # Esquerda (2º e 3º quadrantes)
        ha = 'right'
    elif 225 <= angle_deg_rounded < 315: # Abaixo (3º e 4º quadrantes inferior)
        va = 'top'
    else: # Direita (0-45, 315-360, 4º e 1º quadrantes)
        ha = 'left'

    ax.text(text_x, text_y, full_label, color=color, ha=ha, va=va, fontsize=fontsize)


# --- Dados do Sistema ---
# Tensões Fase-Fase (V)
V_AB_mag = 380
V_AB_ang = 0
V_BC_mag = 380
V_BC_ang = -120 # Ou 240
V_CA_mag = 380
V_CA_ang = 120

# Correntes de Fase (A)
I_AB_mag = 25.33
I_AB_ang = -30
I_BC_mag = 25.33
I_BC_ang = -150
I_CA_mag = 25.33
I_CA_ang = 90

# Correntes de Linha (A)
I_A_mag = 43.87
I_A_ang = -60
I_B_mag = 43.87
I_B_ang = -180
I_C_mag = 43.87
I_C_ang = 60

# --- GRÁFICO DE TENSÕES ---
fig_V, ax_V = plt.subplots(figsize=(8, 8))

# Adicionar os fasores de Tensão
plot_phasor(ax_V, V_AB_mag, V_AB_ang, 'blue', '$V_{AB}$', 'V', is_main_phasor=True)
plot_phasor(ax_V, V_BC_mag, V_BC_ang, 'blue', '$V_{BC}$', 'V', is_main_phasor=True)
plot_phasor(ax_V, V_CA_mag, V_CA_ang, 'blue', '$V_{CA}$', 'V', is_main_phasor=True)

# Configurações adicionais do plot de Tensão
max_magnitude_volt = max(V_AB_mag, V_BC_mag, V_CA_mag)
plot_lim_V = max_magnitude_volt * 1.5 # Adiciona margem para rótulos
ax_V.set_xlim([-plot_lim_V, plot_lim_V])
ax_V.set_ylim([-plot_lim_V, plot_lim_V])
ax_V.set_aspect('equal', adjustable='box')
ax_V.grid(True, linestyle=':', alpha=0.7)
# ax_V.set_title('Diagrama Fasorial das Tensões de Linha', fontsize=16)
ax_V.set_xlabel('Componente Real (V)', fontsize=12)
ax_V.set_ylabel('Componente Imaginária (V)', fontsize=12)
ax_V.axhline(0, color='gray', linewidth=0.5)
ax_V.axvline(0, color='gray', linewidth=0.5)

# --- GRÁFICO DE CORRENTES ---
fig_I, ax_I = plt.subplots(figsize=(8, 8))

# Adicionar os fasores de Corrente de Fase (linha tracejada para diferenciar)
plot_phasor(ax_I, I_AB_mag, I_AB_ang, 'green', '$I_{AB}$', 'A', line_style='--', is_main_phasor=False)
plot_phasor(ax_I, I_BC_mag, I_BC_ang, 'green', '$I_{BC}$', 'A', line_style='--', is_main_phasor=False)
plot_phasor(ax_I, I_CA_mag, I_CA_ang, 'green', '$I_{CA}$', 'A', line_style='--', is_main_phasor=False)

# Adicionar os fasores de Corrente de Linha
plot_phasor(ax_I, I_A_mag, I_A_ang, 'red', '$I_{A}$', 'A', is_main_phasor=True)
plot_phasor(ax_I, I_B_mag, I_B_ang, 'red', '$I_{B}$', 'A', is_main_phasor=True)
plot_phasor(ax_I, I_C_mag, I_C_ang, 'red', '$I_{C}$', 'A', is_main_phasor=True)

# Configurações adicionais do plot de Corrente
max_magnitude_amp = max(I_A_mag, I_B_mag, I_C_mag)
plot_lim_I = max_magnitude_amp * 1.5 # Adiciona margem para rótulos
ax_I.set_xlim([-plot_lim_I, plot_lim_I])
ax_I.set_ylim([-plot_lim_I, plot_lim_I])
ax_I.set_aspect('equal', adjustable='box')
ax_I.grid(True, linestyle=':', alpha=0.7)
# ax_I.set_title('Diagrama Fasorial das Correntes (Fase e Linha)', fontsize=16)
ax_I.set_xlabel('Componente Real (A)', fontsize=12)
ax_I.set_ylabel('Componente Imaginária (A)', fontsize=12)
ax_I.axhline(0, color='gray', linewidth=0.5)
ax_I.axvline(0, color='gray', linewidth=0.5)

# Mostrar todos os plots
plt.tight_layout() # Ajusta o layout para evitar sobreposição de títulos/rótulos
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np

def plot_phasor(ax, magnitude, angle_deg, color, label_text, unit, line_style='-', is_main_phasor=True):
    """
    Função para plotar um fasor.
    ax: o objeto Axes do matplotlib
    magnitude: a magnitude do fasor
    angle_deg: o ângulo do fasor em graus
    color: a cor do fasor
    label_text: o rótulo para o fasor (e.g., '$V_{AN}$')
    unit: a unidade do fasor ('V' ou 'A')
    line_style: estilo da linha (e.g., '-', '--')
    is_main_phasor: Booleano para ajustar o tamanho da seta e do texto (maior para principais)
    """
    angle_rad = np.deg2rad(angle_deg)
    x = magnitude * np.cos(angle_rad)
    y = magnitude * np.sin(angle_rad)

    # Ajuste dinâmico para head_width e head_length baseado nos limites do eixo
    # e se é um fasor "principal" (e.g., linha sólida) ou secundário (e.g., tracejado)
    if is_main_phasor:
        head_width_factor = 0.025
        head_length_factor = 0.04
        text_offset_factor = 1.15
        fontsize = 10
    else: # Para fasores secundários (correntes de fase ou tensões fase-neutro se as de fase-fase forem as principais)
        head_width_factor = 0.02
        head_length_factor = 0.03
        text_offset_factor = 1.35 # Maior offset para evitar sobreposição
        fontsize = 9

    max_axis_limit = max(abs(ax.get_xlim()[0]), abs(ax.get_xlim()[1]))
    head_width = head_width_factor * max_axis_limit
    head_length = head_length_factor * max_axis_limit

    ax.arrow(0, 0, x, y, head_width=head_width, head_length=head_length, fc=color, ec=color, linestyle=line_style, linewidth=1.5)

    # Formatação do texto do rótulo
    full_label = f'{label_text}\n{magnitude:.2f}{unit} $\\angle${angle_deg}°'

    # Posição do texto com um offset para evitar sobreposição
    text_x = magnitude * np.cos(angle_rad) * text_offset_factor
    text_y = magnitude * np.sin(angle_rad) * text_offset_factor

    # Ajustes para o alinhamento do texto dependendo do quadrante
    ha = 'center'
    va = 'center'
    angle_deg_rounded = angle_deg % 360
    if angle_deg_rounded < 0:
        angle_deg_rounded += 360

    if 45 <= angle_deg_rounded < 135: # Acima (1º e 2º quadrantes superior)
        va = 'bottom'
    elif 135 <= angle_deg_rounded < 225: # Esquerda (2º e 3º quadrantes)
        ha = 'right'
    elif 225 <= angle_deg_rounded < 315: # Abaixo (3º e 4º quadrantes inferior)
        va = 'top'
    else: # Direita (0-45, 315-360, 4º e 1º quadrantes)
        ha = 'left'

    ax.text(text_x, text_y, full_label, color=color, ha=ha, va=va, fontsize=fontsize)


# --- Dados do Sistema (Conexão Estrela) ---
# Tensões Fase-Fase (V_LL = 380V)
V_LL = 380
V_phase = V_LL / np.sqrt(3) # Tensão fase-neutro

# Tensões Fase-Neutro (V) - V_AN como referência 0 deg
V_AN_mag = V_phase
V_AN_ang = 0
V_BN_mag = V_phase
V_BN_ang = -120
V_CN_mag = V_phase
V_CN_ang = 120

# Tensões Fase-Fase (V) - baseadas em V_AN = 0 deg
V_AB_mag = V_LL
V_AB_ang = 30 # V_AB = V_AN - V_BN, adiantado de V_AN em 30 graus
V_BC_mag = V_LL
V_BC_ang = -90 # V_BC = V_BN - V_CN, adiantado de V_BN em 30 graus
V_CA_mag = V_LL
V_CA_ang = 150 # V_CA = V_CN - V_AN, adiantado de V_CN em 30 graus

# Impedância de Fase
Z_p_mag = 15.0
Z_p_ang = 30 # Atraso de 30 graus (indutivo)

# Correntes de Linha (que são iguais às correntes de fase em Y)
# I_A = V_AN / Z_p
I_A_mag = V_phase / Z_p_mag
I_A_ang = V_AN_ang - Z_p_ang # 0 - 30 = -30
I_B_mag = V_phase / Z_p_mag
I_B_ang = V_BN_ang - Z_p_ang # -120 - 30 = -150
I_C_mag = V_phase / Z_p_mag
I_C_ang = V_CN_ang - Z_p_ang # 120 - 30 = 90

# --- GRÁFICO DE TENSÕES ---
fig_V, ax_V = plt.subplots(figsize=(9, 9))

# Adicionar os fasores de Tensão Fase-Neutro (em azul claro, linha tracejada)
plot_phasor(ax_V, V_AN_mag, V_AN_ang, 'skyblue', '$V_{AN}$', 'V', line_style='--', is_main_phasor=False)
plot_phasor(ax_V, V_BN_mag, V_BN_ang, 'skyblue', '$V_{BN}$', 'V', line_style='--', is_main_phasor=False)
plot_phasor(ax_V, V_CN_mag, V_CN_ang, 'skyblue', '$V_{CN}$', 'V', line_style='--', is_main_phasor=False)

# Adicionar os fasores de Tensão Fase-Fase (em azul escuro, linha sólida)
plot_phasor(ax_V, V_AB_mag, V_AB_ang, 'blue', '$V_{AB}$', 'V', is_main_phasor=True)
plot_phasor(ax_V, V_BC_mag, V_BC_ang, 'blue', '$V_{BC}$', 'V', is_main_phasor=True)
plot_phasor(ax_V, V_CA_mag, V_CA_ang, 'blue', '$V_{CA}$', 'V', is_main_phasor=True)

# Configurações adicionais do plot de Tensão
max_mag_V = max(V_LL, V_phase)
plot_lim_V = max_mag_V * 1.5 # Adiciona margem para rótulos
ax_V.set_xlim([-plot_lim_V, plot_lim_V])
ax_V.set_ylim([-plot_lim_V, plot_lim_V])
ax_V.set_aspect('equal', adjustable='box')
ax_V.grid(True, linestyle=':', alpha=0.7)
# ax_V.set_title('Diagrama Fasorial das Tensões (Conexão Estrela)', fontsize=16)
ax_V.set_xlabel('Componente Real (V)', fontsize=12)
ax_V.set_ylabel('Componente Imaginária (V)', fontsize=12)
ax_V.axhline(0, color='gray', linewidth=0.5)
ax_V.axvline(0, color='gray', linewidth=0.5)

# --- GRÁFICO DE CORRENTES ---
fig_I, ax_I = plt.subplots(figsize=(8, 8))

# Adicionar os fasores de Corrente de Linha (Correntes de Fase em Y)
plot_phasor(ax_I, I_A_mag, I_A_ang, 'red', '$I_{A}$', 'A', is_main_phasor=True)
plot_phasor(ax_I, I_B_mag, I_B_ang, 'red', '$I_{B}$', 'A', is_main_phasor=True)
plot_phasor(ax_I, I_C_mag, I_C_ang, 'red', '$I_{C}$', 'A', is_main_phasor=True)

# Configurações adicionais do plot de Corrente
max_mag_I = max(I_A_mag, I_B_mag, I_C_mag)
plot_lim_I = max_mag_I * 1.5 # Adiciona margem para rótulos
ax_I.set_xlim([-plot_lim_I, plot_lim_I])
ax_I.set_ylim([-plot_lim_I, plot_lim_I])
ax_I.set_aspect('equal', adjustable='box')
ax_I.grid(True, linestyle=':', alpha=0.7)
# ax_I.set_title('Diagrama Fasorial das Correntes de Linha (Conexão Estrela)', fontsize=16)
ax_I.set_xlabel('Componente Real (A)', fontsize=12)
ax_I.set_ylabel('Componente Imaginária (A)', fontsize=12)
ax_I.axhline(0, color='gray', linewidth=0.5)
ax_I.axvline(0, color='gray', linewidth=0.5)

# Mostrar todos os plots
plt.tight_layout() # Ajusta o layout para evitar sobreposição de títulos/rótulos
plt.show()

#%%