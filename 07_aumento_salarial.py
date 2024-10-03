'''
#comentario em Titulo: Estudo "if" usando o calculo da media
Autor: Camila Rodrigues
Data: 26/09/2024
Descrição: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
salário, sabendo-se que:
Salário < R$ 1000,00 aumento de 25%.
Salário >=R$ 1000,00 e &lt; R$ 2000,00 aumento de 15%.
Salário >= R$ 2000,00 aumento de 10%. Algoritmo quecalcula a média e apresenta o status de aprovado, 
           média aritimética de 4 notas e apresenta reprovado ou recuperação.
        
'''        
#entrada de dados
salario = float(input('digite o salario'))
# processamento de dados
if salario <1000:
    salario_reajuste = salario * 1.25

if salario >= 1000 and salario < 2000:
    reajuste = salario * 0.15 
    salario_reajuste = salario + reajuste

if salario >= 2000:
    salario_reajuste = salario * 1.1

#saida de dados
print ('Seu novo salario:', salario_reajuste)