'''
Faça um algoritmo que receba três notas de um aluno como parâmetros
e o tipo da média que deverá ser calculada.
Se o tipo da média for "A" a função calcula a média aritmética das
notas do aluno, se for "P" a função calcula a média ponderada
pesos 5, 3 e 2. A média calculada deve ser devolvida ao programa
principal para, então, ser mostrada.


'''

#variaveis
nota1, nota2, nota3 = 0.0, 0.0, 0.0
media, media_f = 0.0, 0.0
tipo_media = ""

#funcao
def calcula_media(n1, n2, n3, tipo):
    if (tipo == "A"):
        media_f = (n1+n2+n3)/3
    else:
        media_f = (n1*5 + n2*3 + n3*2)/(5+3+2)
    return media_f
    

#algoritmo principal
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))
   
tipo_media = input("Informe o tipo da média \nA - Aritmética \nP - Ponderada :").upper()

media = calcula_media(nota1, nota2, nota3, tipo_media)

print(f"A média do aluno é: {media}")