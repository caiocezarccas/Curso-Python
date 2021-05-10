velocidade = float(input('Digite a velocidade que você estava: '))

if (velocidade >= 81):
    print('''Você ultrapassou o limite de velocidade!
Você será MULTADO e a multa é 7,00R$ por Km/h ultrapassado.''')
    valor_km = 7.00
    multa = (velocidade - 80)* valor_km
    acréscimo = 400
    valor_total = multa + acréscimo
    print('Dirija com segurança. Use o cinto, e prossiga sua viagem!')
    print('Sua velocidade registrada foi de: {}Km/h'.format(velocidade))
    print('O valor por Km/h é : {}R$'.format(valor_km))
    print('A multa será do valor de: {}R$ e terá um acréscimo de : {}R$'.format(multa, acréscimo))
    print('Valor total a pagar: {:.2f}R$'.format(valor_total))
else:
    print('Dirija com segurança. Use o cinto, e prossiga sua viagem!')
    print('Sua velocidade registrada foi de: {}Km/h'.format(velocidade))
    print('Velocidade dentro dos padrões da via!')