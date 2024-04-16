valor1 = int(input(""))
valor2 = int(input(""))
valor3 = int(input(""))
valor4 = int(input(""))
valor5 = int(input(""))

contador = 0

if valor1 % 2 == 0:
    contador += 1
if valor2 % 2 == 0:
    contador += 1
if valor3 % 2 == 0:
    contador += 1
if valor4 % 2 == 0:
    contador += 1
if valor5 % 2 == 0:
    contador += 1

print(f"{contador} valores pares")