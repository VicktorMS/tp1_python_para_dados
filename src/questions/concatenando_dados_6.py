from .carregando_dados_5 import perfis_arquivo 
from .aquecendo_os_motores_1 import usuarios
from .perfil_2 import perfis as perfis2

# 6 - Concatenando dados
"""
Com os dados carregados no exercício anterior, adicione os usuários dos exercícios 1 e 2, definindo um padrão para lidar com os dados ausentes e salve estas informações em um arquivo "rede_INFNET.txt".
"""
########################

def padronizar_dados(perfil):
    perfil_padronizado = {
        "nome": perfil.get("nome", "N/A"),
        "idade": perfil.get("idade", "N/A"),
        "cidade": perfil.get("localizacao", ("N/A", "N/A"))[0],
        "estado": perfil.get("localizacao", ("N/A", "N/A"))[1],
        "amigos": perfil.get("amigos", []),
    }
    return perfil_padronizado

def converter_usuarios_para_perfis(usuarios):
    return [
        {
            "nome": usuario[0] if usuario[0] else "N/A",
            "idade": usuario[1] if isinstance(usuario[1], int) else "N/A",
            "cidade": usuario[2] if usuario[2] else "N/A",
            "estado": usuario[3] if usuario[3] else "N/A",
            "amigos": []
        }
        for usuario in usuarios
    ]

def salvar_em_arquivo(perfis, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo:
        for perfil in perfis:
            linha = f"{perfil['nome']}?{perfil['idade']}?{perfil['cidade']}?{perfil['estado']}?{'?'.join(perfil['amigos'])}\n"
            arquivo.write(linha)
    print(f"Arquivo '{caminho_arquivo}' foi gerado com sucesso.")
def main():
    print("Esta é a questão: Concatenando dados")
    
    perfis_padronizados = [padronizar_dados(perfil) for perfil in perfis_arquivo]
    perfis2_padronizados = [padronizar_dados(perfil) for perfil in perfis2]
    perfis_usuarios = converter_usuarios_para_perfis(usuarios)
    
    todos_perfis = perfis_padronizados + perfis2_padronizados + perfis_usuarios
    salvar_em_arquivo(todos_perfis, "src/data/rede_INFNET.txt")
