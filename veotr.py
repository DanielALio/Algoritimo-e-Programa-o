'''
Faça um algoritmo que leia 30 números reais em um vetor e depois
mostre os números localizados nas posições impares.


'''

#variaveis
vet=[0.0]*30
cont = 0

#algoritmo
for cont in range(0,30,1):
   vet[cont] = int(input(f"Informe o número {cont+1}: "))

print("=====Forma 1 - Mostrando os números nas posições impares=====")
for cont in range(0,30,1):
   if(cont % 2 != 0):
      print(f"{vet[cont]} ", end=' ')


print("=====Forma 2 - Mostrando os números nas posições impares=====")
for cont in range(1,30,2):
   print(f"{vet[cont]} ", end=' ')