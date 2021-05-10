print('Olá seja bem-vindo(a)')
nome = input('Qual o seu nome? ')
print('É uma prazer em te conhecer {}!'.format(nome))
n1 = int(input('{}, digite um número: '.format(nome)))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é: {}!'.format(n1, n2, s))
