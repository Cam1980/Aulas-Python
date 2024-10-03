'''
#comentario em Titulo: Mês por extenso
Autor: Camila Rodrigues
Data: 26/09/2024
Descrição: Faça um programa que receba o mês em número e apresente-o por extenso.
        
'''        
#entrada de dados
mes = int(input('inserir o mês:'))
# recebo o valor do usuário e converto para inteiro
#processamento de dados
if mes == 1:
    mes_extenso = 'Janeiro'
elif mes == 2:
    mes_extenso = 'Fevereiro'
elif mes == 3:
    mes_extenso = 'Março'
elif mes == 4:
    mes_extenso = 'Abril'
elif mes == 5:
    mes_extenso = 'Maio'
elif mes == 6:
    mes_extenso = 'Junho'
elif mes == 7:
    mes_extenso = 'Julho'
elif mes == 8:
    mes_extenso = 'Agosto'
elif mes == 9:
    mes_extenso = 'setembro'
elif mes == 10:
    mes_extenso = 'Outubro'
elif mes == 11:
    mes_extenso = 'Novembro'
elif mes == 12:
    mes_extenso = 'Dezembro'
else:
    mes_extenso = ' Mês não existe'

#saida de dados
print(mes_extenso)

# No Python, o comando else é executado quando nenhuma das condições anteriores (if ou elif) for verdadeira. 
# A estrutura if-else é uma estrutura condicional que permite que um programa tome 
# decisões com base em condições específicas. A gramática geral é: 
# if(condição){ faça isso } else {faça aquilo}