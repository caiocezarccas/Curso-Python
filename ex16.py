from math import ceil, floor, trunc
num = float(input('Digite qualquer número real: '))
print('O número que você digitou foi: {}'.format(num))
print('Arredondando esse número fica: {}'.format(floor(num)))
print('Arredondando para cima o número fica: {}'.format(ceil(num)))
print('A porção inteira é: {}'.format(trunc(num)))