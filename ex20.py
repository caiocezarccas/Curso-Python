from random import shuffle
nome1 = str(input('Pirmeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
print('Os nomes foram apresentados e iremos sortear.')
shuffle(lista)
print('A ordem de aprensentação será...')
print(lista)