# Você está analisando palavras e deseja saber quantas vogais cada palavra contém. Escreva um programa que conte e exiba o número de vogais em uma palavra inserida pelo usuário.


palavra = input("Digite uma palavra para contar as vogais: ")
vogais = 'aeiouAEIOU'
contador_vogais = 0
for letra in palavra:
    if letra in vogais:
        contador_vogais += 1
print(f"A palavra '{palavra}' contém {contador_vogais} vogais.")
