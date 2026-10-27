num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
operacao = input("Operação: ")
if operacao == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == "4":
    if num2 == 0:
        print("Não dá para dividir por zero.")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)
else:
    print("Operação inválida.")