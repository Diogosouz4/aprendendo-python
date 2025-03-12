peso = float(input("Digite seu peso:\n"))
altura = float(input("Digite sua altura:\n"))
imc = peso / (altura * altura)

print("Seu IMC é de {:.2f}".format(imc))
if imc >= 18.5 and imc <= 24.9:
    print("Seu IMC esta bom")
else:
    print("Seu IMC esta ruim")