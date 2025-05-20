# O usuário insere uma string. A função lower() transforma a string em minúsculas para facilitar a comparação.
# Dessa forma, tanto letras maiúsculas quanto minúsculas serão contadas igualmente.
texto = input("Digite uma string: ").lower()  # Converte a string para minúsculas

# Definimos as vogais em uma string para fazer a comparação.
vogais = 'aeiou'

# Variável para contar o número de vogais
contagem = 0

# Iteramos sobre cada caractere da string digitada pelo usuário.
for letra in texto:
    if letra in vogais:  # Se a letra estiver na lista de vogais, incrementamos a contagem.
        contagem += 1

# Exibe o número total de vogais encontradas
print(f"O número de vogais é: {contagem}")

