# O usuário insere números separados por espaço, que são transformados em uma lista de inteiros.
lista = [int(x) for x in input("Digite os números da lista separados por espaço: ").split()]

# O usuário digita o número que deseja encontrar.
item = int(input("Digite o número a ser encontrado: "))

# Variável que indica se o número foi encontrado
encontrado = False

# Iteramos sobre a lista usando range(len(lista)), onde len(lista) retorna o tamanho da lista.
# Verificamos se o número em cada posição é igual ao número que estamos buscando.
for i in range(len(lista)):  # len(lista) nos dá o número de elementos na lista
    if lista[i] == item:  # Se o item for encontrado, exibimos a posição
        print(f"Número {item} encontrado na posição {i}")
        encontrado = True  # Atualizamos a variável para indicar que o número foi encontrado
        break  # Saímos do laço, pois o número já foi encontrado

# Se o número não foi encontrado, exibimos uma mensagem informando isso.
if not encontrado:
    print(f"Número {item} não encontrado.")