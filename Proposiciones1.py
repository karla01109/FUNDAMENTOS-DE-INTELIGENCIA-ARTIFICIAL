#Pre = float ("¿Cuantas proposiciones desea?")
#valores = [True, False]
#Aregar la tabla

n = int(input("¿Cuántas proposiciones quieres?: "))

valor = ["P", "Q", "R", "S", "T", "U", "V"]
proposiciones = valor[:n]

print(" | ".join(proposiciones))
print("-" * (n * 4))

total_filas = 2 ** n

for i in range(total_filas):
    fila = []
    for j in range(n):
        if (i // (2 ** (n - 1 - j))) % 2 == 0:
            fila.append("V")
        else:
            fila.append("F")
            
    print(" | ".join(fila))