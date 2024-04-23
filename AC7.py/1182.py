num_col = int(input(""))
op = input("")
matriz = []
soma = 0

for i in range(12):
    array = []
    for j in range(12):
        array.append(float(input("")))
    matriz.append(array)

for k in range(12):
    soma += matriz[k][num_col]

if op == "S":
    print(f"{soma:.1f}")
elif op == "A":
    media = soma / 12
    print(f"{media:.1f}")