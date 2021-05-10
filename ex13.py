nome = input('Digite o seu nome: ')
print('Iremos calcular o seu aumento salarial.')
salario = float(input('Digite o seu salário: '))
print('OK, vamos calcular...')
valor_aumento = (salario*15)/100
valor_final = salario + valor_aumento
print('{},o seu salário atual é: {}RS$, o aumento foi de: {:.2f}.\n O valor final é: {:.2f}RS$'. format(nome, salario, valor_aumento, valor_final))