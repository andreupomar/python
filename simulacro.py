#Pomar Cabot, Andreu
#Simulacro exámen

# ------ Funciones y procedimientos ----------------------

def añadir_pelicula(contador, cantidad, total):

    if cantidad + total >= 3000:
        print ("El videoclub no puede almacenar más copias")
        añadir_pelicula(contador, cantidad, total) #Vuelve a llamarse a si misma sin auto-incrementar para evitar que nos falten IDs

    elif cantidad <= 0:
        print ("No pueden añadirse películas con cantidades negativas de copias")
        añadir_pelicula(contador, cantidad, total)

    else:
        titulo = input ("¿Título de la película? ")
        director = input ("¿Director? ")
        genero = input ("¿Género? ")
        año = input ("¿Año? ")
        duracion = input ("¿Duración en minutos? ")
        ID = contador
        estado = "disponible"
        disponible = True
        reservadas = 0

        pelicula = [ID, titulo, director, genero, año, duracion, estado, disponible, reservadas, cantidad]

        return pelicula

      
def listar_peliculas():

    for i in range (len(catalogo)):
        print ("ID: ", catalogo[i][0], " Título: ", catalogo[i][1], " Director: ", catalogo[i][2], " Género: ", catalogo[i][3], " Año: ", catalogo[i][4],
               " Duración: ", catalogo[i][5], " Estado: ", catalogo[i][6]) #Imprime una serie de parámetros de todas las sublistas, buscando elementos específicos.


def reservar_pelicula():  

    listar_peliculas()
    idreserva = int (input ("\nIntroduzca el ID de la película que desea reservar: ")) -1 # Utilizaremos este valor para buscar la sublista correcta.

    if catalogo[idreserva][7] == False:
        print ("La película no está disponible")
        input ("Presione enter para volver al menú")

    else:
        cantidadreserva = int (input ("Introduzca la cantidad de copias que desea reservar: "))

        if cantidadreserva + catalogo[idreserva][8] > catalogo[idreserva][9]: #Comprobamos que no vayamos a reservar más copias de las disponibles
            print ("No hay tantas copias disponibles")
            input ("Presione enter para volver al menú")
            
        else:
            catalogo[idreserva][8] += cantidadreserva

            if catalogo[idreserva][8] == catalogo[idreserva][9]: #Si tras reservar copias nos quedamos sin, actualizamos los parámetros de la sublista correspondiente.
                catalogo[idreserva][7] = False
                catalogo[idreserva][6] = "No disponible"



def buscar_peliculas(): 
    print ("1 - Buscar por nombre")
    print ("2 - Buscar por director")
    print ("3 - Buscar por género")
    print ("4 - Buscar por año")
    print ("5 - Buscar por duración")

    tipobusqueda = int (input ())
    buscar = input ("Introduce la secuencia a buscar: ")
    encontrado = False #La función comienza asumiendo que la secuencia a buscar no va a ser encontrada.
    
    for i in range (len (catalogo)): #Busca en todas las entradas del catálogo las que coinciden con el parámetro especificado, y las imprime
            if buscar in catalogo[i][tipobusqueda]:
                print ("ID: ", catalogo[i][0], " Título: ", catalogo[i][1], " Director: ", catalogo[i][2], " Género: ", catalogo[i][3], " Año: ", catalogo[i][4],
                       " Duración: ", catalogo[i][5], " Estado: ", catalogo[i][6])
                encontrado = True # Si encuentra al menos una, encontrado deja de ser False y no nos mostrará el mensaje de error

    if encontrado == False:
        print ("No se ha encontrado ninguna película que coincida con la secuencia especificada")

    input ("Presione enter para volver al menú")









# ----- Programa principal. ------------------------------

opcion = 0 # Variable para controlar el bucle while del programa principal.
contador = 0 # Variable que utilizaremos para generar un ID auto-incremental
total = 0 # Cantidad total de copias en el videoclub
catalogo = [] #Lista de listas, almacena nuestro catálogo

while opcion != "4":

    print ("- - - - - - - - - - - - - - - -\n")
    print ("Programa de gestión de videoclub\n")
    print ("- - - - - - - - - - - - - - - -\n")
    print ("1 - Añadir película")
    print ("2 - Reservar película")
    print ("3 - Buscar peliculas")
    print ("4 - Salir")
    print ("- - - - - - - - - - - - - - - -\n")

    opcion = input ("Pulse un número y presione enter: ")

    if opcion == "1":
        contador += 1
        cantidad = int (input ("¿Cuántas copias? "))
        catalogo.append(añadir_pelicula(contador,cantidad,total)) #Añade a nuestra lista catálogo una sublista con todos los valores
        total += cantidad
        

    elif opcion == "2":
        reservar_pelicula()

    elif opcion == "3":
        buscar_peliculas()

    elif opcion == "4":
        print ("Saliendo...")

    else:
        print ("Opcion no válida.\n")


    
