# O exercito te contratou para criar um programa que mostre aos brasileiros a situação deles em relação ao serviço militar. Segundo o exército:

#    - Em tempos de paz, a Partir dos 17 anos qualquer brasileiro pode se alistar como voluntário
#    - Em tempos de paz a convocação pode ocorrer no dia primeiro de janeiro do ano em que a pessoa completa 
# 18 anos de idade até 31 de dezembro do ano em que a pessoa completa 45 anos
#    - Em tempos de guerra qualquer brasileiro pode ser convocado a partir dos 17 anos.

#   A partir dos dados acima crie um programa que mostre de forma clara em qual 
#   situação uma pessoa se encontra. O exercito solicitou que mesmo que alguém não esteja em idade de alistamento, seja informado em que ano o alistamento deve ocorrer.

from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Insira o ano de seu nascimento: '))
idade = anoAtual - anoNascimento
temposDePaz = True
    
print(f'\n ================================= \n SITUAÇÃO MILITAR \n ================================= \n')

if((idade >= 17) and (idade <= 18) and (temposDePaz == True)):
    print(f'\n ================================= \n Estamos em tempo de paz \n ================================= \n Você tem {idade} anos e pode se alistar voluntariamente. \n ================================= \n')
else:
    if(temposDePaz == True):
        print(f'\n ================================= \n Estamos em tempo de paz \n ================================= \n Você tem {idade} anos e está fora do alistamento militar. \n ================================= \n')
        
if((idade >= 18) and (idade < 19)):
    print(f'\n ================================= \n Você pode ser convocado! \n ================================= \n')
else:
    if((idade >= 19)):
        print(f'\n ================================= \n Você pode ser convocado CASO seja necessário \n ================================= \n')
    
if((idade < 17)):
    print(f' Você ainda não possui idade suficiente para se alistar \n ================================= \n aliste-se em {anoNascimento + 17} \n ================================= \n')
        
if((idade >= 17) and (temposDePaz == False)):
    print(f' Estamos em tempos de guerra \n ================================= \n Você foi convocado aos {idade}. \n ================================= \n')
        
if(idade > 45):
    print(f' Você está livre de convocações.')    
    

