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

    def printarEventoDetalhado(self, numero, evento) -> None:
        """Printa um eventos detalhadamente
        :param numero: int: número do evento na lista
        :param evento: dict: dicionário contendo os dados do evento
        """

        #Printando o evento
        print(f"""Número do evento [{numero}] - Evento: {evento[0]}
Data: {evento[1]['data']}
Descrição: {evento[1]['descrição']}
Vasgas restantes: {evento[1]['número máximo de inscritos'] - evento[1]['inscritos']}
""")
    
    def printarEventos(self) -> None:
        """Mostra os eventos disponíveis e possibilita se inscrever em um"""
        cabecalho("Eventos Unifecaf")
        #ListComprehension que passa os dados dos eventos que tem vagas disponíveis a função printarEventoDetalhado um por um.
        [self.printarEventoDetalhado(numero, evento) if evento[1]['inscritos'] < evento[1]['número máximo de inscritos'] else None for numero, evento in enumerate(lerArquivoJson(LocalArquivos().arquivoEventos).items())]
        print("-"*50)

        usuario = input("[sair] para voltar \n[1] Para se inscrever-se em um evento \n\nO que deseja: ").strip().lower()
        if usuario == 'sair':
            return None
        
        #Permite que o usuário se inscreva em um evento
        elif usuario == '1':
            usuario = input("Número do evento: ")
            
            #Verifica se o usuário digitou um número e se ele é menor que o número de eventos disponíveis
            if usuario.isnumeric() and int(usuario) < len(lerArquivoJson(LocalArquivos().arquivoEventos)):
                self.inscreverEmEventos(int(usuario))
            else:
                print("Evento inválido!")
                sleep(1)
        else:
            print("Opção inválida!")
            sleep(1)
    
    def inscreverEmEventos(self, numeroEvento) -> None:
        """Inscreve o usuario em um evento disponível"""

        #Coletando dados dos arquivos
        eventos = lerArquivoJson(LocalArquivos().arquivoEventos)
        inscritos = lerArquivoJson(LocalArquivos().arquivoInscritos)

        #Verifica se tem vagas no evento
        if list(eventos.items())[numeroEvento][1]['inscritos'] < list(eventos.items())[numeroEvento][1]['número máximo de inscritos'] and list(eventos.items())[numeroEvento][1]['status'] == 'aberto':

            #Registra a inscrição do aluno no evento
            aluno = list(self.dadosDoAluno.keys())[0]
            if aluno not in list(inscritos.keys()):
                inscritos[aluno] = [list(eventos.keys())[numeroEvento]]
                #Aumenta o número de inscritos em um evento
                eventos[list(eventos.keys())[numeroEvento]]['inscritos'] += 1
            
            elif len(inscritos[aluno]) > 0:

                #Verifica se o aluno já está inscrito no evento
                if list(eventos.keys())[numeroEvento] not in inscritos[aluno]:
                    
                    #Adiciona o evento na lista de eventos inscritos
                    inscritos[aluno].append(list(eventos.keys())[numeroEvento])
                    
                    #Aumenta o número de inscritos em um evento
                    eventos[list(eventos.keys())[numeroEvento]]['inscritos'] += 1
               
                else:
                    print("Você já está inscrito nesse evento!")
                    sleep(1)
                    return None
            #Salva nos arquivos
            salvarArquivoJson(LocalArquivos().arquivoEventos, eventos)
            salvarArquivoJson(LocalArquivos().arquivoInscritos, inscritos)

            print("Inscrição efetuada com sucesso!")
            sleep(1)
        
        else:
            print("Evento inválido!")
            sleep(1)