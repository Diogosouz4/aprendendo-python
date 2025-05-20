# O usuário digita os números separados por espaço, e o split() divide a string em uma lista de strings,
# que são convertidas para inteiros usando int(x) em uma list comprehension.
lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

# Algoritmo simples de ordenação (similar ao bubble sort), que compara cada número com os outros e troca se necessário
for i in range(len(lista)):  # len(lista) retorna o tamanho da lista
    for j in range(i + 1, len(lista)):  # A segunda iteração começa sempre um passo à frente de i
        if lista[i] > lista[j]:  # Se o elemento na posição i for maior que o da posição j, trocamos os dois
            lista[i], lista[j] = lista[j], lista[i]  # Troca dos valores

# Exibe a lista ordenada
print(f"Lista ordenada: {lista}")