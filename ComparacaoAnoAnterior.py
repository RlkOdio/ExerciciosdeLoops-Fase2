produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
for i, produto in enumerate(produtos):
    venda2019 = vendas2019[i]
    venda2020 = vendas2020[i]
    if venda2020 > venda2019:
        crescimento = (venda2020 / venda2019 - 1) * 100
        print(f"O produto {produto} teve um crescimento de {crescimento:.2f}% em 2020 em comparação a 2019. Vendas 2019: {venda2019}, Vendas 2020: {venda2020}.")

