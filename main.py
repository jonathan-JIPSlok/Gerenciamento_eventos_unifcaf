from os import makedirs
from time import sleep

from funcoes_do_sistema import login_coordenador
from funcoes_do_sistema.utilidades import cabecalho, printar_opcoes
from manipulador_de_dados import lerArquivoJson, LocalArquivos
from funcoes_do_sistema.systema_coordenador import Coordenador


# Verifica se é o primeiro acesso, caso seja ele criar a pasta "data" e chama o cadastro de um coordenador
if lerArquivoJson(LocalArquivos().arquivoUsuarios) == {}:
    makedirs("data", exist_ok = True)
    Coordenador().cadastrar()

# Opções para login de um usuário
while True:

    # Cabeçalho e opções para o usuário
    cabecalho("Sistema de Eventos Unifecaf")
    printar_opcoes(("Sou aluno", "Sou coordenador"))
    usuario = input("oque deseja: ")
    
    if usuario == "0": # chama o login de um aluno
        pass
    elif usuario == '1': #chama o login de um coordenador
        dadosDoUsuario = login_coordenador()
        if dadosDoUsuario != {}:
            break
    elif usuario == '2': # Sair do sistema
        exit()

# Verifica se é um coordenador e manipula
if list(dadosDoUsuario.values())[0]["tipo"] == "coordenador":

    #Cria um objeto que vai controlar o acesso total
    objetoDoUsuario = Coordenador()
    objetoDoUsuario.dadosDoCoordenador = dadosDoUsuario #Define os dados do usuário no objeto

    # Looping para fazer o sistema funcionar.
    while True:
        cabecalho("Unifecaf Eventos")
        printar_opcoes(objetoDoUsuario.funcoesDoCoordenador)
        usuario = input("O que deseja: ")

        if usuario == "0": #Chama função para cadastrar um evento
            objetoDoUsuario.cadastrarEvento()

        elif usuario == '1': #Chama função para atualizar um evento
            objetoDoUsuario.atualizarEvento()

        elif usuario == '2': #Chama função para excluir um evento
            objetoDoUsuario.excluirEvento()
        elif usuario == '3':
            exit()
        