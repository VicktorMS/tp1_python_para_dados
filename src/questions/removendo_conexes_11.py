from .limpando_o_terreno_4 import perfis_validos
# 11 - Removendo Conexões
"""
Permita que o usuário remova um amigo da lista de conexões de um membro do INFwebNET específico no dicionário criado no exercício 4.
"""
########################

# NOTE - Na questão 4 usuários não tem amigos
def remover_amigo(perfis, nome_usuario, nome_amigo):
    for perfil in perfis:
        if perfil["nome"] == nome_usuario:
            if nome_amigo in perfil["amigos"]:
                perfil["amigos"].remove(nome_amigo)
                print(f"Amigo '{nome_amigo}' removido de '{nome_usuario}'.")
            else:
                print(f"'{nome_amigo}' não está na lista de amigos de '{nome_usuario}'.")
            return perfil
    print(f"Usuário '{nome_usuario}' não encontrado.")
    return None

def main():
    print("Esta é a questão: Removendo Conexões")
    nome_usuario = "Sheldon"  # Ususario seleciona
    nome_amigo = "Carlos"  # Amigo a ser removido
    perfil_atualizado = remover_amigo(perfis_validos, nome_usuario, nome_amigo)
    
    if perfil_atualizado:
        print("Perfil atualizado:", perfil_atualizado)