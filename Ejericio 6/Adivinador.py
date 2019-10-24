#Andreu Pomar Cabot
#Adivinador de números

import random

print ("Voy a intentar adivinar el número en el que estás pensando.")

mini = int ( input ("Dime un mínimo: "))
maxi = int ( input ("Dime un máximo: "))
intentos = 0

if mini > maxi:
    print ("¡Eres un tramposo!")
    mini = int ( input ("Dime un mínimo: "))
    maxi = int ( input ("Dime un máximo: "))

feedback = ""

while feedback != "igual" and mini <= maxi:

    guess = random.randint (mini,maxi)
    intentos+=1
    feedback = input ("Creo que es %d. Es mayor, menor o igual?" % (guess))

    if feedback == "mayor":
        mini = guess+1

    elif feedback == "menor":
        maxi = guess-1

if feedback == "igual":
    print ("¡Solo he necesitado %d intentos!" % (intentos))

if mini > maxi:
    print ("¡Eres un sucio tramposo! Ya no quiero jugar contigo.")
