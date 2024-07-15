from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Insira o ano de seu nascimento: '))
idade = anoAtual - anoNascimento
temposDePaz = str(input('Condição atual é de tempos de paz? (Sim/Não): ').lower())
    
print(f'\n ================================= \n SITUAÇÃO MILITAR \n ================================= \n')

if((idade >= 17) and (idade <= 18) and (temposDePaz == 'sim')):
    print(f'\n ================================= \n Estamos em tempo de paz \n ================================= \n Você tem {idade} anos e pode se alistar voluntariamente. \n ================================= \n')
else:
    if(temposDePaz == 'sim'):
        print(f'\n ================================= \n Estamos em tempo de paz \n ================================= \n Você tem {idade} anos e está fora do alistamento militar. \n ================================= \n')
        
if((idade >= 18) and (idade < 19)):
    print(f'\n ================================= \n Você pode ser convocado! \n ================================= \n')
else:
    if((idade >= 19)):
        print(f'\n ================================= \n Você pode ser convocado CASO seja necessário \n ================================= \n')
    
if((idade < 17)):
    print(f' Você ainda não possui idade suficiente para se alistar \n ================================= \n Aliste-se em {anoNascimento + 17} \n ================================= \n')
        
if((idade >= 17) and (temposDePaz == 'não')):
    print(f' Estamos em tempos de guerra \n ================================= \n Você foi convocado aos {idade} anos. \n ================================= \n')
        
if(idade > 45):
    print(f' Você está livre de convocações.')    
    

