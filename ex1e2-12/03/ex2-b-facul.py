palavra_correta = "sair"

while True:
    senha = input("Escreva a palavra chave:\n")    
    if senha == palavra_correta:
        print("Palavra chave correta!")
        break
    else:
        print("Tente novamente.")