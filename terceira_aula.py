# media_final = float(input("Média final = "))
#
# if media_final >= 6:
#     print("Aprovado")
# else:
#     print("Reprovado")

# Exercício 1
# vel = int(input("Velocidade do carro em km/h = "))
# if vel > 80:
#     print("Você foi multado.")
#     multa = (vel - 80) * 5
#     print(f"O valor da multa é R${multa:.2f}.")

# Exercício 2
# num1 = float(input("Número 1 = "))
# num2 = float(input("Número 2 = "))
# num3 = float(input("Número 3 = "))
#
# maior = num1
# if num2 >= num1 and num2 >= num3:
#     maior = num2
# if num3 >= num1 and num3 >= num2:
#     maior = num3
#
# menor = num1
# if num2 <= num1 and num2 <= num3:
#     menor = num2
# if num3 <= num1 and num3 <= num2:
#     menor = num3
#
# print(f"Maior = {maior}")
# print(f"Menor = {menor}")

# Exercício 3
# sal = float(input("Salário = R$"))
# if sal > 1250:
#     aumento = sal * 0.1
# else:
#     aumento = sal * 0.15
# print(f"Aumento de R${aumento:.2f}")

# Exercício 4
dist = int(input("Distância em km = "))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print(f"O valor da passagem é R${preco:.2f}.")



