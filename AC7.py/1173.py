i = int(input(""))
lista = []
lista.append(i)
for number in range(1, 10):
    lista.append(lista[number - 1] * 2)

for x in range(0, 10):
    print(f"N[{x}] = {lista[x]}")