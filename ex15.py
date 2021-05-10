print('Você alguou um carro em nossa loja.')
dias = int(input('Quantos dias com o carro alugado? '))
km = float(input('Quantos Km rodados? '))
print('Se ultrapassar mais de 300Km tera um valor adicional.')
dias_alugados = 60
km_rodado = 0.15
km_rodado2 = 0.30
print('Diária: {}R$'.format(dias_alugados))
print('Menos de 300Km fica: {}R$'.format(km_rodado))
print('Ultrapassando 300Km: {}R$'.format(km_rodado2))
if (km <= 300):
    dias_km = (dias * dias_alugados)+(km_rodado)
    print('Irei calcular com base nas informações...')
    print('A diária custa {}R$, e por Km rodado custa {}R$'.format(dias_alugados, km_rodado))
    print('E cobramos 0.15R$ por Km rodado, com base nessa informações fica no total de:')
    print('{:.2f}R$'.format(dias_km))
else:
    dias_km = (dias * dias_alugados)+(km*km_rodado2)
    print('Irei calcular com base nas informações...')
    print('A diária custa {}R$, e por Km rodado custa {}R$'.format(dias_alugados, km_rodado2))
    print('E cobramos 0.30R$ por Km rodado, com base nessa informações fica no total de:')
    print('{:.2f}R$'.format(dias_km))