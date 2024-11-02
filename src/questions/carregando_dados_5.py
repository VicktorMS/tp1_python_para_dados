# 5 - Carregando dados
"""
Crie uma implementação que leia os dados presentes no arquivo "base_inicial.txt" e os armazene na lista perfis_validos, criando novas palavras-chave para os dados adicionais encontrados. (O arquivo está disponível no repositório.)
"""
########################
perfis_arquivo = []

def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas


def processar_dados(brutos):
    header = brutos[0].strip().split('?')
    linhas = brutos[1:]
    return [criar_perfil(linha.strip().split('?')) for linha in linhas]


def criar_perfil(dados):
    nome = dados[0] if dados[0] else None
    idade = int(dados[1]) if dados[1].isdigit() else None
    cidade = dados[2] if dados[2] else None
    estado = dados[3] if dados[3] else None
    amigos = dados[4:]
    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "estado": estado,
        "amigos": amigos,
    }


def carregar_perfis_validos(caminho_arquivo):
    dados_brutos = ler_arquivo(caminho_arquivo)
    perfis_validos = processar_dados(dados_brutos)
    return perfis_validos


def carregar_perfis_arquivo(caminho_arquivo):
    global perfis_arquivo
    dados_brutos = ler_arquivo(caminho_arquivo)
    perfis_arquivo = processar_dados(dados_brutos)
    return perfis_arquivo


caminho_arquivo = 'src/data/base_inicial.txt'
carregar_perfis_arquivo(caminho_arquivo)

def main():
    print(perfis_arquivo)