venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']
meta = 50
i = 0

while i < len(venda):
    if venda[i] >= meta:
        print(f"O vendedor {vendedores[i]} bateu a meta com {venda[i]} vendas.")
    i += 1


    