#Andreu Pomar Cabot
#Práctica 7.9 - Mirar si riman

def rimar():
    if pal1[-3] == pal2[-3]:
        print ("%s y %s riman" % (pal1,pal2))
    elif pal1[-2] == pal2[-2]:
        print ("%s y %s riman un poco" % (pal1,pal2))
    else:
        print ("%s y %s no riman" % (pal1,pal2))

pal1 = str(input("Introduce la primera palabra: "))
pal2 = str(input("Introduce la segunda palabra: "))

rimar()
input()

