print('Olá, iremos cacular a sua média: ')
nome = input('Digite o seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
print('Irei calcular...')
media = (nota1 + nota2) / 2
print('{}, a sua média é : {:.1f}'.format(nome, media))
if media >= 7:
    print('PARABÉNS!')
else:
    print('{}, PRECISA ESTUDAR MAIS!'.format(nome))
