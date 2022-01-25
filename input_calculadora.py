numero_1 = input("Digite um número: ")
numero_2 = input("Digite um número a ser somado pelo primeiro: ")

print(numero_1 + numero_2)

print("Algo deu errado! Vamos tentar de novo...")

# O resultado foi a soma de duas strings, porque o valor não foi convertido para int

# Deve-ser converter o valor para int para que a adição seja feita de forma correta


numero_1 = input("Digite um número: ")
numero_2 = input("Digite um número a ser somado pelo primeiro: ")

numero_1 = int(numero_1)
numero_2 = int(numero_2)


"""Também pode ser feito de uma forma mais direta:

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número a ser somado pelo primeiro: "))

"""

print(numero_1 + numero_2)

print(";)")

