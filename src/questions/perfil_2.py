from .aquecendo_os_motores_1 import usuarios

# 2 - Perfil
"""
Escreva um programa que leia os dados da lista ‘usuarios’ criada no exercício anterior e crie um dicionário para cada usuário. Cada dicionário deve ter as chaves "nome" e "idade" com os respectivos valores, e a chave "localização" contendo uma tupla (cidade, estado). Armazene esses dicionários em uma nova lista chamada perfis.
"""
########################

perfis = [
    {"nome": usuario[0], "idade": usuario[1], "localizacao": (usuario[2], usuario[3])} 
    for usuario in usuarios
]

def main():
    print("Esta é a questão: Perfil")

    # Exemplo de uso: impressão dos perfis
    for perfil in perfis:
        print(perfil)
