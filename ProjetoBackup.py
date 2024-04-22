# 1-Etapa : Selecionar a pasta do computador

#Importação das bibliotecas
import os
from tkinter.filedialog import askdirectory
import shutil
import datetime

#Comando askdirectory para o usuario selecionar uma pasta
pasta_selecionada = askdirectory()

#Listando os arquivos de dentro dessa pasta
lista_arquivos = os.listdir(pasta_selecionada)

#Estamos adicionando uma pasta backup dentro da pasta selecionada
pasta_backup = pasta_selecionada + "/backup"

#Verificando se a pasta ja existe, caso não exista, ela sera criada
if not os.path.exists(pasta_backup):
    os.mkdir(pasta_backup)

# 2-Etapa : Fazer o backup dos arquivos que estão nessa pasta

#Armazenando a data atual
data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

#Nosso objetivo é fazer o backup dos arquivos dentro da pasta selecionada
#Para uma pasta criada dentro da pasta selecionada, o backup vai criar uma pasta
#Cuja nome vai ser a data e a hora exata do backup

#Para cada arquivo na lista de arquivos
for arquivo in lista_arquivos:

    #Estamos pegando o diretorio atual e criando o novo
    dir_atual = f"{pasta_selecionada}/{arquivo}"
    dir_final = f"{pasta_backup}/{data_atual}/{arquivo}"

    #Se a pasta Data Atual não exisitir, crie ela
    if not os.path.exists(f"{pasta_backup}/{data_atual}"):
        os.mkdir(f"{pasta_backup}/{data_atual}")

    #Essa parte copia os arquivos para o backup
    if "." in arquivo:
        shutil.copy2(dir_atual,dir_final)
    #Essa parte copia as pastas para o backup
    elif not "backup" in arquivo:
        shutil.copytree(dir_atual,dir_final)




