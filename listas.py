produtos = ["camiseta", "calça", "par meias", "boné", "touca"]
precos = [40.00, 80.00, 15.00, 20.00, 20.00]

print(produtos)
print(produtos[0])
print(produtos[-1])
print(len(produtos))

print(f"O produto {produtos[0]} custa R${precos[0]}.")

produtos.remove(produtos[-1])
precos.remove(precos[-1])

total = sum(precos)
print(f"O total deu R${total}")

if total < 100:
    exit()
else:
    desconto = 0.95
    total = total * desconto
    print(f"O total agora com desconto é de R${total}.")
