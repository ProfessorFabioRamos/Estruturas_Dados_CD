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

'''
# Dicionário aninhado , similar a json
banco_de_dados = {
    "cliente_1":{
        "nome": "Ana",
        "compras": ["Livro", "Caneta"]
    },
    "cliente_2":{
        "nome": "Bruno",
        "compras": ["Caderno", "Tesoura"]
    },
    "cliente_3":{
        "nome": "Caio",
        "compras": ["Borracha", "Livro"]
    }
}
primeira_compra_ana =  banco_de_dados["cliente_1"]["compras"][0]
print(primeira_compra_ana)
compras_bruno = banco_de_dados["cliente_2"]["compras"]
print(compras_bruno)
nome_cliente_3 = banco_de_dados["cliente_3"]["nome"]
print(nome_cliente_3)
'''

'''
# Mesclar dicionários
dict1 = {"a":1, "b":2, "c":3}
dict2 = {"d":4, "e":5, "f":6}

# | Mescla dicionários a partir do Python 3.9
dict3 = dict1 | dict2  
print(dict3)

# Versão antiga de mesclagem
dict4 = {**dict1,**dict2}
print(dict4)
'''

# Operação/Compreensão em dicionários
numeros = [1,2,3,4,5,6,7,8,9]
quadrados = {x:x**2 for x in numeros} # x é a chave e valor é a potência de x
print(quadrados)

salarios = {"João":3000, "Maria": 6000, "Pedro":4500}
novos_salarios = {
    nome:valor *1.1 for nome,valor in salarios.items() if valor < 5000
}
print(novos_salarios)
