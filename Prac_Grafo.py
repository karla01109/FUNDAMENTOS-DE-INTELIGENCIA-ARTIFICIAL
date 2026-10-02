
#estados= {"A","B","C","D","E","F"}

#acciones= "A":  

def bfs(acciones, estados, nodo_inicio):
    visitados = [nodo_inicio]
    cola = [nodo_inicio]

    while cola:
        nodo_actual = cola.pop(0)

        for vecino in acciones[nodo_actual]:
            if vecino in estados and vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    return visitados


estados = {"A", "B", "C", "D", "E", "F"}

acciones = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

resultado = bfs(acciones, estados, 'A')
print(" -> ".join(resultado))  