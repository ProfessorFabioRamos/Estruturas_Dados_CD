import math

a = 3
b = 2

# Operadores Aritiméticos
'''
print(a + b)        #Adição
print(a - b)        #Subtração
print(a * b)        #Multiplicação
print(a / b)        #Divisão
print(a % b)        #Divisão que retorna o resto
print(a // b)       #Divisão que retorna a parte inteira
print(a ** b)       #Potenciação
print(a ** 0.5)     #Raiz quadrada
print(math.sqrt(9)) #Raiz quadrada com biblioteca

#Operadores Lógicos
print(a > b)            #Maior
print(a >= b)           #Maior ou igual
print(a < b)            #Menor
print(a <= b)           #Menor ou igual
print(a == b)           #Igual
print(a != b)           #Diferente
print(a > b and a > 0)  #E(and)
print(a > b or a < 0)   #Ou(or)
'''

'''
PESO_MAXIMO = 120
PESO_LIMITE = 500

peso = float(input("Bem-vindo ao parque aquático, digite seu peso: "))
print(peso)

if peso >= PESO_MAXIMO and peso < PESO_LIMITE:
    print("Não é permitido utilizar o tobogã!!!")
elif peso > 0 and peso < PESO_MAXIMO:
    print("É permitido utilizar o tobogã.")
else:
    print("Peso inválido")
'''

'''
fruta = input("Digite o nome de uma fruta: ")
fruta = str.lower(fruta)

match fruta:
    case "banana":
        print("Amarelo")
    case "maça":
        print("Vermelho")
    case "abacate":
        print("Verde")
    case "açai":
        print("Roxo")
    case defaut:
        print("Cor indisponível")
'''
# Recebe 10 numeros com input e faz o somatório de todos

soma = 0
repeticoes = 10

for i in range(0,repeticoes):
    numero = float(input(f"Digite o numero {i+1}: "))
    soma += numero

print("A soma de todos os números é:",soma)
media = soma/repeticoes
print("A média de todos os números é:",media)


#print("Número: "+str(i))  # Concatenação com + (necessário converterpara string)
#print("Número:",i)   # Concatenação com ,(adiciona espaço)