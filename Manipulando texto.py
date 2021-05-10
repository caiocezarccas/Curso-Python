'''Fatiamento de String;
    Análise:
len();
count();
find();
in;
   - Transformação:
-replace();
-upper();
- lower();
- capitalize();
- title();
- strip();
- rtrip();
- lstrip();
   - Divisão:
- split();
- Junção:
   - join();
   '''

'''Frase = 'Curso em vídeo Python '
Fatiamento= [9:21]
Fatiamento= [9:21:2] para pular duas casas
frase [:5] omissão do inicio então vai do 0 até o 4
frase [15:] incando o inicio então vai do 15 até o final da frase
frase[9::3] do 9 até o final pulando de 3 até o final'''

'''Análise
len(frase) mostrando o len é o comprimento da frase, len mostra o comprimento
frase.count('o') o programar conta quantas vezes aparece letra
frase.count('o',0,13) considera do 0 até o 12 e ele vai colocar quantas aprece a letra 'O'
frase.find('deo') vai dizer quantas vezes encontrou essa junção de palavras
e diz tbm o começo apartir dessa junção
frase.find('Android') se colocar um string que não existe ele vai retornar -1
 então logo -1 não que não existe
'Curso' in frase ele vai dizer se existe ou não se tiver ele escrevrar 'True'''''

'''Transformação
frase.replace('Python','Android') Aonde tiver python ele substitui por Android
ele substitiu de uma forma secundária
frase.upper() Vai transformar em maiúsculo
frase.lower() Vai transformar em minúsculo
frase.capitalize() Ele joga os caracters para minúsculo e só o primeiro caractere joga para maiúsculo e todo resto em mnústulo
frase.title() analisa mais profundo e verifica as palavras  e aonde tiver quebra de espaço coloca em maiúsculo'''

'''Exemplo
 |    Aprenda Python  |
frase.strip() remove espaços inúteis antes e depois da frase
frase.rstrip() remove só os últimos espaços
frase.lstripo() remove os espaços da esquerda e mantém os da direita'''

'''Divisão de string
frase.split() vai fazer uma divisão aonde houver espaços, gera uma lista
com todas os caracteres. Dividir em uma lista, aonde vai ser dividido em espaços'''

'''Junção
 '-'.join(frase) Vai juntar todos os elementos de frase e vai gerar uma string única
 separando apenas por '-', caso queria a espaço em branco é só deixar o
 espaço entre as aspas'''



