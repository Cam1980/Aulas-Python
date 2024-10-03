'''
#Titulo: Dólar
#Autor: Camila Rodrigues
#Data: 19/09/2024
#Descrição: Faça um algoritmo qu um  valor na moeda real (R$), 
#           a cotação da conversão Real para Dólar, e apresenta
#           a quantidade desse valor em dólar ($)
#
            Exemplo de execução
            Insira o valor em real: 5000
            Insira o valor cotação do dia: 5
            R$5000,00 equivalente $1000,00
'''            

#entrada de dados 
moeda_real = 5000
cotacao_dia= 5
#processamento de dados
equivalente = 5000/5
moeda_dolar = moeda_real / cotacao_dia
#saida de dados
print(equivalente)
print(f'R${moeda_real} equivalente $ {moeda_dolar}')#format