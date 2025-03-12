import random

while True:
    numero = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
    print(f"Número sorteado: {numero}")
    
    if numero == 7:
        print("Número 7 sorteado, saindo do loop")
        break