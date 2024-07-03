'''
Criar um algoritmo que leia 10 números pelo
teclado e exiba os números na ordem inversa da
que os números foram digitados.


'''

#variaveis
vet=[0]*10
cont = 0

#algoritmo
for cont in range(0,10,1):
   vet[cont] = int(input(f"Informe o número {cont+1}: "))

print("=====Mostrando o Vetor na ordem inversa=====")
for cont in range(9,-1,-1):
   print(f"{vet[cont]} ", end=' ')