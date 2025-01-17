import json

def lerArquivoJson(localDoArquivo = str) -> dict:
    """
    Função que lê um arquivo .JSON
    :param localDoArquivo: str: Local em que se encontra o arquivo.
    :return dict: Retorna um dicionário com os dados do arquivo.
    """
    try:
        with open(localDoArquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        return {}

def salvarArquivoJson(localDoArquivo = str, dados = dict) -> None:
    """
    Salva os dados de um dicionário no arquivo .JSON
    :param localDoArquivo: str: Local em que se encontra o arquivo.
    :param dados: dict: dicionário contendo os dados.
    """
    with open(localDoArquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

class LocalArquivos:
    """
    Contem os locais dos arquivos.
    """

    @property
    def arquivoUsuarios(self) -> str:
        """Retorna o local do arquivo dos dados dos usuários"""
        return "data/usuarios.json"
    
    @property
    def arquivoEventos(self) -> str:
        """Retorna o local do arquivo dos eventos cadastrados"""
        return "data/eventos.json"
    
    @property
    def arquivoInscritos(self) -> str:
        """Retorna o local do arquivo dos inscritos em eventos"""
        return "data/inscritos.json"