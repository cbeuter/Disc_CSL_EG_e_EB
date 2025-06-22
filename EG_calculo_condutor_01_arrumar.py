# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 09:10:04 2025

@author: chbeu
"""

import math

def calcular_corrente(potencia, tensao, fator_potencia):
    return potencia / (tensao * fator_potencia)

def calcular_queda_tensao(corrente, comprimento, resistividade, secao):
    return (corrente * comprimento * resistividade) / secao

def calcular_secao_minima(corrente, queda_tensao_maxima, comprimento, resistividade, tensao):
    return (corrente * comprimento * resistividade) / (queda_tensao_maxima * tensao)

def main():
    # Exercício 1
    potencia1 = 2000  # W
    tensao1 = 220  # V
    fator_potencia1 = 0.9
    comprimento1 = 30  # m
    temperatura1 = 30  # oC
    queda_tensao_maxima1 = 0.04 * tensao1  # V
    resistividade = 0.0172  # Ωm (para cobre)

    corrente1 = calcular_corrente(potencia1, tensao1, fator_potencia1)
    print("Exercício 1:")
    print(f"Corrente: {corrente1:.2f} A")

    secao_minima1 = 1.5e-6  # m2 (1,5 mm2)
    queda_tensao1 = calcular_queda_tensao(corrente1, comprimento1, resistividade, secao_minima1)
    queda_tensao_percentual1 = (queda_tensao1 / tensao1) * 100
    print(f"Queda de tensão: {queda_tensao_percentual1:.2f}%")

    # Exercício 2
    potencia2 = 5000  # W
    tensao2 = 220  # V
    fator_potencia2 = 0.8
    comprimento2 = 50  # m
    temperatura2 = 40  # oC
    queda_tensao_maxima2 = 0.04 * tensao2  # V

    corrente2 = calcular_corrente(potencia2, tensao2, fator_potencia2)
    print("\nExercício 2:")
    print(f"Corrente: {corrente2:.2f} A")

    secao_minima2 = 6e-6  # m2 (6 mm2)
    queda_tensao2 = calcular_queda_tensao(corrente2, comprimento2, resistividade, secao_minima2)
    queda_tensao_percentual2 = (queda_tensao2 / tensao2) * 100
    print(f"Queda de tensão: {queda_tensao_percentual2:.2f}%")

if __name__ == "__main__":
    main()