import time
from time import sleep
import pyautogui
import pyperclip
import pandas as pd
import numpy
import openpyxl
#import display
#import pytest
#import IPython
# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escreve um texto
# pyautogui.press -> apertar 1 tecla

sleep(2)

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empres (no nosso caso vai ser um Link do drive)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
#pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# demora alguns segundinhos
sleep(5)


# descobrir posição do mouse
#mouse = pyautogui.position()
#print(mouse)


# Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta exportar)
pyautogui.click(x=-1215, y=400, clicks=2)
sleep(2)


# Passo 3: Exportar/Fazer Download da Base de Dados
pyautogui.click(x=-1249, y=468)             # clica no arquivo
pyautogui.click(x=-203, y=285)              # clica nos 3 pontinhos
pyautogui.click(x=-382, y=699, clicks=2)    # clicar no fazer download
sleep(5)


# Passo 4: Importar a base de dados para o Python
# r - para ler de maneira crua (raw)
tabela = pd.read_excel(r"D:\Users\Celso Annes\Downloads\Vendas - Dez.xlsx")



# Passo 5: Calcular os indicadores
# faturamento - soma da coluna valor final
faturamento = tabela["Valor Final"].sum()

# quantidade de produtos - soma da coluna quantidade
quantidade = tabela["Quantidade"].sum()

print(quantidade)
print(faturamento)

# Passo 6: Enviar um email para diretoria com o relatório
