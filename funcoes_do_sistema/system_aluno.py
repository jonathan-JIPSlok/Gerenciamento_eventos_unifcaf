from time import sleep

from manipulador_de_dados import LocalArquivos, lerArquivoJson, salvarArquivoJson
from .utilidades import cabecalho

class aluno:
    """Contem todas as funções dos alunos"""
    def __init__(self) -> None:
        self._dadosDoAluno = {}

    @property
    def dadosDoAluno(self) -> dict:
        """Retorna os dados do Aluno"""
        return self._dadosDoAluno
    
    @dadosDoAluno.setter
    def dadosDoAluno(self, dados: dict) -> None:
        """Defini os dados do aluno"""
        self._dadosDoAluno = dados
    
    @property
    def funcoesDoAluno(self) -> tuple:
        """Retorna as funções de um aluno"""
        return ('Ver Eventos', )

    def printarEventoDetalhado(self,numero, evento) -> None:
        """Printa um eventos detalhadamente
        :param numero: int: número do evento na lista
        :param evento: dict: dicionário contendo os dados do evento
        """
        cabecalho("Eventos Unifecaf")

        #Printando o evento
        print(f"""Níumero do evento [{numero}] - Evento: {evento[0]}
Data: {evento[1]['data']}
Descrição: {evento[1]['descrição']}
Vasgas restantes: {evento[1]['número máximo de inscritos'] - evento[1]['inscritos']}
""")
    
    def printarEventos(self) -> None:
        """Mostra os eventos disponíveis e possibilita se inscrever em um"""
        
        #ListComprehension que passa os dados dos eventos que tem vagas disponíveis a função printarEventoDetalhado um por um.
        [self.printarEventoDetalhado(numero, evento) if evento[1]['inscritos'] < evento[1]['número máximo de inscritos'] else None for numero, evento in enumerate(lerArquivoJson(LocalArquivos().arquivoEventos).items())]
        print("-"*50)

        usuario = input("[sair] para voltar \n[1] Para se inscrever-se em um evento \nO que deseja: ").strip().lower()
        if usuario == 'sair':
            return None
        
        #Permite que o usuário se inscreva em um evento
        elif usuario == '1':
            usuario = input("Número do evento: ")
            self.inscreverEmEventos(int(usuario))
        else:
            print("Opção inválida!")
            sleep(1)
    
    def inscreverEmEventos(self, numeroEvento) -> None:
        """Inscreve o usuario em um evento disponível"""

        #Coletando dados dos arquivos
        eventos = lerArquivoJson(LocalArquivos().arquivoEventos)
        inscritos = lerArquivoJson(LocalArquivos().arquivoInscritos)

        #Verifica se tem vagas no evento
        if list(eventos.items())[numeroEvento][1]['inscritos'] < list(eventos.items())[numeroEvento][1]['número máximo de inscritos']:
            
            #Aumenta o número de inscritos em um evento
            eventos[list(eventos.keys())[numeroEvento]]['inscritos'] += 1

            #Registra a inscrição do aluno no evento
            inscritos[str(self.dadosDoAluno.keys())] = list(eventos.keys())[numeroEvento]

            #Salva nos arquivos
            salvarArquivoJson(LocalArquivos().arquivoEventos, eventos)
            salvarArquivoJson(LocalArquivos().arquivoInscritos, inscritos)

            print("Inscrição efetuada com sucesso!")
            sleep(1)
        
        else:
            print("Evento inválido!")
            sleep(1)