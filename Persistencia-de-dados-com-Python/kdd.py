# kdd.py

import time
import string


class Glossario:
    def __init__(self):
        self.palavras = list()

    def ler_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                # remove pontuação e quebra em palavras
                linha = linha.translate(str.maketrans("", "", string.punctuation))
                palavras_linha = linha.split()
                for palavra in palavras_linha:
                    self.palavras.append(palavra.lower())

    def bubble_sort(self, lista):
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    def selection_sort(self, lista):
        for i in range(len(lista)):
            menor = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j
            lista[i], lista[menor] = lista[menor], lista[i]

    def ordenar_e_medir(self, metodo):
        copia = self.palavras.copy()

        inicio = time.time()

        if metodo == "bubble":
            self.bubble_sort(copia)
        elif metodo == "selection":
            self.selection_sort(copia)
        elif metodo == "sort":
            copia.sort()

        fim = time.time()

        print(f"\nMétodo: {metodo}")
        print(f"Tempo de execução: {fim - inicio:.6f} segundos")
        print(f"Total de palavras: {len(copia)}")

        return copia

    def salvar_em_txt(self, palavras_ordenadas, nome_arquivo):
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for palavra in palavras_ordenadas:
                arquivo.write(palavra + "\n")


# ==============================
# EXECUÇÃO
# ==============================

glossario = Glossario()

glossario.ler_arquivo("loremipsum.txt")

resultado_bubble = glossario.ordenar_e_medir("bubble")
resultado_selection = glossario.ordenar_e_medir("selection")
resultado_sort = glossario.ordenar_e_medir("sort")

# Após escolher o melhor método (spoiler: sort)
glossario.salvar_em_txt(resultado_sort, "glossario_ordenado.txt")
