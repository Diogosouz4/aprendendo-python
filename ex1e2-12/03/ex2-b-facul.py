palavra_correta = "sair"

# Loop para pedir a senha até que o usuário acerte
while True:
    senha = input("Escreva a palavra chave:\n")    
    if senha == palavra_correta:
        print("Palavra chave correta!")
        break
    else:
        print("Tente novamente.")