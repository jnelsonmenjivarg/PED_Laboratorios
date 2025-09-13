import time
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        intercambio =  False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio=True
                if not intercambio:
                    break
#Generar listsa
def generar_lista(n, tipo="aleatoria"):
    if tipo == "ordenada":
        return list(range(n))
    elif tipo == "inversa":
        return list(range(n,0,-1))
    else:
        return [random.randint(1, n*10) for _ in range(n)]
                
#Experimentos
n=5000
casos = {
    "Ordenaa": generar_lista(n, "ordenada"),
    "Inversa": generar_lista(n, "inversa"),
    "Aleatoria": generar_lista(n, "aleatoria"),
}

for caso, lista in casos.items():
    copia = lista[:]
    inicio = time.time()
    bubble_sort(copia)
    fin = time.time()
    print(f"Caso {caso}: {fin - inicio: .6f} Segundos")
