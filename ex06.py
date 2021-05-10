num = float(input('Digite um número e irei lhe mostrar algumas informações sobre ele: '))
dobro = num * 2
triplo = num * 3
rq = num**(1/2) #pow(num,(1/2))
print('Já obtive as informações sobre o número escolhido.')
print('O número digitado foi: {}, e seu dobro é: {}'.format(num, dobro))
print('O número digitado foi: {}, e seu triplo é: {},'.format(num, triplo))
print('O número digitado foi: {}, e a sua raiz quadrada é: {:.2f}'.format(num, rq))
print('Essa foi as informações que queria lhe mostrar!')
