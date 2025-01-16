from funcoes_do_sistema.utilidades import cabecalho
from manipulador_de_dados import lerArquivoJson, LocalArquivos

def login_coordenador() -> dict:
    """
    Responsável por logar um coordenador no sistema
    :return dict: dados do coordenador
    """
    cabecalho("Login Coordenador")
    nome = input("Nome completo: ").strip().lower()
    senha = input("Senha: ").strip()

    #lê os dados do arquivo
    dados = lerArquivoJson(LocalArquivos().arquivoUsuarios)

    #Verifica se os dados batem.
    if nome in dados.keys() and dados[nome]['senha'] == senha:
        return {nome:dados[nome]}
    else:
        print("Nome ou senha inválidos!")
        return {}