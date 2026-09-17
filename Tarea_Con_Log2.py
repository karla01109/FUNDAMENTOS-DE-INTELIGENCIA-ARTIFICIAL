print("SELECCIONA EL CONECTOR LÓGICO:")
print("1. Negación (no P)")
print("2. Conjunción (P y Q y R...)")
print("3. Disyunción (P o Q o R...)")
print("4. Condicional (P -> Q)")
print("5. Bicondicional (P <-> Q)")

opcion = input("\nIngresa la opción (1-5): ")
#cantidad de proposiciones según la opción
if opcion == "1":
    print("Nota: La negación se evaluará para 1 proposición (P).")
elif opcion in ["4", "5"]:
    print("Nota: Condicional y Bicondicional evalúan 2 proposiciones (P y Q).")
else:
    n = int(input("¿Cuántas proposiciones quieres?: "))
letras = ["P", "Q", "R", "S", "T", "U", "V"]
proposiciones = letras[:n]
 
nombres_conectores = {
    "1": "no " + proposiciones[0],
    "2": " AND ".join(proposiciones),
    "3": " OR ".join(proposiciones),
    "4": "P -> Q",
    "5": "P <-> Q"
}

encabezado = proposiciones + [nombres_conectores[opcion]]

print("\n" + " | ".join(encabezado))
print("-" * (len(" | ".join(encabezado)) + 2))

#cuántas filas tiene la tabla
total_filas = 2 ** n

for i in range(total_filas):
    fila = []
    valores_bool = [] 
    
    for j in range(n):
        if (i // (2 ** (n - 1 - j))) % 2 == 0:
            fila.append("V")
            valores_bool.append(True)
        else:
            fila.append("F")
            valores_bool.append(False)

    resultado = False

    # 1. NEGACIÓN
    if opcion == "1":
        resultado = not valores_bool[0]

    # 2. CONJUNCIÓN (Todas deben ser True)
    elif opcion == "2":
        resultado = all(valores_bool)

    # 3. DISYUNCIÓN INCLUSIVA (Al menos una debe ser True)
    elif opcion == "3":
        resultado = any(valores_bool)

    # 4. CONDICIONAL (Falso solo si P es True y Q es False)
    elif opcion == "4":
        resultado = not (valores_bool[0] is True and valores_bool[1] is False)

    # 5. BICONDICIONAL (Verdadero si P y Q son iguales)
    elif opcion == "5":
        resultado = valores_bool[0] == valores_bool[1]

    # Agregar el resultado convertido a 'V' o 'F'
    fila.append("V" if resultado else "F")

    print(" | ".join(fila))