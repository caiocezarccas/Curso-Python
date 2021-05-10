from math import hypot
ca = int(input('Digite o cateto adjacente: '))
co = int(input('Digite o cateto oposto: '))
hi = (ca ** 2 + co ** 2) **(1/2)
print('Cateto adjacente: {}, Cateto Oposto: {} e a Hipotenusa: {:.2f}'.format(ca, co, hi))
## dois modos diferentes de execução do mesmo resultado
cateto_adjacente = int(input('Cumprimento do cateto adjacente: '))
cateto_oposto = int(input('Cumprimento do cateto oposto: '))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print('O cumprimento da cateto adjacente é : {}'.format(cateto_adjacente))
print('O cumprimento do cateto oposto é: {}'.format(cateto_oposto))
print('Estou calculando.....')
print('Obtive a respota e a hipotenusa é : {:.2f}'.format(hipotenusa))


