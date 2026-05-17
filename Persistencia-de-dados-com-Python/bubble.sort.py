# bubble.sort.py

import random

def bubbleSort(array):
    # Laço externo: controla o número de passagens
    for i in range(len(array)):
        # Laço interno: compara elementos adjacentes
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                # Troca dos valores
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# Array com 15 números inteiros aleatórios
array_numeros = random.sample(range(0, 100), 15)

print("Array original:")
print(array_numeros)

# Aplicação do Bubble Sort
bubbleSort(array_numeros)

print("\nArray ordenado em ordem crescente:")
print(array_numeros)
