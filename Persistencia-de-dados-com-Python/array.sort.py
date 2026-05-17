# array.sort.py

import random

# ==============================
# ARRAY DE INTEIROS
# ==============================

# Cria um array com 15 números inteiros aleatórios (0 a 100)
array_inteiros = random.sample(range(0, 101), 15)

print("Array original (inteiros):")
print(array_inteiros)

# Ordenação crescente
array_inteiros.sort()
print("\nArray ordenado em ordem crescente:")
print(array_inteiros)

# Ordenação decrescente
array_inteiros.sort(key=None, reverse=True)
print("\nArray ordenado em ordem decrescente:")
print(array_inteiros)

# ==============================
# ARRAY DE STRINGS
# ==============================

array_strings = [
    "nome",
    "dataNascimento",
    "cpf",
    "rg",
    "email",
    "telefone",
    "endereco"
]

print("\nArray original (strings):")
print(array_strings)

# Ordenação crescente (ordem alfabética)
array_strings.sort()
print("\nArray de strings ordenado em ordem crescente:")
print(array_strings)

# Ordenação decrescente
array_strings.sort(key=None, reverse=True)
print("\nArray de strings ordenado em ordem decrescente:")
print(array_strings)
