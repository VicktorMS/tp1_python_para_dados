from .carregando_dados_5 import perfis_arquivo as perfis

# 8 - Verificando Conexões
"""
Crie um programa que permita verificar se um determinado usuário foi adicionado como amigo de mais de 4 usuários. Caso tenha, exiba uma mensagem afirmando que o usuário é "popular".
"""
########################

def verificar_popularidade(perfis, nome_usuario):
    contador = sum(nome_usuario in perfil["amigos"] for perfil in perfis)
    
    if contador > 4:
        print(f"O usuário '{nome_usuario}' é popular! Ele é amigo de {contador} pessoas.")
    else:
        print(f"O usuário '{nome_usuario}' não é popular. Ele é amigo de {contador} pessoas.")

def main():
    print("Esta é a questão: Verificando Conexões")
    nome_usuario = "João" 
    verificar_popularidade(perfis, nome_usuario)