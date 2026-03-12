# Estruturas de dados lineares
# Dicionário {}
'''
dic_vazio = {}
dic_vazio_2 = dict()

# Par chave:valor
aluno = {
    "nome":"Henrique",
    "idade": 26,
    "curso":"Ciência de Dados e ML",
    "ativo": True
}
print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])
print(aluno["ativo"])
# print(aluno["semestre"]) # Gera erro se não existir a chave
name = aluno.get("nome")
print(name)
semestre = aluno.get("semestre") # Get retorna None se não existir
print(semestre)

# Criando dicionário a partir de listas
chaves = ["id","status","taxa_acerto"]
valores = [101,"ativo",0.95]
modelo_IA = dict(zip(chaves,valores))
print(modelo_IA)
'''

# Adicionar e modificar valores
perfil_gamificacao = {"usuario":"ninja", "pontos":500}
perfil_gamificacao["nivel"] = "Senior" # Nova chave com valor
perfil_gamificacao["pontos"] = 550     # Novo valor para chave existente
perfil_gamificacao.update(
    {"pontos":1000, "ultimoLogin": "12-03-26","nivel": "Mestre"})
print(perfil_gamificacao)
