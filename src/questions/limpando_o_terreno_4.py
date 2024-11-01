from .perfil_2 import perfis as perfis_originais

# 4 - Limpando o terreno
"""
Alguns usuários do INFwebNET forneceram informações incompletas. Remova da lista perfis todos os perfis que não possuem as informações de "nome" ou "cidade". 
Mantenha a lista perfis original intacta, criando uma nova lista chamada perfis_validos para armazenar os perfis válidos.
"""
def validar_localizacao(localizacao):
    """
    Verifica se a localizacao é uma tupla contendo duas strings não vazias.
    Retorna True se ambas as strings (cidade e estado) forem válidas, caso contrário, False.
    """
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


def main():
    print("Esta é a questão: Limpando o terreno")
    
    perfis_invalidos = [
        {"nome": 'Sheldon', "idade": 23, "localizacao": ('Pé fundo', '')},
        {"nome": 'Done Neide', "idade": 23, "localizacao": None},
        {"nome": 'Armando', "idade": 23, "localizacao": (None, 'São Paulo')},
    ]

    # Populando perfis com perfis inválidos para resolução da questão
    todos_perfis = perfis_originais + perfis_invalidos

    perfis_validos = []
    for perfil in todos_perfis:
        # Condições explícitas
        nome_presente = perfil.get("nome") is not None
        localizacao_presente = perfil.get("localizacao") is not None
        localizacao_valida = validar_localizacao(perfil["localizacao"])

        # Adiciona o perfil à lista de perfis válidos se todas as condições forem atendidas
        if nome_presente and localizacao_presente and localizacao_valida:
            perfis_validos.append(perfil)

    # Exibindo perfis originais, perfis inválidos, e perfis válidos
    print("Perfis válidos:", perfis_validos)
