#Exercício 1

def eq_seg_grau(a, b, c):
    return a + "x²" + " + " + b +"x + " + c + " = 0"

def bissexto(ano):
    mult_quatro = (ano % 4 == 0)
    mult_cem = (ano % 100 == 0)
    mult_quatrocentos = (ano % 400 == 0)
    return(mult_quatro and not mult_cem) or (mult_quatro and mult_quatrocentos)

# Exercício 2

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    return (valor_hora * num_horas) * (1 - irpf)

def main():
    print(calcula_salario(17, 8))
    print(bissexto(2000))
    print(eq_seg_grau("2", "5", "6")) # Valores passados aqui devem ser str

main()