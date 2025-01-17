from time import sleep
from datetime import datetime

from .utilidades import cabecalho
from manipulador_de_dados import lerArquivoJson, salvarArquivoJson, LocalArquivos

class Coordenador:
    """
    Classe que controla o Coordenador
    """

    def cadastrar(self) -> None:
        """Faz o cadastro de um Coordenador"""
        
        cabecalho("Cadastro de Coordenador")

        #Coletando os dados
        nomeCompleto = input("Nome completo: ").capitalize().strip()
        senha = input("Senha: ").strip()
        email = input("E-mail: ").strip()
        telefone = input("Telefone: ").replace(" ", '')
        print("Data de nascimento")
        diaNascimento = input("Dia: ").strip()
        mesNascimento = input("Mês: ").strip()
        anoNascimento = input("Ano: ").strip()
        dataNascimento = f"{diaNascimento}-{mesNascimento}-{anoNascimento}"
        
        #Confirmando se está tudo correto
        try:
            if len(nomeCompleto) > 0 and len(senha) > 0 and len(email) > 0 and telefone.isnumeric() and datetime.strptime(dataNascimento, "%d-%m-%Y"):
                
                #Arrumando a data, lendo arquivo de usuários e inserindo o novo usuário
                dataNascimento = f"{diaNascimento}/{mesNascimento}/{anoNascimento}"
                usuarios = lerArquivoJson(LocalArquivos().arquivoUsuarios)
                usuarios[nomeCompleto] = {"senha": senha, "e-mail": email, "telefone": telefone, "data de nascimento": dataNascimento, "tipo": "coordenador"}
                salvarArquivoJson(LocalArquivos().arquivoUsuarios, usuarios)
                
                print(f"{nomeCompleto} registrado com sucesso!")
                sleep(1)
            else:
                print("Dados inválidos")
                sleep(1)
        except ValueError:
            print("Dados inválidos")
            sleep(1)