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
nombreDificultad = None
termometro = None
termometroFacil = [12,7,5,2]
termometroNormal = [30,15,7,5]
termometroDificil = [50,30,10,8]
while True:
    print ("--------- Numerin V 0.1 ---------")
    dificultad= input("Selecciona la dificultad inicial: \n 1.Facil \n 2.Normal \n 3.Dificil\n")
    try:
        dificultad = int(dificultad)
    except ValueError:
        print ("Ingresa un valor valido")
        continue
    if dificultad == 1:
        dificultad = facil
        nombreDificultad = "facil"
        intentosMaximos = 3
        intentos = intentosMaximos
        puntuacionGanada = 1
        numeroMaestro = random.randint(facil [0], facil [1])
        termometro = termometroFacil
        break
    elif dificultad == 2:
        dificultad = normal
        nombreDificultad = "normal"
        intentosMaximos = 5
        intentos = intentosMaximos
        puntuacionGanada = 3
        numeroMaestro = random.randint(normal [0], normal [1])
        termometro = termometroNormal
        break
    elif dificultad == 3:
        dificultad = dificil
        nombreDificultad = "dificil"
        intentosMaximos = 10
        intentos = intentosMaximos
        puntuacionGanada = 6
        numeroMaestro = random.randint(dificil [0], dificil [1])
        termometro = termometroDificil
        break
    else:
        print("Ingrese una dificultad valida: ")
        continue
print (f'Elegiste la dificultad {nombreDificultad}, ¿estas listo?')

while True: 
    print (numeroMaestro)
    tirada = input("¿Que numero sera?: ")
    try:
        tirada = int(tirada)
    except ValueError:
        print ("Ingresa un valor valido")
        continue
    distancia = abs(numeroMaestro - tirada)
    if tirada != numeroMaestro:
        intentos = intentos -1
        if distancia >= termometro[0]:
            print ("🥶 frio ")
        elif distancia <= termometro[0] and distancia >termometro[1]:
            print ("🌡️ Tibio")
        elif distancia <= termometro[1] and distancia >termometro[2]:
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
