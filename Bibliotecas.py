#Modulos e Bibliotecas

"""
Bibliotecas a "Grosso Modo" são pacotes de códigos que outos programadores
ja fizerem anteriormente, porque o problema que voce esta tentando resolver, muito
provalvemente alguem ja precisou resolver anteriormente, então bibliotecas públicas e 
gratuitas nos ajudam a otimizar nosso tempo

Obs: Na maioria da vezes ao importar bibliotecas, voce esta na realidade importando classes
e assim voce pode criar objetos dessas classes e usar métodos e atributos

Existem diversas bibliotecas para difernentes finalidades

Pandas para a ánalise de dados
https://pandas.pydata.org/

Openpyxl muito útil para editar arquivos xlsx
https://openpyxl.readthedocs.io/en/stable/

TensorFlow para Redes Neurais e Visão Computacional
https://www.tensorflow.org/?hl=pt-br

Pyautogui Para Automação 
https://pyautogui.readthedocs.io/en/latest/
"""

#Biblioteca "Operating System"
import os

#Vamos fazer um exercicio
#No repositorio temos uma pasta de arquivos com varios arquivos, alguns de 2022 e outros de 2023
#Meu objetivo é colocar todos os de 2022 na pasta de 22
#E todos os de 2023 na pasta de 23
#Lembrando que as pastas inicialmente estão vazias

#Lista dos arquivos
'''
['22', '23', 'abr22.txt', 'abr23.txt', 'fev22.txt', 'fev23.txt', 
 'jan22.txt', 'jan23.txt', 'mai22.txt', 'mar22.txt', 'mar23.txt']
'''

lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}",f"arquivos/22/{arquivo}")
        else:
            os.rename(f"arquivos/{arquivo}",f"arquivos/23/{arquivo}")

#Realizamos nosso objetivo nessa parte
#Aqui estamos renomeando o arquivo, colocando ele em outro diretorio
#Estamos levadando em consideração que sua pasta no mesmo local desse codigo
#Caso contrario,é so passar o caminho completo