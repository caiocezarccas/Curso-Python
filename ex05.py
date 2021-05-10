print('Olá, vamos fazer um programa simples.')
print('O programa consiste é fazer sucessor e antecessor.')
num = int(input('Digite um número: '))
print('OK, recebi o número que você deseja saber...')
print('Estou preparando o cálcula para mostrar...')
ant = num - 1
suc = num + 1
print('O número digitado foi: {}, e o seu antecessor é: {}, e o sucessor é: {}'.format(num, ant, suc))
var = input('Acertei? (S/N)')
if var == 'S' or var == 's':
    print('Obrigado pela resposta, foi um prazer em ajudar!')
elif var == 'N' or var == 'n':
    print('Que pena... irei melhorar para acerta na próxima!')
