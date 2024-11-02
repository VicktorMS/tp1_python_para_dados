from .perfil_2 import perfis as perfis_originais
# 4 - Limpando o terreno
"""
Alguns usuários do INFwebNET forneceram informações incompletas. Remova da lista perfis todos os perfis que não possuem as informações de "nome" ou "cidade". 
Mantenha a lista perfis original intacta, criando uma nova lista chamada perfis_validos para armazenar os perfis válidos.
"""

def validar_localizacao(localizacao):
    if not isinstance(localizacao, tuple):
        return False
    if len(localizacao) != 2:
        return False
    cidade, estado = localizacao
    if not isinstance(cidade, str) or not cidade.strip():
        return False
    if not isinstance(estado, str) or not estado.strip():
        return False
    return True

def validar_perfis(perfis):
    perfis_validos = []
    for perfil in perfis:
        nome_presente = perfil.get("nome") is not None
        localizacao_presente = perfil.get("localizacao") is not None
        localizacao_valida = validar_localizacao(perfil["localizacao"])
        if nome_presente and localizacao_presente and localizacao_valida:
            perfis_validos.append(perfil)
    return perfis_validos

# Definindo `perfis_validos` para exportação
perfis_invalidos = [
    {"nome": 'Sheldon', "idade": 23, "localizacao": ('Pé fundo', '')},
    {"nome": 'Done Neide', "idade": 23, "localizacao": None},
    {"nome": 'Armando', "idade": 23, "localizacao": (None, 'São Paulo')},
]
todos_perfis = perfis_originais + perfis_invalidos
perfis_validos = validar_perfis(todos_perfis)


def main():
    print("Esta é a questão: Limpando o terreno")
    print("Perfis válidos:", perfis_validos)
