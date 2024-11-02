# 14 - Quantidade de Amigos
"""
Crie uma função que leia o arquivo "rede_INFNET.txt" e mostre quantos amigos cada usuário possui, imprimindo o nome do usuário e a quantidade de amigos.
"""
########################
def contar_amigos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split('?')
            nome = dados[0]
            amigos = dados[4:]  
            if nome and nome != "None": 
                print(f"{nome} possui {len(amigos)} amigo(s).")

def main():
    print("Esta é a questão: Quantidade de Amigos")
    contar_amigos("src/data/rede_INFNET.txt")