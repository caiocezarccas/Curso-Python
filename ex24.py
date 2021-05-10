print('Me diga um nome de cidade e irei lhe dizer se começa com "Santo"')
cidade = str(input('Digite nome da cidade: ')).strip()
'''separando = cidade.split()
if (cidade == 'Santo'):
    print('Santo' in separando[0])
elif (cidade == 'santo'):
    print('santo' in separando[0])
else:
    print('SANTO' in separando[0])'''
print(cidade[:5].upper() == 'SANTO')
