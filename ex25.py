print('Será que seu nome tem "Silva"? ')
nome = str(input('Digite que para tirar minha dúvida: ')).strip()
'''separando = nome.split()
if (nome == 'Silva' in separando):
    print('Silva' in separando)
elif (nome == 'silva'):
    print('silva' in separando)
else:
    print('SILVA' in separando)'''
print('Será que tem Silva? {} '.format('SILVA' in nome.upper()))