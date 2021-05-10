print('Vamos converter reais para dólares')
dinheiro = float(input('Digite o valor em reais: '))
d = 5.67
res = dinheiro / d
print('O valor em {}R$ é equivalente a {:.2f}US$, valor do dólar atual: {}US$'.format(dinheiro, res, d))
