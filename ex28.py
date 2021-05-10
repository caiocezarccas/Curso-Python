from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Irei pensar em um número de 0 a 5 e você terá que adivinhar!')
print('Você não irá advinhar hehe...')
print('Pensei no número....')
print('-=-'*20)
num = int(input('Em que número eu pensei?  '))
print('Processando...')
sleep(2.5)
if (num == computador):
    print('Oiaaa... você adivinhou!')
    print('Pensei no número: {}'.format(computador))
elif(num > 5):
    print('Combinamos que iria de 0 a 5 ')
    print('Eu tinha pensando no número: {}'.format(computador))
else:
    print('Avisei que você não iria adivinhar!')
    print('Pensei no número: {}'.format(computador))
