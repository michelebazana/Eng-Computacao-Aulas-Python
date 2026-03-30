# Checkpoint 1

# cp1 = float(input("Checkpoint 1 = "))
# cp2 = float(input("Checkpoint 2 = "))
# cp3 = float(input("Checkpoint 3 = "))
# sp1 = float(input("Sprint 1 = "))
# sp2 = float(input("Sprint 2 = "))
# gs = float(input("Global Solution = "))
# print("-" * 45)
#
# if cp1 <= cp2 and cp1 <= cp3:
#     menor = cp1
# elif cp2 <= cp1 and cp2 <= cp3:
#     menor = cp2
# else:
#     menor = cp3
#
# media = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4 + gs * 0.6
# media_peso = media * 0.4
#
# print(f"Média do 1º semestre = {media:.1f}")
# print("-" * 45)
# print(f"Média do 1º semestre com peso = {media_peso:.1f}")

# exercício 7

quant_kWh = int(input("kWh consumida = "))
tipo_inst = input("Tipo de instalação (R/I/C) = ")

if tipo_inst == "R":
    if quant_kWh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo_inst == "C":
    if quant_kWh <= 1000:
        preco = 0.5
    else:
        preco = 0.60
elif tipo_inst == "I":
    if quant_kWh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Tipo de instalação é desconhecido.")

valor_pagar = preco * quant_kWh
print(f"Preço a pagar R$ {valor_pagar:.2f}")



