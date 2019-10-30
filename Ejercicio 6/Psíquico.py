#Andreu Pomar Cabot
#Test Vidente


import random
intentos = 1

print ("¿Tienes poderes psíquicos? ¿Puedes adivinar el número en el que está pensando el ordenador?")

mini = int (input ("Dame un número mínimo: "))
maxi = int (input ("Dame un número máximo: "))

rng = random.randint(mini, maxi)

guess = int (input ("¿Qué numero crees que es? (entre %d y %d) " % (mini,maxi)))

while guess != rng:

    if guess > rng:
        print ("¡Demasiado grande! no es %d" % (guess))

    elif guess < rng:
            print ("¡Demasiado pequeño! no es %d" % (guess))

    guess = int (input ("¿Qué numero crees que es? (entre %d y %d) " % (mini,maxi)))
    intentos = intentos+1

print ("¡Enhorabuena! El número es %d! Has necesitado %d intentos" % (rng, intentos))

input ("Pulse Enter para cerrar el programa")
