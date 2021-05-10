'''distância = float(input('Digite a distância da sua viagem: '))
km_rodado1 = 0.50
km_rodado2 = 0.45
print('Irei lhe ajudar com algumas informações para lhe ajudar na viagem.')
print('Já que você me disse a distância vou fazer alguns calculos...')
if (distância <= 200):
    resultado = distância * km_rodado1
    print('O cáculo será {} x {}'.format(distância, km_rodado1))
    print('A distância será menor que 200Km então o valor irá ficar: {}R$'.format(distância, resultado))
else:
    resultado = distância * km_rodado2
    print('Será maior que 200Km, a distância é : {}Km'.format(distância))
    print('O cáculo será {} x {}'.format(distância, km_rodado2))
    print('O total a pagar é: {}R$'.format(resultado))'''
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
