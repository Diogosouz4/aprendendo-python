# O usuário insere um número.
numero = int(input("Digite um número: "))

# A função range(1, 11) gera uma sequência de números de 1 até 10, que serão multiplicados pelo número fornecido.
# Para cada número de 1 a 10, multiplicamos pelo número inserido e exibimos o resultado.
for i in range(1, 11):  # Gera os números de 1 a 10
    print(f"{numero} x {i} = {numero * i}")  # Imprime a multiplicação do número inserido pelo valor de i
