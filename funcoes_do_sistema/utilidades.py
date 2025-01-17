from os import system

def cabecalho(titulo = str) -> None:
    """
    Função que imprime um cabeçalho bonito
    :param titulo: str: titulo do cabeçalho
    """
    system("cls")
    print("-"*50)
    print(f"\t {titulo}")
    print("-" *50)

def printar_opcoes(opcoes = tuple) -> None:
    """
    Função que imprime opções a um usuário
    :param opcoes: tuple: tupla contendo as opções a serem passadas ao usuário
    """
    for numero, item in enumerate(opcoes):
        print(f"[{numero}] - {item}")
    print(f"[{len(opcoes)}] - sair \n")