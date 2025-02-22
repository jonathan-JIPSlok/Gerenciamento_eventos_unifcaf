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
        telefone = input("Telefone: ").replace(" ", '').replace("(",'').replace(')','')
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
        return ("Cadastrar Evento", "Atualizar Evento", "Remover Evento", "Cadastrar Aluno", "Visualizar Eventos", "Alunos Inscritos em eventos")

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
                
                #Arrumando a data
                data = str(data).split()[0]
                data = f"{data[8:10]}/{data[5:7]}/{data[0:4]}"

                #Coletando os eventos e salvando o novo evento
                eventos = lerArquivoJson(LocalArquivos().arquivoEventos)
                eventos[nome] = {"data": str(data).split()[0], "descrição": descricao, "número máximo de inscritos": int(numeroMaxInscritos), "inscritos": 0, "coordenador": list(self.dadosDoCoordenador.keys())[0], 'status':"aberto"}
                salvarArquivoJson(LocalArquivos().arquivoEventos, eventos)
                print("Evento registrado com sucesso!")
                sleep(1)
            
            else:
                print("Dados inválidos! confirme se todos os campos estão preenchidos.")
                sleep(1)
        except ValueError:
            print("Dados inválidos! verifique data ou número máximo de inscritos.")
            sleep(1)
    
    def atualizarEvento(self) -> None:
        """
        Atualiza um evento
        """
        cabecalho("Atualizar Evento")

        #Coletando os eventos
        eventos = lerArquivoJson(LocalArquivos().arquivoEventos)

        # mostrando os eventos pelo nome com ListComprehension, seu desempenho é melhor
        [print(f"\n[{numero}] \nEvento: {nome}") for numero, nome in enumerate(eventos.keys())]
        usuario = input("\nQual evento deseja atualizar: ")

        try:
            evento = list(eventos)[int(usuario)] # coleta o evento selecionado

            # Mostra os dados do evento selecionado
            print(f"""\nNome: {evento}
Data: {eventos[evento]["data"]}
Descrição: {eventos[evento]["descrição"]}
Número máximo de inscritos: {eventos[evento]["número máximo de inscritos"]}
Inscritos: {eventos[evento]["inscritos"]}
Coordenador: {eventos[evento]["coordenador"]}
status: {eventos[evento]["status"]}
{'-'*50}\n""")
            
            #Mostra as opções do usuário
            printar_opcoes(("Alterar data", "Alterar número máximo de vagas", "Cancelar Evento"))
            usuario = input("O que deseja: ")
            
            if usuario == "0":
                print("Data do evento")
                dia = input("Dia: ")
                mes = input("Mês: ")
                ano = input("Ano: ")

                try:
                    #Válidando data
                    data = datetime.strptime(f"{dia}-{mes}-{ano}", "%d-%m-%Y")
                except ValueError:
                    print("Dados inválidos!")
                    sleep(1)
                    return None
                else:
                    #Arrumando a data
                    data = str(data).split()[0]
                    data = f"{data[8:10]}/{data[5:7]}/{data[0:4]}"

                    eventos[evento]["data"] = data

            elif usuario == '1':
                #Altera o maximo de inscritos de um evento
                try:
                    maximoDeInscritos = int(input("Número máxmio de inscritos: "))

                    #Verifica se o máximo de inscritos definido é maior ou igual ao total de inscritos. 
                    if maximoDeInscritos >= eventos[evento]['inscritos']:
                        eventos[evento]["número máximo de inscritos"] = maximoDeInscritos
                    else:
                        print("Número máximo deve ser maior ou igual o total de inscritos!")
                        sleep(1)
                except ValueError:
                    print("Dados inválidos!")
                    sleep(1)
            elif usuario == '2':
                eventos[evento]['status'] = "cancelado"
            elif usuario == '3': # saindo
                return None
            else:
                print("opção inválida!")
                sleep(1)
                return None
            
            salvarArquivoJson(LocalArquivos().arquivoEventos, eventos)
            print("dados atualizados com sucesso!")
            sleep(1)

        except ValueError:
            print("Dados inválidos!")
            sleep(1)
        except IndexError:
            print("Dados inválidos!")
            sleep(1)

    def excluirEvento(self):
        """Exclui um evento que foi cancelado"""
        cabecalho("Exclui Eventos")
        eventos = []
        
        #separa os eventos que estão cancelados
        [eventos.append(evento) if evento[1]['status'] == "cancelado" else None for evento in lerArquivoJson(LocalArquivos().arquivoEventos).items()]
        
        #Mostra os eventos detalhado
        for numero, evento in enumerate(eventos):
            print(f"""[{numero}]
Nome: {evento[0]}
Data: {evento[1]['data']}
Descrição: {evento[1]["descrição"]}
Número máximo de inscritos: {evento[1]["número máximo de inscritos"]}
Inscritos: {evento[1]["inscritos"]}
Coordenador: {evento[1]["coordenador"]}
status: {evento[1]["status"]}
{'-'*50}\n""")
        
        usuario = input("Qual evento deseja excluir: ")
        
        try: #Esclui o evento selecionado e salva o json.
            evento = eventos[int(usuario)][0]
            eventos = lerArquivoJson(LocalArquivos().arquivoEventos)
            del eventos[evento]
            salvarArquivoJson(LocalArquivos().arquivoEventos, eventos)
            print("Evento deletado com sucesso!")
            sleep(1)

        except ValueError:
            print("Dados inválidos!")
            sleep(1)
        except IndexError:
            print("Dados inválidos!")
            sleep(1)

    def cadastrarAluno(self) -> None:
        """
        Cadastra um aluno.
        """
        cabecalho("Cadastro de Aluno")

        #Coletando dados
        ra = input("RA do Aluno: ").strip()
        nome = input("Nome completo: ").strip().capitalize()
        senha = input("Senha: ").strip()
        print("Data de Nascimento")
        dia = input("Dia: ")
        mes = input("Mês: ")
        ano = input("Ano: ")
        email = input("Email do Aluno: ").strip()
        telefone = input("Telefone: ").replace(" ", '').replace("(", '').replace(')', '')

        try: #Vericicando a data
            data = datetime.strptime(f"{dia}-{mes}-{ano}", '%d-%m-%Y')
            data = str(data).split()[0]
            data = f"{data[8:10]}/{data[5:7]}/{data[0:4]}"
        except ValueError:
            print("Data inválida!")
            sleep(1)
            return None
        
        #Verificando os dados
        if ra.isnumeric() and len(nome) > 0 and len(senha) > 0 and len(email) > 0 and telefone.isnumeric():
            usuarios = lerArquivoJson(LocalArquivos().arquivoUsuarios)
            
            if not ra in usuarios: #Verificando se o aluno não está registrado para evitar duplicidade

                #Registrando o aluno
                usuarios[ra] = {"nome": nome, "senha": senha, "data de nascimento": str(data), 'email':email, 'telefone':telefone, 'coordenador':list(self.dadosDoCoordenador.keys())[0], 'tipo':"aluno"}
                salvarArquivoJson(LocalArquivos().arquivoUsuarios, usuarios)

                print("Alunos registrado com sucesso!")
                sleep(1)
            else:
                print("Aluno já exitente nos registros!")
                sleep(1)
        else:
            print("Dados inválidos!")
            sleep(1)
    
    def visualizarEventos(self):
        """Mostra os eventos registrados"""
        cabecalho("Eventos registrados Unifecaf")

        eventos = lerArquivoJson(LocalArquivos().arquivoEventos)
        [print(f'[{numero}] - Evento: {nome} \n') for numero, nome in enumerate(eventos.keys())]
        print("-"*50)
        print("\n")

        printar_opcoes(("Ver inscritos", 'Cadastrar novo evento', "Atualizar evento"))
        usuario = input("O que deseja: ")
        if usuario == '0':
            self.alunosInscritos()
        elif usuario == '1':
            self.cadastrarEvento()
        elif usuario == '2':
            self.atualizarEvento()
        elif usuario == '3':
            return

    def alunosInscritos(self):
        """Mostra os alunos inscritos em um evento"""
        cabecalho("Alunos Inscritos")
        eventos = lerArquivoJson(LocalArquivos().arquivoEventos)
        
        #Mostra os eventos
        [print(f'[{numero}] - Evento: {nome} \n') for numero, nome in enumerate(eventos.keys())]
        print("-"*50)
        print("\n")
        
        usuario = input("Qual evento deseja ver os inscritos: ")
        try:
            evento = list(eventos)[int(usuario)]
            inscritos = lerArquivoJson(LocalArquivos().arquivoInscritos)
            
            #Mostra os inscritos
            [print(f'Aluno: {aluno}') for aluno in inscritos.keys() if evento in inscritos[aluno]]
            print("-"*50)
            print("\n")
            input("Pressione enter para continuar...")
        except ValueError:
            print("Dados inválidos!")
            sleep(1)
        except IndexError:
            print("Dados inválidos!")
            sleep(1)