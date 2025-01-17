from time import sleep
from datetime import datetime

from .utilidades import cabecalho, printar_opcoes
from manipulador_de_dados import lerArquivoJson, salvarArquivoJson, LocalArquivos

class Coordenador:
    """
    Classe que controla o Coordenador
    """
    def __init__(self):
        self._dadosDoCoordenador = None

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
                
                #Arrumando a data, lendo arquivo de usuários
                dataNascimento = f"{diaNascimento}/{mesNascimento}/{anoNascimento}"
                usuarios = lerArquivoJson(LocalArquivos().arquivoUsuarios)
                
                #Verifica se o usuário não está cadastrado
                if not nomeCompleto in usuarios.keys():

                    #inserindo o novo usuário
                    usuarios[nomeCompleto] = {"senha": senha, "e-mail": email, "telefone": telefone, "data de nascimento": dataNascimento, "tipo": "coordenador"}
                    salvarArquivoJson(LocalArquivos().arquivoUsuarios, usuarios)
                    
                    print(f"{nomeCompleto} registrado com sucesso!")
                    sleep(1)
                else:
                    print("Dados inválidos")
                    sleep(1) 
            else:
                print("Dados inválidos")
                sleep(1)
        except ValueError:
            print("Dados inválidos")
            sleep(1)
    

    @property
    def funcoesDoCoordenador(self) -> tuple:
        """
        Opções disponíveis para um coordenador em formato de tupla
        """
        return ("Cadastrar Evento", "Atualizar Evento", "Remover Evento")

    @property
    def dadosDoCoordenador(self) -> dict:
        """Retorna os dados do coordenador"""
        return self._dadosDoCoordenador
    
    @dadosDoCoordenador.setter
    def dadosDoCoordenador(self, dados: dict) -> None:
        """Define os dados do coordenador
        :param dados: dict: deve conter os dados do coordenador"""
        self._dadosDoCoordenador = dados

    def cadastrarEvento(self) -> None:
        """
        Faz o cadastro de um evento.
        """
        cabecalho("Cadastrar Eventos")

        #coletando dados
        nome = input("Nome do evento: ").strip()
        print("Data do evento")
        dia = input("Dia: ")
        mes = input("Mês: ")
        ano = input("Ano: ")
        descricao = input("Descrição: ").strip()
        numeroMaxInscritos = input("Número máximo de inscritos: ")
        data = f"{dia}-{mes}-{ano}"
        
        # válidando dados
        try:
            data = datetime.strptime(data, "%d-%m-%Y") #Válidando data
            if len(nome) != 0 and len(descricao) != 0 and int(numeroMaxInscritos) > 0 and data > datetime.now():
                
                #Coletando os eventos e salvando o novo evento
                eventos = lerArquivoJson(LocalArquivos().arquivoEventos)
                eventos[nome] = {"data": str(data).split()[0], "descrição": descricao, "número máximo de inscritos": numeroMaxInscritos, "inscritos": 0, "coordenador": list(self.dadosDoCoordenador.keys())[0]}
                salvarArquivoJson(LocalArquivos().arquivoEventos, eventos)
            
            else:
                print("Dados inválidos! confirme se todos os campos estão preenchidos.")
        except ValueError:
            print("Dados inválidos! verifique data ou número máximo de inscritos.")
            sleep(1)