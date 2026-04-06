# print(1)
# print(2)
# print(3)
# print()
# x = 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)
# print()
#
# x = 1
# while x <= 3:
#     print(x)
#     x += 1

# Exercício 3

# from time import sleep
#
# x = 10
# while x >= 0:
#     print(x)
#     sleep(1)
#     x -= 1
#
# print("Fogo!")

# fim = int(input("Digite o nº de parada: "))
# x = 0
# while x <= fim:
#     print(x)
#     x += 2

# Exercício 5

# x = 3
# while x <= 30:
#     print(x)
#     x += 3

# num = int(input("Tabuada de: "))
# fim = int(input("Fim a tabuada: "))
# x = 1
# while x <= fim:
#     print(f"{num} x {x} = {num * x}")
#     x += 1

soma = 0
x = 0
while x < 3:
    x += 1
    check = float(input(f"Nota do Checkpoint {x}: "))
    soma += check
print(f"Média = {soma/x}")
