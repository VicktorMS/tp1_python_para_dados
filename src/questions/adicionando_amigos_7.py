from .carregando_dados_5 import perfis_arquivo as perfis
# 7 - Adicionando Amigos
"""
Com o dicionário criado no exercício anterior, adicione um novo amigo ao set de amigos de um usuário específico.
"""
########################

# NOTE - O Exercicio anterior pediu para criar um arquivo de texto e não un dicionário
def adicionar_amigo(perfis, nome_usuario, novo_amigo):
    for perfil in perfis:
        if perfil["nome"] == nome_usuario: # Algum tipo de Id seria melhor
            if novo_amigo not in perfil["amigos"]:
                perfil["amigos"].append(novo_amigo)
                print(f"Amigo '{novo_amigo}' adicionado ao usuário '{nome_usuario}'.")
            else:
                print(f"'{novo_amigo}' já é amigo de '{nome_usuario}'.")
            return perfil
    print(f"Usuário '{nome_usuario}' não encontrado.")
    return None

def main():
    print("Esta é a questão: Adicionando Amigos")
    nome_usuario = "João"  
    novo_amigo = "Daniel" 
    perfil_atualizado = adicionar_amigo(perfis, nome_usuario, novo_amigo)
    
    if perfil_atualizado:
        print("Perfil atualizado:", perfil_atualizado)
