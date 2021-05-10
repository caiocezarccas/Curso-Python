print('Vamos calcular o valor baseado na forma de pagamento.')
preço = float(input('Digite o valor do produto: '))
cartão = (preço*15)/100
boleto = (preço*10)/100
preço_cartão = cartão + preço
preço_boleto = preço - boleto
print('Já calculei o valor...')
pagamento = input('O pagamento será cartão ou boleto ?')
if (pagamento == 'boleto'):
    print('O valor do produto é {}R$, e o desconto foi de: {}R$'.format(preço, boleto))
    print('Com desconto de 10% fica no valor total de: {}R$'.format(preço_boleto))
elif (pagamento == 'cartão'):
    print('O valor do produto é {}R$, e no cartão tem um acréscimo fica no valor de: {}R$.'.format(preço, cartão))
    print('Com acréscimo fica no total de {}R$.'.format(preço_cartão))

