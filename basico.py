#print basico (textos ficam sempre em aspas duplas "")

print("hello, world!")

#no print os numeros diretamente (10 como numero inteiro e 9,5 como numero com virgula)

print(10)
print(9,5)

#Tbm faz calculos simples como a calculadora

#Soma
print(5 + 5)

#Subtração
print(5-5)

#Multiplicação
print(5*5)

#divisão
print(5/5)

#resto da divisão
print(5%4)
print(5%5) 

#variaveis podem guardar valores

idade = 20
nome = "vinicius"

print(idade, nome)

#pode usar vairaveis para frases
print("Olá! Meu nome é ", nome, "e eu tenho ", idade, " anos.")

#entrada de dados com input (E tudo que vem pelo input é em formato de string)

nome2 = input("Digite seu nome:")
print("Olá", nome2)

idade2 = int(input("Digite sua idade:"))

#float só aceita numero com ponto e nao com virgula 
numerodecimal = float(input("Digite um numero com ponto:"))

print(idade2 + 1)
print(numerodecimal)

#execicio para finalizar a revisao basico do basico 
#Pergunte o nome
#Pergunte a idade
#Mostre:

nome_ex = input("Digite seu nome")
idade_ex = int(input("Digite sua idade"))

print("Olá ", nome_ex, " ano que vem você terá ", idade_ex + 1, " ano")