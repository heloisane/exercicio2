# Variáveis
senha_correta = "python"
tentativas = 0
acertou = False

# Laço com duas condições no mesmo laço
while not acertou and tentativas < 3:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1

    if senha_digitada == senha_correta:
        acertou = True
    else:
        print("Senha errada.")

# Verificação final do status de acesso
if acertou:
    print("Acesso liberado!")
else:
    print("Acesso bloqueado.")
