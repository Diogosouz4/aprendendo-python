# O usuário insere um número, e nós inicializamos a variável fatorial como 1.
numero = int(input("Digite um número: "))
fatorial = 1

# A função range(1, numero + 1) gera uma sequência de números de 1 até o número inserido pelo usuário.
# Multiplicamos o valor de fatorial por cada número da sequência para calcular o fatorial.
for i in range(1, numero + 1):  # range vai de 1 até o número fornecido
    fatorial *= i  # fatorial = fatorial * i, ou seja, acumulamos o resultado de cada multiplicação

# Exibe o resultado do fatorial
print(f"O fatorial de {numero} é: {fatorial}")

