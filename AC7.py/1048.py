salario = float(input(""))
reajuste = 0

if salario <= 400.00:
    reajuste = 0.15
elif salario >= 400.01 and salario <= 800:
    reajuste = 0.12
elif salario >= 800.01 and salario <= 1200:
    reajuste = 0.10
elif salario >= 1200.01 and salario <= 2000:
    reajuste = 0.07
elif salario >= 2000.01:
    reajuste = 0.04

novo_salario = salario * (1 + reajuste)
aumento = salario * reajuste
percentual = int(reajuste * 100)

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {aumento:.2f}")
print(f"Em percentual: {percentual} %")