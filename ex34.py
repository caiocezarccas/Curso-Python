salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    valor_aumento = salário * 15 / 100
    novo_salário = salário + valor_aumento
else:
    valor_aumento = salário * 10 / 100
    novo_salário = salário + valor_aumento
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário,novo_salário))
