
import random
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    palpite = int(input("Digite seu palpite (entre 1 e 100): "))
    tentativas += 1
    if palpite < numero_secreto:
        print("O número é maior. Tente novamente.")
    elif palpite > numero_secreto:
        print("O número é menor. Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
        break

