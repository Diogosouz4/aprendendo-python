lista_de_strings = "Diogo", "Claudio", "Gabriel", "Jeferson", "Durvalina"

# Inicializa a variável para armazenar a string de maior comprimento
maior_string = ""

# Percorre a lista de strings
for string in lista_de_strings:
    if len(string) > len(maior_string):
        maior_string = string  # Atualiza a maior string

print(f"A string de maior comprimento é: {maior_string}")