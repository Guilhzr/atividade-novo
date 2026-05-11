
frutas = ["manga", "banana", "abacaxi", "laranja", "uva"]

fruta_favorita = input("Qual sua fruta favorita?: ")

if fruta_favorita not in frutas:
    
    print("Sua fruta favorita não está na lista!")
    print("Adicionando...")
    frutas.append(fruta_favorita)

for posicao, fruta in enumerate(frutas):
    
    if fruta == fruta_favorita:
        
        posicao_fruta_favorita = posicao
        
        break 

print(f"Minha fruta favorita está na posição índice {posicao_fruta_favorita}")