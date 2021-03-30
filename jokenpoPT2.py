#FEITO POR MATEUS
#PROJETADO NO DIA 2/06
import random
import time

print('-'*50)
perg = int(input("DIGITE (1) PARA VER DUAS MAQUINAS JOGANDO E (2) PARA VC JOGAR CONTRA A MAQUINA: "))
print('-'*50)
if perg == 1:
    lista = ['papel', 'tesoura', 'pedra']
    karen = random.choice(lista)
    jarvis = random.choice(lista)
    print("\33[34mJO")
    time.sleep(0.8)
    print("\33[32mKEN")
    time.sleep(0.8)
    print("\33[33mPO!!!\33[m")
    time.sleep(1)
    if jarvis == "papel" and karen == "tesoura":
        print(jarvis, "(JARVIS)", "\33[33mVS\33[m", karen, "(KAREN)")
        print("TESOURA WINS")
    elif jarvis == "pedra" and karen == "papel":
        print(jarvis, "(JARVIS)", "\33[33mVS\33[m", karen, "(KAREN)")
        print("PAPEL WINS")
    elif jarvis == "tesoura" and karen == "pedra":
        print(jarvis, "(JARVIS)", "\33[33mVS\33[m", karen, "(KAREN)")
        print("PEDRA WINS")
    elif jarvis == "pedra" and karen == "tesoura":
        print(jarvis, "(JARVIS)", "\33[33mVS\33[m", karen, "(KAREN)")
        print("PEDRA WINS")
    elif jarvis == "papel" and karen == "pedra":
        print(jarvis, "(JARVIS)", "\33[33mVS\33[m", karen, "(KAREN)")
        print("PAPEL WINS")
    elif jarvis == "tesoura" and karen == "papel":
        print(jarvis, "(JARVIS)", "\33[33mVS\33[m", karen, "(KAREN)")
        print("TESOURA WINS")
    elif jarvis == karen:
        print(jarvis, "(JARVIS)", "\33[33mVS\33[m", karen, "(KAREN)")
        print("EMPATE")
elif perg == 2:
    print("\33[31m-=" * 10)
    print("\33[33mINSTRUÇOES\33[m -->")
    print("[1] Pedra".upper())
    print("[2] Papel".upper())
    print("[3] Tesoura".upper())
    print("\33[31m-=\33[m" * 10)
    player = int(input("Digite sua jogada --> ".upper()))
    jarvis = random.randint(1, 3)
    time.sleep(0.8)
    print("\33[31mJO")
    time.sleep(0.8)
    print("\33[33mKEN")
    time.sleep(0.8)
    print("\33[34mPO !!!\33[m")
    time.sleep(0.8)
    if jarvis == 1:  # Pedra
        print("\33[30mJARVIS JOGOU PEDRA")
        time.sleep(0.8)
        if player == jarvis:
            print("\33[33mHOUVE EMPATE...")
        elif player == 2:  # PAPEL
            print("\33[32mVC GANHOU  ☻"
                  " !!!")
            print("PAPEL GANHA DE PEDRA !!!")
        elif player == 3:  # TESOURA
            print("\33[31mVC PERDEU !!!")
            print("PEDRA GANHA DE TESOURA")
    if jarvis == 2:
        print("\33[30mJARVIS JOGOU PAPEL")
        time.sleep(0.8)
        if player == 1:
            print("\33[31mVC PERDEU !!!")
            print("PAPEL GANHA DE PEDRA")
        elif player == 2:
            print("\33[33mHOUVE EMPATE")
        elif player == 3:
            print("\33[32mVC GANHOU  ☻ !!!")
            print("TESOURA GANHA DE PAPEL")
    if jarvis == 3:
        print("\33[30mJARVIS JOGOU TESOURA")
        time.sleep(0.8)
        if player == 1:
            print("\33[32mVC GANHOU  ☻ !!!")
            print("PEDRA GANHA DE TESOURA")
        if player == 2:
            print("\33[31mVC PERDEU !!!")
            print("TESOURA GANHA DE PAPEL")
        if player == 3:
            print("\33[33mHOUVE EMPATE...")
    time.sleep(0.8)
    print("\33[34mObg por jogar !!!")





