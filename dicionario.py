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

'''
# Adicionar e modificar valores
perfil_gamificacao = {"usuario":"ninja", "pontos":500}
perfil_gamificacao["nivel"] = "Senior" # Nova chave com valor
perfil_gamificacao["pontos"] = 550     # Novo valor para chave existente
perfil_gamificacao.update(
    {"pontos":1000, "ultimoLogin": "12-03-26","nivel": "Mestre"})
print(perfil_gamificacao)
'''

'''
# Removendo elementos
carrinho_loja_informatica = {
    "mouse":79.99,
    "teclado_gamer":249.99,
    "monitor": 1499.00,
    "placa_RTX":15000.75
}
print(carrinho_loja_informatica) 

# Anular valor de chave
carrinho_loja_informatica["teclado_gamer"] = None

# Remove e retorna valor
preco_mouse = carrinho_loja_informatica.pop("mouse")
print(preco_mouse)
print(carrinho_loja_informatica) 

# Remove sem retornar 
del carrinho_loja_informatica["teclado_gamer"]
print(carrinho_loja_informatica) 

# Remove último par chave/valor como tupla
ultimo_item = carrinho_loja_informatica.popitem()
print(ultimo_item)
print(carrinho_loja_informatica) 

# Limpar dicionário
carrinho_loja_informatica.clear()
print(carrinho_loja_informatica)
'''

'''
# Iteração (laços de repetição)
faturamento = {"jan": 1000, "fev": 1500, "mar": 1800}

for mes in faturamento.keys():          # Iteração apenas nas chaves
    print(mes)

for fatu in faturamento.values():       # Iteração apenas nos valores
    print(fatu)

for mes,fatu in faturamento.items():   # Iteração no par chave/valor
    print(f"No mês {mes} o valor foi {fatu}")
'''

