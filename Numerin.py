import random

numeroMaestro = None
facil = [1,15]
normal = [1,50]
dificil = [1,100]
puntuacion  = 0
puntuacionGanada = None
ronda = 0
intentos = None
tirada = None

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
        intentosMaximos = 3
        intentos = intentosMaximos
        puntuacionGanada = 1
        numeroMaestro = random.randint(facil [0], facil [1])
        break
    elif dificultad == 2:
        dificultad = normal
        intentosMaximos = 5
        intentos = intentosMaximos
        puntuacionGanada = 3
        numeroMaestro = random.randint(normal [0], normal [1])
        break
    elif dificultad == 3:
        dificultad = dificil
        intentosMaximos = 10
        intentos = intentosMaximos
        puntuacionGanada = 6
        numeroMaestro = random.randint(dificil [0], dificil [1])
        break
    else:
        print("Ingrese una dificultad valida: ")
        continue

while True:
    print (f'Elegiste la dificultad, {dificultad}, ¿estas listo?')
    tirada = input("¿Que numero sera?: ")
    try:
        tirada = int(tirada)
    except ValueError:
        print ("Ingresa un valor valido")
        continue
    distancia = abs(numeroMaestro - tirada)
    if tirada != numeroMaestro:
        intentos = intentos -1
        if distancia >= 12:
            print ("🥶 frio ")
        elif distancia >= 10 and distancia <12:
            print ("🌡️ Tibio")
        elif distancia >= 5 and distancia <10:
            print ("🔥 Caliente")
        else:
            print ("🌋 Muy caliente")
    else:
        print ("Acertaste!! felicitaciones!")
        puntuacion = puntuacion + puntuacionGanada
        verificar = input(f'Puntuacion acumulada: {puntuacion} \n ¿Queres seguir jugando? : ')
        if verificar.lower() == "si":
            intentos = intentosMaximos
            numeroMaestro = random.randint(dificultad [0], dificultad [1])
            continue
    
    if intentos == 0:
        print (f'Perdiste! Puntuacion total: {puntuacion}')
        break
