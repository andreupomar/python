#Andreu Pomar Cabot
#7.14 - Diccionarios

def Verbose (entrada):
    fecha = entrada.split("/")
    salida = fecha[0]+" de "+meses[fecha[1]]+" de "+fecha[2]
    return salida


meses = {"01" : "Enero",
         "02" : "Febrero",
         "03" : "Marzo",
         "04" : "Abril",
         "05" : "Mayo",
         "06" : "Junio",
         "07" : "Julio",
         "08" : "Agosto",
         "09" : "Septiembre",
         "10" : "Octubre",
         "11" : "Noviembre",
         "12" : "Diciembre"}

entrada = str(input("Introduzca una fecha en el formato dd/mm/aaaa:\n"))
print (Verbose(entrada))

