'''
#Comentario em Titulo: Ocupação de um funcionário
Autor: Camila Rodrigues
Data: 01/10/2024
Descrição: Faça um programa para exibir a ocupação de um funcionário a 
           partir de seu código de
           profissão, de acordo com a tabela abaixo;
           1 - Matemático
           2 - Analista de Sistemas
           3 - Físico
           4 - Arquiteto
           5 - Piloto deAeronaves
        
'''  
#Entrada de dados
codigo = int(input('Inserir Código de Profissão'))
#Processamento de dados
if codigo == 1:
    ocupação = 'Matemática'
elif codigo == 2:
    ocupação = 'Analista de Sistema'
elif codigo == 3:
    ocupação = 'Físico'
elif codigo == 4:
    ocupação = 'Arquiteto'
elif codigo == 5:
    ocupação = ' Piloto de Aeronaves'


#Saida de dados
print (ocupação)