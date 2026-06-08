quarto = []
quantidade_pessoas = int(input("Quantas pessoas ficarão no quarto? (1, 2, 3 ou 4): "))
for i in range(quantidade_pessoas):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    cpf = input(f"Digite o CPF da pessoa {i + 1} (formato: cpf:00000000000): ")
    quarto.append([nome, cpf])
print("Lista de hóspedes no quarto:")
for hospede in quarto:
    print(f"Nome: {hospede[0]}, CPF: {hospede[1]}")
