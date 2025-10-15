# 6ª) Crie um algoritmo que leia um numero e mostre na tela o seu dobro
# triplo e raiz quadrada.

n = int(input('Escreva um numero para descobrir, o seu dobro, o seu triplo e sua raiz quadrada: '))
dobro = n * 2
triplo = n * 3
rq = n ** 2
print('O dobro de {} é {}'.format(n, dobro), '\nO triplo de {} é {}'.format(n, triplo), '\ne a Raiz Quad de {} é {}'.format(n, rq))
