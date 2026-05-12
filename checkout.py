produtos = ["moletom", "calça", "sueter", "par de luvas", "touca"]
precos = [100.00, 80.00, 90.00, 15.00, 20.00]
quantidades = [5, 2, 3, 2, 3]
subtotais = []
for indice, produto in enumerate(produtos):
    preco = precos[indice]
    quantidade = quantidades[indice]
    subtotal = quantidade * preco
    subtotais.append(subtotal)

    mensagem = f"""
    --------------------------------
    Produto: {produto}
    Quantidade: {quantidade}
    Valor unitário: {preco}
    Subtotal: {subtotal}
    --------------------------------
    """

    print(mensagem)

print(f"O total da compra deu: R${sum(subtotais)}")