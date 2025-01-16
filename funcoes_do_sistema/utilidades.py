from os import system

def cabecalho(titulo = str) -> None:
    """
    Classe que imprime um cabeçalho bonito
    :param titulo: str: titulo do cabeçalho
    """
    system("cls")
    print("-"*50)
    print(f"\t {titulo}")
    print("-" *50)