valor_produto = int(input('Digite o valor do produto: '))
print('Iremos analisar o desconto.')
desconto = (valor_produto*5)/100
valor_final = valor_produto - desconto
print('O valor do desconto ficou de {:.2f}RS$, e o valor do produto de {}RS$.\n O valor final é de: {}'.format(desconto, valor_produto, valor_final))
