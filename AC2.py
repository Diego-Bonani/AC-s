#Exercício 1

def eq_seg_grau(a, b, c):
    return;

def bissexto(ano):
    mult_quatro = (ano % 4 == 0);
    mult_cem = (ano % 100 == 0);
    mult_quatrocentos = (ano % 400 == 0);
    return(mult_quatro and not mult_cem) or (mult_quatro and mult_quatrocentos);

print(bissexto(2000));
print(eq_seg_grau())
