# -*- coding: utf-8 -*-
"""
Created on Mon May 19 18:54:50 2025

@author: CB

Calculo simples, onde os dados não são coletados via tabela e sim, inseridos
pelo usuário.

Aprimoramentos: É necessário embutir as tabelas para a escolha automática dos
parâmetros do ambiente.


"""


import tkinter as tk
from tkinter import ttk, messagebox
from math import ceil

TIPOS_LAMPADAS = {
    "LED 9W": 800,
    "LED 12W": 1100,
    "LED 15W": 1600,
    "Fluorescente 15W": 900,
    "Fluorescente 20W": 1300,
    "Incandescente 60W": 700,
    "Incandescente 100W": 1600,
    "Halógena 50W": 600,
    "Halógena 100W": 1200,
}

DEFAULTS = {
    "iluminancia": 300,
    "area": 20,
    "uf": 0.6,
    "mf": 0.8,
}

def calcular_fluxo_luminoso_total(iluminancia, area, uf, mf):
    return (iluminancia * area) / (uf * mf)

def calcular_quantidade_lampadas(fluxo_total, fluxo_lampada):
    return ceil(fluxo_total / fluxo_lampada)

def calcular():
    try:
        iluminancia = float(entry_iluminancia.get())
        area = float(entry_area.get())
        uf = scale_uf.get() / 100  # valor real com casas decimais
        mf = scale_mf.get() / 100
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        return

    tipo_lampada = combo_lampadas.get()
    fluxo_luminoso_lampada = TIPOS_LAMPADAS[tipo_lampada]

    fluxo_total = calcular_fluxo_luminoso_total(iluminancia, area, uf, mf)
    qtd = calcular_quantidade_lampadas(fluxo_total, fluxo_luminoso_lampada)

    resultado_texto = (
        f"Fluxo luminoso total necessário: {fluxo_total:.2f} lumens\n"
        f"Lâmpada escolhida: {tipo_lampada} ({fluxo_luminoso_lampada} lumens)\n"
        f"Quantidade mínima de lâmpadas necessárias: {qtd}\n"
        f"Fator de Utilização (UF): {uf:.2f}\n"
        f"Fator de Manutenção (MF): {mf:.2f}"
    )
    label_resultado.config(text=resultado_texto)

root = tk.Tk()
root.title("Cálculo de iluminação pelo método dos lumens")
root.geometry("450x450")
root.resizable(False, False)

tk.Label(root, text="Iluminância desejada (lux):").pack(pady=(10,0))
entry_iluminancia = tk.Entry(root)
entry_iluminancia.pack()
entry_iluminancia.insert(0, str(DEFAULTS["iluminancia"]))

tk.Label(root, text="Área do ambiente (m²):").pack(pady=(10,0))
entry_area = tk.Entry(root)
entry_area.pack()
entry_area.insert(0, str(DEFAULTS["area"]))

# Slider para UF (0.3 a 0.9)
tk.Label(root, text="Fator de utilização (UF):").pack(pady=(10,0))
scale_uf = tk.Scale(root, from_=30, to=90, orient='horizontal', length=300)
scale_uf.set(int(DEFAULTS["uf"]*100))
scale_uf.pack()

# Slider para MF (0.6 a 0.9)
tk.Label(root, text="Fator de manutenção (MF):").pack(pady=(10,0))
scale_mf = tk.Scale(root, from_=60, to=90, orient='horizontal', length=300)
scale_mf.set(int(DEFAULTS["mf"]*100))
scale_mf.pack()

tk.Label(root, text="Tipo de lâmpada:").pack(pady=(10,0))
combo_lampadas = ttk.Combobox(root, values=list(TIPOS_LAMPADAS.keys()), state="readonly")
combo_lampadas.pack()
combo_lampadas.current(0)

btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.pack(pady=15)

label_resultado = tk.Label(root, text="", justify="left")
label_resultado.pack(padx=10)

root.mainloop()