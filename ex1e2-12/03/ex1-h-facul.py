v_prod = float(input("Digite o valor do produto\n"))
v_desc = float(input("Digite a porcentagem do desconto\n"))

v_totaldesconto = (v_prod * v_desc) / 100
v_final = v_prod - v_totaldesconto

print("o valor de desconto é de: R${:.2f}".format(v_totaldesconto))
print("o valor do produto com o desconto é de: R${:.2f}".format(v_final))