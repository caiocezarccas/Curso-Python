from time import sleep
número = int(input('Digite um número: '))
resultado = número % 2
print('Obtendo alguns resultados sobre o número...')
print('Processando...')
sleep(2)
if (resultado == 0):
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é ÍMPAR!'.format(número))
