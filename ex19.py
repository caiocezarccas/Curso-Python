from random import choice
nome1 = str(input('Primeiro aluno: '))
num1 = int(input('{}, digite um número: '.format(nome1)))
nome2 = str(input('Segundo aluno: '))
num2 = int(input('{}, digite um número: '.format(nome2)))
nome3 = str(input('Terceiro aluno: '))
num3 = int(input('{}, digite um número: '.format(nome3)))
nome4 = str(input('Quarto aluno: '))
num4 = int(input('{}, digite um número: '.format(nome4)))
print('Iremos fazer o sorteio pelos números que foram digitados.')
lista = [num1, num2, num3, num4]
escolhido = choice(lista)
#print('O número escolhido foi :{}'.format(escolhido))
if (escolhido == num1 and nome1):
    print('O número escolhido foi :{}'.format(escolhido))
    print('{}, vá limpar o quadro!'.format(nome1))
elif (escolhido == num2 and nome2):
    print('O número escolhido foi :{}'.format(escolhido))
    print('{}, vá limpar o quadro!'.format(nome2))
elif (escolhido == num3 and nome3):
    print('O número escolhido foi :{}'.format(escolhido))
    print('{}, vá limpar o quadro!'.format(nome3))
elif (escolhido == num4 and nome4):
    print('O número escolhido foi :{}'.format(escolhido))
    print('{}, vá limpar o quadro!'.format(nome4))


