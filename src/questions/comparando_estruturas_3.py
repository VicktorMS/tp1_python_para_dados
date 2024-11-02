# 3 - Comparando Estruturas
"""
Explique, em poucas palavras, as principais diferenças entre uma lista, um dicionário e uma tupla em Python. Dê exemplos de como cada estrutura pode ser usada no contexto da análise de dados do INFwebNET.
"""
########################
resposta = """

Uma lista, um dicionário e uma tupla são tipos diferentes de "caixas", estruturas de dados, em Python, cada uma com seu jeito de funcionar.

- Lista é uma caixa onde você guarda coisas em ordem e pode mexer nos itens depois (adicionar, remover, mudar). Em um contexto como o INFwebNET, uma lista pode armazenar os nomes dos usuários que estão online, por exemplo: usuarios_online = ["João", "Ana", "Carlos"].

- No dicionário cada item tem um nome (chave), como uma etiqueta, e um valor associado a essa chave. É ótimo para organizar dados com informações mais específicas, como o perfil de um usuário. Exemplo: perfil_usuario = {"nome": "João", "idade": 25, "cidade": "Rio de Janeiro"}.

- A tupla é quase uma lista, mas você não pode mexer nos itens depois de criada. Ela é útil para dados que não mudam, como uma localização fixa de um usuário. Exemplo: localizacao = ("Rio de Janeiro", "RJ").

"""
def main():
    print("Esta é a questão: Comparando Estruturas")
    print(resposta)