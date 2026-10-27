n = int(input("Mostrar os pares de 1 até: "))
contador = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        contador = contador + 1
print("São", contador, "números pares.")