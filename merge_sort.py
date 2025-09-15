import time
import random

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        
        # Iterador de la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Tamaños de las listas a probar
tamaños = [8, 16, 32, 64, 128, 256, 512, 1024]
resultados = []

for n in tamaños:
    # Generar una lista de números aleatorios
    lista_aleatoria = [random.randint(0, 1000) for _ in range(n)]
    
    # Medir el tiempo de ejecución
    inicio = time.perf_counter()
    merge_sort(lista_aleatoria)
    fin = time.perf_counter()
    
    tiempo_transcurrido = fin - inicio
    resultados.append((n, tiempo_transcurrido))

# Imprimir la tabla de resultados
print(f"{'Tamaño de la lista':<20} | {'Tiempo de ejecución (s)':<25} | {'Observaciones'}")
print("-" * 70)
for tamaño, tiempo in resultados:
    print(f"{tamaño:<20} | {tiempo:<25.10f} |")

    

