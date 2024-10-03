'''
#Comentario em Titulo: Categoria pela idade
Autor: Camila Rodrigues
Data: 01/10/2024
Descrição: Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que
pertence, de acordo com a tabela abaixo.
        
'''  
#entrada de dados

idade = int(input('Digite a Idade'))
Categoria = 'faixa_etaria'

#processamento de dados

if idade <= 12:
    faixa_etaria = 'Criança'
elif idade >= 13 and idade <= 17:
    faixa_etaria = 'Adolecente'
elif idade >= 18 and idade <= 59:
    faixa_etaria = 'Adulto'
elif idade >= 60:
    faixa_etaria ='Especialista'

#saida de dados
print(faixa_etaria)