from fuzzywuzzy import process

def interprete(mensaje):
    #Mensaje al agente
    Texto = mensaje
    #Lista con las posibles opciones
    Opciones = baseConocimiento()
    #Extrae la mejor respuesta para el mensaje dejado por el agente
    ordenar = process.extractBests(Texto,Opciones)
    #SACAMOS LA TUPLA CORRESPONDIENTE A LA MEJOR OPCION
    MejorOpcion = ordenar[0]
    #DE LA TUPLA SACAMOS LA OPCION MEJOR PARECIDA Y LOS GRADOS DE PERTENENCIA
    BestWord = MejorOpcion[0]
    Deegres = MejorOpcion[1]
    #ENVIAMOS LOS PARAMETROS A LA FUNCION PARA OBTENER UNA RESPUESTA A ESA OPCION
    respuesta = pickAchoice(BestWord,Deegres)
    return respuesta

def baseConocimiento():
    #ESTA BASE DE CONOCIMIENTOS PUEDE SER AMPLIADA CON BIG DATA
    Conocimientos = ["Hola", "Hola como estas?", "Buenos dias", "Buenas tardes", "Buenas noches", "",
                     ]
    return Conocimientos

def pickAchoice(palabra, grados):
    #SI LOS GRADOS DE PERTENENCIA ES MENOR A 70, QUIERE DECIR QUE NO HAY MUCHA CORRESPONDENCIA ENTRE LAS OPCIONES Y LA RESPUESTA
    if grados < 70:
        return "Vuelva a hacer su pregunta"
    else:
        if(True):
            return "Hola mundo"