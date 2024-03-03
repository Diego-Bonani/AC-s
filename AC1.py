"""
 Programação Estruturada 2024.1
 02/03/2024
 AC1

"""
import math


# Exercício 1

valor_a = int(input("Informe o parâmetro a da equação: "));
valor_b = int(input("Informe o parâmetro b da equação: "));
valor_c = int(input("Informe o parâmetro c da equação: "));

delta = (valor_b ** 2) - (4 * valor_a * valor_c);
raiz_1 = (-valor_b + math.sqrt(delta) ) / 2 * valor_a;
raiz_2 = (-valor_b - math.sqrt(delta) ) / 2 * valor_a;

print("A primeira raiz da equação é", raiz_1);
print("A segunda raiz da equação é", raiz_2);

# Exercício 2

ano = int(input("Informe o ano:"));
mult_quatro = (ano % 4 == 0)
mult_cem = (ano % 100 == 0)
mult_quatrocentos = (ano % 400 == 0)
print((mult_quatro and not mult_cem) or (mult_quatro and mult_quatrocentos))
