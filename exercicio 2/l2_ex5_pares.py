def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado
n = int(input("Calcular o fatorial de: "))
fatorial = calcular_fatorial(n)
print("Fatorial de", n, "=", fatorial)