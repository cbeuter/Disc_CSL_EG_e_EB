# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 00:06:48 2025

@author: chb
SPD (Semiplano Direito): raízes com parte real positiva → número igual ao número de mudanças de sinal na primeira coluna da tabela.
SPE (Semiplano Esquerdo): raízes com parte real negativa → número igual ao grau do polinômio menos o número de raízes em SPD e o número de raízes sobre o eixo imaginário.
jw (Eixo imaginário puro): raízes com parte real zero → detectadas quando há linha inteira zero na tabela (ou se a substituição do polinômio auxiliar ocorreu).




"""

#%%

import numpy as np

def routh_hurwitz_detalhado(coeffs, epsilon=1e-6):
    n = len(coeffs) - 1
    cols = (n + 1 + 1) // 2

    tabela = np.zeros((n + 1, cols))
    tabela[0, :len(coeffs[0::2])] = coeffs[0::2]
    tabela[1, :len(coeffs[1::2])] = coeffs[1::2]

    linha_zero_ocorreu = False

    for i in range(2, n + 1):
        for j in range(cols - 1):
            a = tabela[i - 2, 0]
            b = tabela[i - 2, j + 1]
            c = tabela[i - 1, 0]
            d = tabela[i - 1, j + 1]

            if abs(c) < epsilon:
                c = epsilon

            tabela[i, j] = ((c * b) - (a * d)) / c

        if np.all(np.abs(tabela[i]) < epsilon):
            linha_zero_ocorreu = True
            ordem_aux = n - i + 1
            linha_aux = tabela[i - 1, :cols]
            deriv_aux = np.array([linha_aux[k] * (ordem_aux - 2 * k) for k in range(len(linha_aux))])
            tabela[i, :len(deriv_aux)] = deriv_aux
            if abs(tabela[i, 0]) < epsilon:
                tabela[i, 0] = epsilon

    primeira_coluna = tabela[:, 0]
    primeira_coluna = np.where(np.abs(primeira_coluna) < epsilon, 0, primeira_coluna)
    sinais = np.sign(primeira_coluna[primeira_coluna != 0])

    mudancas_sinal = 0
    for k in range(len(sinais) - 1):
        if sinais[k] != sinais[k + 1]:
            mudancas_sinal += 1

    # Número de raízes no SPD (parte real positiva)
    n_spd = mudancas_sinal
    # Raízes no jw (eixo imaginário puro)
    n_jw = 0
    if linha_zero_ocorreu:
        # Se linha zero ocorreu, indica raízes no jw (exemplo: raiz múltipla ou imaginária pura)
        # Mas a contagem exata requer análise adicional, aqui assumimos pelo menos 2 raízes no jw
        # pois sempre aparece em pares conjugados
        n_jw = 2

    # Raízes no SPE (parte real negativa)
    n_spe = n - n_spd - n_jw

    return tabela, n_spd, n_spe, n_jw

# Exemplo de uso
if __name__ == "__main__":
    # coef = [1, 0, 3, 0, 1]  # Exemplo com possibilidade de linha zero
    # coef = [1, 3, 2, 6, 5, 15]
    # coef = [1, 2, 3, 4, 5]
    # coef = [3, 9, 6, 4, 7, 8, 2, 6]
    # coef = [1, 2, 3, 6, 5, 3]
    # coef = [3, 5, 6, 3, 2, 1]
    coef = [3, 5, 8, 3, 7, 3, 5, 6, 3, 2, 1]
    
    
    tabela, spd, spe, jw = routh_hurwitz_detalhado(coef)

    print("Tabela de Routh-Hurwitz:")
    print(tabela)
    print()
    print(f"Número de raízes em SPD (parte real positiva): {spd}")
    print(f"Número de raízes em SPE (parte real negativa): {spe}")
    print(f"Número de raízes no eixo jw (parte imaginária pura): {jw}")


#%%