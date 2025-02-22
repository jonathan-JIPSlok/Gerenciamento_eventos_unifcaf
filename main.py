from os import makedirs

from funcoes_do_sistema import login_coordenador, loginAluno
from funcoes_do_sistema.utilidades import cabecalho, printar_opcoes
from manipulador_de_dados import lerArquivoJson, LocalArquivos
from funcoes_do_sistema.systema_coordenador import Coordenador
from funcoes_do_sistema.system_aluno import aluno

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
        dadosDoUsuario = loginAluno()
        if dadosDoUsuario != {}:
            break
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

        elif usuario == '3': #chama função para cadastrar um aluno
            objetoDoUsuario.cadastrarAluno()
        
        elif usuario == '4': #Chama função para vizualisar eventos
            objetoDoUsuario.visualizarEventos()

        elif usuario == '5': #Chama função para vizualisar alunos
            objetoDoUsuario.alunosInscritos()
        
        elif usuario == '6':
            exit()

# verifica se é um Aluno e manipula
elif list(dadosDoUsuario.values())[0]['tipo'] == 'aluno':

    #objeto que vai controlar o aluno.
    objetoDoUsuario = aluno()
    objetoDoUsuario.dadosDoAluno = dadosDoUsuario #Define os dados do aluno

    # Looping para fazer o sistema funcionar.
    while True:
        cabecalho("Unifecaf Eventos")
        printar_opcoes(objetoDoUsuario.funcoesDoAluno)
        usuario = input("O que deseja: ")

        if usuario == '0':
            objetoDoUsuario.printarEventos()
        elif usuario == '1':
            exit()