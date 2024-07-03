'''
Você está fazendo um trabalho de classificação de solo. Após colher uma
amostra e verificar a quantidade de pontos de água presente nela, classificou
a amostra em:
    Rochosa: se menos ou igual a 10 pontos de água
    Firme: se mais do 10 e menos ou igual a 40 pontos
    Pantanosa: se mais do 40 e menos ou igual a 80 pontos
    Quantidade Inválida: se mais do que 80 pontos

'''

#variaveis
agua = 0

#programa
agua = int(input("Digite a quantidade de pontos de água encontrado: "))

#Forma 1
if(agua <= 10):
    print("O solo é rochoso!!!")
else:
    if((agua > 10) and (agua <= 40)):
        print("O solo é firme!!!")
    else:
        if((agua > 40) and (agua <=80)):
            print("O solo é pantanoso!!!")
        else:
            print("Quantidade de água inválida!!!")



#Forma 2
if(agua <= 10):
    print("O solo é rochoso!!!")
elif((agua > 10) and (agua <= 40)):
    print("O solo é firme!!!")
elif((agua > 40) and (agua <=80)):
    print("O solo é pantanoso!!!")
else:
    print("Quantidade de água inválida!!!")