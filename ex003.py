'''
Crie um programa que leia dois numeros
e mostre a soma entre eles.
'''
print('=' * 20, "Exemplo com o tipo INT")
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = num1 + num2

print('A soma entre {} e {} é igual a: {}'.format(num1, num2, soma))

print('=' * 20, "Exemplo com o tipo FLOAT")
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
soma = num1 + num2

print("O resultado de {} + {} = {}".format(num1, num2, soma))