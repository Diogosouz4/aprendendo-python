numero = int(input("Digite um número: "))
eh_primo = True
if numero < 2:
    eh_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
if eh_primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")