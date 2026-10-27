numero_secreto = 7
tentativas = 1
palpite = int(input("Adivinhe o número (de 1 a 10): "))
while palpite != numero_secreto:
    if palpite < numero_secreto:
        print("É maior!")
    else:
        print("É menor!")
        
    tentativas += 1
    palpite = int(input("Tente de novo: "))
print(f"Acertou em {tentativas} tentativas!")