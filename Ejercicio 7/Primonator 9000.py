#Andreu Pomar Cabot
#7.13 - Determinadora de primos, con medidor de tiempo.


#IMPORTS
from time import time


# FUNCIONES

def PrimoFor (num):
    primo = True

    for i in range(2,num):
        if num%i==0:
            primo = False

    return primo

# -------------------------------------------- 

def PrimoWhile (num):
    contador = 2
    primo = True

    while primo == True and contador < num:
        if num%contador == 0:
            primo = False
        else:
            contador+=1

    return primo

# --------------------------------------------

selector = int(input("Pulse 1 para usar un FOR, 2 para usar un WHILE o cualquier otro valor para usar ambas: "))
num = int(input("Introduzca el número que desea calcular: "))

if selector == 1:
    start_time=time()
    if PrimoFor(num) == True:
        print ("%d es primo" % (num))
    else:
        print ("%d no es primo" % (num))
               
    elapsed_time=time()-start_time
    print ("Tiempo transcurrido: %.10f segundos" % (elapsed_time))

elif selector == 2:
    start_time=time()
    if PrimoWhile(num) == True:
        print ("%d es primo" % (num))
    else:
        print ("%d no es primo" % (num))
               
    elapsed_time=time()-start_time
    print ("Tiempo transcurrido: %.10f segundos" % (elapsed_time))

else:
    start_time=time()
    if PrimoFor(num) == True:
        print ("%d es primo" % (num))
    else:
        print ("%d no es primo" % (num))
               
    elapsed_time=time()-start_time
    print ("Tiempo transcurrido mediante FOR: %.10f segundos" % (elapsed_time))

    start_time=time()
    if PrimoWhile(num) == True:
        print ("%d es primo" % (num))
    else:
        print ("%d no es primo" % (num))
               
    elapsed_time=time()-start_time
    print ("Tiempo transcurrido mediante WHILE: %.10f segundos" % (elapsed_time))

    input()
