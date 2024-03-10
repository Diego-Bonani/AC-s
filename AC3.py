#Exercício 1

def checa_forma_triangulo(a, b, c):
    condicao_1 = a < b + c
    condicao_2 = b < a + c
    condicao_3 = c < a + b
    return condicao_1 and condicao_2 and condicao_3

def determina_tipo_triangulo(a, b, c):
    if(checa_forma_triangulo(a, b, c)):
        if(a == b and b == c):
            return "Equilátero"
        elif(a == b or b == c or a == c):
            return "Isosceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

#Execício 2

def dia_valido(dia):
    return dia >= 1 and dia <= 7

def dia_semana(dia):
    if(dia_valido(dia)):
        match dia:
            case 1:
                return "Domingo"
            case 2:
                return "Segunda-Feira"
            case 3:
                return "Terça-Feira"
            case 4:
                return "Quarta-Feira"
            case 5:
                return "Quinta-Feira"
            case 6:
                return "Sexta-Feira"
            case 7:
                return "Sábado"
    else:
        return ""


def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

#Exercício 3

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    a = int(input("Insira o primeiro valor:"))
    b = int(input("Insira o segundo valor:"))
    operacao = input("Insira a operação a se realizar:")
    match operacao:
        case "soma":
            print(soma(a, b))
        case "subtracao":
            print(subtracao(a, b))
        case "multiplicacao":
            print(multiplicacao(a, b))
        case "divisao":
            print(divisao(a, b))
        case _:
            print("Operação inválida")


def main():
    testa_dia_semana()
    testa_triangulo()
    calculadora()

main()