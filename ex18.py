from math import radians, sin, cos, tan
Ângulo = float(input('Digite o ângulo e lhe daremos a reposta: '))
seno = sin(radians(Ângulo))
cosseno = cos((radians(Ângulo)))
tangente = tan(radians(Ângulo))
print('Já calculei os valores do ângulo digitado. E os valores são: ')
print('O ângulo {} tem o seno {:.2f}'.format(Ângulo, seno))
print('O ângulo {} tem o cosseno {:.2f}'.format(Ângulo, cosseno))
print('O ângulo {} tem a tangente {:.2f}'.format(Ângulo, tangente))
