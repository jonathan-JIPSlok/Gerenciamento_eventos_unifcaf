from time import sleep

from funcoes_do_sistema.utilidades import cabecalho
from manipulador_de_dados import lerArquivoJson, LocalArquivos

def login_coordenador() -> dict:
    """
    Responsável por logar um coordenador no sistema
    :return dict: dados do coordenador
    """
    cabecalho("Login Coordenador")
    nome = input("Nome completo: ").strip().capitalize()
    senha = input("Senha: ").strip()

    #lê os dados do arquivo
    dados = lerArquivoJson(LocalArquivos().arquivoUsuarios)

    #Verifica se os dados batem.
    if nome in dados.keys() and dados[nome]['senha'] == senha:
        return {nome:dados[nome]}
    else:
        print("Nome ou senha inválidos!")
        sleep(1)
        return {}

def loginAluno() -> dict:
        """Faz o login de um Aluno
        :return dict: retorna os dados do aluno"""

        cabecalho("Login do Aluno")

        #Coleta os dados
        ra = input("RA: ").strip()
        senha = input("Senha: ").strip()

        #Coleta os usuarios
        usuarios = lerArquivoJson(LocalArquivos().arquivoUsuarios)
        if ra in usuarios.keys() and usuarios[ra]['senha'] == senha:
            return {ra:usuarios[ra]}
        else:
            print("Dados inválidos!")
            sleep(1)
            return {}