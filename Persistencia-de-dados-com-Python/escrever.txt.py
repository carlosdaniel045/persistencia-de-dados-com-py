# escrever.txt.py

# Abrindo (ou criando) o arquivo texto.txt em modo escrita
arquivo = open("texto.txt", "w", encoding="utf-8")

# Criando a lista conforme solicitado
texto = list()

# Adicionando frases à lista
texto.append("Primeira linha escrita no arquivo.\n")
texto.append("Segunda linha adicionada através de uma lista.\n")
texto.append("Terceira linha gerada pelo script Python.\n")

# Escrevendo o conteúdo da lista no arquivo
for linha in texto:
    arquivo.write(linha)

# Fechando o arquivo
arquivo.close()
