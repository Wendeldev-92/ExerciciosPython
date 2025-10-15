# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possiveis sobre ele.

a = input('Digite algo: ')
print("O tipo primitivo desse valor é{}".format(type(a)))
print("Só tem espaços? {}".format(a.isspace()))
print("É um numero? {}".format(a.isnumeric()))
print("É alfabético? {}".format(a.isalpha()))
print("Esta em Maiusculas? {}".format(a.isupper()))
print("Esta em minusculas? {}".format(a.islower()))
print("Esta capitalizada? {}".format(a.istitle()))


