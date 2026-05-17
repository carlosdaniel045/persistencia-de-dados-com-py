# ler.txt.py

# 1) Abrindo o arquivo com open
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

# 2) Lendo todo o conteúdo
conteudo = arquivo.read()
print("Conteúdo completo do arquivo:\n")
print(conteudo)

# 3) Imprimindo apenas a primeira linha
primeira_linha = conteudo.splitlines()[0]
print("\nPrimeira linha do arquivo:\n")
print(primeira_linha)

# 4) Imprimindo os 3 primeiros caracteres
print("\nTrês primeiros caracteres do arquivo:")
print(conteudo[:3])

# Fechando o arquivo
arquivo.close()

# 5) Usando with para abrir e ler o arquivo
print("\nLeitura utilizando 'with':\n")
with open("loremipsum.txt", "r", encoding="utf-8") as arquivo_with:
    conteudo_with = arquivo_with.read()
    print(conteudo_with)
