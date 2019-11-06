#Andreu Pomar Cabot
#Ejercicio 7.7 - Contador de vocales

def TheCount():
    numa = frase.count("a") + frase.count("á")
    nume = frase.count("e") + frase.count("é")
    numi = frase.count("i") + frase.count("í")
    numo = frase.count("o") + frase.count("ó")
    numu = frase.count("u") + frase.count("ú")
    print ("La frase contiene: \n A: %d \n E: %d \n I: %d \n O: %d \n U: %d \n (Ah! Ah! Ah!)" % (numa,nume,numi,numo,numu))

frase = str(input("Introduce una frase, por favor: "))

TheCount()
input()
