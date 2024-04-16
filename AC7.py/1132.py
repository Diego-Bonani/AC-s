x = int(input(""))
y = int(input(""))
soma = 0
for number in range(x, y + 1):
    if number % 13 != 0:
        soma += number
print(soma)