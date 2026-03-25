import random

numeroMaestro = random.randint(1,100)
facil = [1,15]
normal = [1,50]
dificil = [1,100]
dificultad = None
puntuacion  = 0
puntuacionGanada = None
ronda = 0
intentos = None

while True:
    print ("--------- Numerin V 0.1 ---------")
    dificultad= input("Selecciona la dificultad inicial: \n 1.Facil \n 2.Normal \n 3.Dificil")
    try:
        dificultad = int(dificultad)
    except ValueError:
        print ("Ingresa un valor valido")
        continue
    if dificultad == 1:
        dificultad = facil
        intentos = 3
        puntuacionGanada = 1
    elif dificultad == 2:
        dificultad = normal
        intentos = 5
        puntuacionGanada = 3
    elif dificultad == 3:
        dificultad = dificil
        intentos = 10
        puntuacionGanada = 6
    else:
        print("Ingrese una dificultad valida: ")
        continue