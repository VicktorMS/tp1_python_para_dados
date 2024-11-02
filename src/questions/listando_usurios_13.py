# 13 - Listando Usuários
"""
Escreva um programa que leia o arquivo "rede_INFNET.txt" e imprima na tela a lista dos nomes de todos os usuários da rede social.
"""
########################
def listar_usuarios(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        nomes = []
        for linha in arquivo:
            dados = linha.strip().split('?')
            nome = dados[0]
            if nome and nome != "None":  
                nomes.append(nome)
    
    print("Lista de Usuários:")
    for nome in sorted(set(nomes)):
        print(nome)

def main():
    print("Esta é a questão: Listando Usuários")
    listar_usuarios("src/data/rede_INFNET.txt")