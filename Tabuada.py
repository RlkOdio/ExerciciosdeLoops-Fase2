# Você é um estudante tentando aprender a tabuada. 
# Escreva um programa que peça um número ao usuário e, em seguida, exiba a tabuada desse número, de 1 a 10.

numero = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
    