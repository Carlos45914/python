precoCapaLivro = 24.95
precoCapaLivroDesconto = precoCapaLivro - (precoCapaLivro * 0.40)
custoFretePrimeiroExemplar = precoCapaLivroDesconto + 3.00
custoDeFreteRestanteExemplar = precoCapaLivroDesconto + 0.75
custoTotallAtacado = custoFretePrimeiroExemplar + (custoDeFreteRestanteExemplar * 59)

print("o preco total de atacado para 60 exemplares é de:", custoTotallAtacado)