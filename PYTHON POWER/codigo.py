# bibliotecas = pacotes de códigos 
# pip intall pyautogui

import pyautogui
import time

#pyautogui.click -> clicar
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar uma unica tecla
#pyautogui.hotkey -> aperta um atalho (hotkey)
#pyautogui.scroll -> rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5 # tempo de espera entre um comando e outro
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo a passso do meu proframa
# Passo 1:Entrar no sistema da empresa 

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
#pyautogui.click(x=2669, y=113) #ampliar a minha tela
#fazer uma pausa maior para o site carregar 
time.sleep(5) 


# Passo 2: Fazer login 
#clicar no campo de email
pyautogui.click(x=571, y=413) #clicar no campo de email (posição do mouse)    
pyautogui.write('mestradopython@gmail.com')
pyautogui.press('tab') #passar para o campo de senha
pyautogui.write('xuxubeleza')
pyautogui.press('tab') #passar para o botão de login
pyautogui.press('enter')
#fazer uma pausa para o site carregar a próxima página
time.sleep(5)
#time.sleep serve para colocar alguns segundos como pausa, para o próximo passo.


# Passo 3: Abrir a base do dados (importar o arquivo)
#pip install pandas opnenpyxl
import pandas as pd

tabela = pd.read_csv('produtos.csv')#ele vai ler a tabela da base de dados e guardar dentro da variável tabela
print(tabela) #mostrar a tabela para o usuário

# Passo 4: Cadastrar um produto
for linha in tabela.index: #para cada linha da minha tabela faça o passo 4
# Index (índice) representa a posição de um elemento em uma lista, string ou array.
# Em Python os índices começam em 0, ou seja, o primeiro elemento sempre terá index 0.
    pyautogui.click(x=649, y=296)
    
    
    #codigo
    codigo = str(tabela.loc[linha,'codigo']) #loc -> localizar o valor da linha e coluna 
    #str -> converter o valor para texto, para o pyautogui escrever
    pyautogui.write(codigo)
    pyautogui.press('tab')

    #marca
    marca = str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    #tipo
    tipo = str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    #categoria
    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
   #preço
    preco = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')  
    
    #custo
    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    #obs 
    obs =  str(tabela.loc[linha, "obs"])
    if obs != 'nan': #verificar se a célula de obs não está vazia (nan)
       pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter') 
    
    #voltar ao inicio da tela
    pyautogui.scroll(2000) #rolar a tela para cima, para voltar ao início da página

# Passo 5: Repetir o passo 4 até acabar a lista de produtos