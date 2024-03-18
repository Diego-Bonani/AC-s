"""
Programação Estruturada
2024.1
18/03/2024

Estruturas de Repetição
AC5
"""

import random

def main():
    vida_aventureiro = 100
    vida_monstro = random.randint(60, 80)
    ata_aventureiro = random.randint(10, 20)
    def_aventureiro = random.randint(1, 5)
    ata_monstro = random.randint(20, 30)
    rodada = 1
    print("Aventureiro: vida", vida_aventureiro, "- att", ata_aventureiro, "- def", def_aventureiro)
    print("Monstro: vida", vida_monstro, "- att", ata_monstro)
    print("Rodada", rodada)


    while(vida_aventureiro and vida_monstro):
        rodada += 1
        dano_monstro = random.randint(1, ata_monstro) - def_aventureiro
        if dano_monstro > 0:
            vida_aventureiro -= dano_monstro
        vida_monstro -= random.randint(1, ata_aventureiro)
        if(vida_aventureiro <= 0):
            vida_aventureiro = 0
            print("O aventureiro morreu")
        elif(vida_monstro <= 0):
            vida_monstro = 0
            print("O monstro morreu")
        else:
            print("Aventureiro: vida", vida_aventureiro, "- att", ata_aventureiro, "- def", def_aventureiro)
            print("Monstro: vida", vida_monstro, "- att", ata_monstro)
            print("Rodada", rodada)
    return

main()