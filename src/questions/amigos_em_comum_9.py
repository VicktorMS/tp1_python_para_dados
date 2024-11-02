import random
from .carregando_dados_5 import perfis_arquivo as perfis
# 9 - Amigos em Comum
"""
Crie um programa que selecione dois perfis aleatórios e utilize sets para armazenar os amigos de cada um desses usuários. Exiba os amigos em comum entre esses dois usuários, utilizando métodos e operação de sets.
"""
########################

def amigos_em_comum(perfis):
    perfil1, perfil2 = random.sample(perfis, 2) # Perfis aleatórios
    
    amigos_perfil1 = set(perfil1["amigos"])
    amigos_perfil2 = set(perfil2["amigos"])
    
    amigos_comuns = amigos_perfil1 & amigos_perfil2 # NOTE - Seria mais preciso se os amigos fossem IDs
    
    print(f"Usuário 1: {perfil1['nome']}, Amigos: {perfil1['amigos']}")
    print(f"Usuário 2: {perfil2['nome']}, Amigos: {perfil2['amigos']}")
    print(f"Amigos em comum: {amigos_comuns}" if amigos_comuns else "Não há amigos em comum.")

def main():
    print("Esta é a questão: Amigos em Comum")
    amigos_em_comum(perfis)

