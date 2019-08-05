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
    Conocimientos = ["Hola", "Hola como estas?", "Buenos dias", "Buenas tardes", "Buenas noches", "Buenas",
                     "materias que pasan a ser obligatorias?", "materias que pasan a optativas?","Cuando puedo firmar o cambiarme de pensum",
                     "Que debo hacer para cambiarme de pensum?","Cuantos creditos debo ver para graduarme?", "Cuantos creditos debo ver ahora?",
                     "Cuantos creditos de fundamentacion debo ver ahora?","Que fisicas son obligatorias", "Que materias pasan de libre eleccion a optativas",
                     "Cual es el prerequisito de Inteligencia Artificial?", "Cual es el prerequisito de sistemas multiagente","Cual es el prerequisito de fundamentos de programacion",
                     "materias que pasan a ser libre eleccion","donde puedo firmar para cambiarme de pensum", "como se llama el monitor de cambio de pensum",
                     "Prerequisito", "Cuando queda activo el nuevo pensum", "Cuales fueron los principales cambios", "Donde puedo reservar citas",
                     "Cuantos creditos de fundamentacion optativa debo ver","Debo ver fisica 2","Debo ver ecuaciones difenciales","Prerequisito de Estructura de datos",
                     "Prerequisito de POO programacion objetos","Correo del monitor","Cual es el sentido de la vida", "Alguna vez alguien me amará" ]
    return Conocimientos


def pickAchoice(palabra, grados):
    #SI LOS GRADOS DE PERTENENCIA ES MENOR A 70, QUIERE DECIR QUE NO HAY MUCHA CORRESPONDENCIA ENTRE LAS OPCIONES Y LA RESPUESTA
    #LAS RESPUESTAS PUEDEN SER AMPLIADAS BASADAS EN PREGUNTAS FRECUENTES EXTRAIDAS DIRECTAMENTE DE UNA PAGINA
    if grados < 40:
        return "Esa pregunta se puede resolver en asesoría, M8A - 203"
    else:
        if(palabra == "Hola"):
            return "Hola, Como estás?"
        elif(palabra == "Hola como estas?"):
            return "Muy bien y tu. ¿En que puedo ayudarte?"
        elif(palabra == "Buenos dias"):
            return "Buenos dias, ¿En que puedo ayudarte?"
        elif(palabra =="Buenas tardes"):
            return "Buenas tardes. ¿En que puedo ayudarte?"
        elif(palabra == "Buenas noches"):
            return "Buenas noches ¿En que puedo ayudarte?"
        elif(palabra == "Buenas"):
            return "Hola, ¿En que puedo ayudarte?"
        elif(palabra == "materias que pasan a ser obligatorias?"):
            return "Las materias que pasan a ser obligatorias son: Calidad de Software, Algebra Lineal, \n" \
                   "Introduccion al analisis de decisiones"
        elif(palabra == "materias que pasan a optativas?"):
            return "Las materias que ahora pasan a ser optativas son: Ecuaciones diferenciales"
        elif(palabra == "Cuando puedo firmar o cambiarme de pensum"):
            return "A partir del 2019-2"
        elif(palabra == "Que debo hacer para cambiarme de pensum?"):
            return "Debes firmar un documento expresando que deseas hacer el cambio"
        elif(palabra == "Cuantos creditos debo ver para graduarme?"):
            return "160 creditos"
        elif (palabra == "Cuantos creditos de fundamentacion debo ver ahora?"):
            return "43 creditos"
        elif(palabra == "Que fisicas son obligatorias"):
            return "Fisica Mecanica"
        elif(palabra == "Que materias pasan de libre eleccion a optativas"):
            return "Vision artificial, Analisis y diseño de algoritmos y semat pasan de ser libre eleccion a optativas"
        elif(palabra == "Cual es el prerequisito de Inteligencia Artificial?"):
            return "Basde de datos 1 y estadistica"
        elif(palabra == "Los seminarios siguen siendo obligatorios?"):
            return "Si"
        elif(palabra == "Cual es el prerequisito de fundamentos de programacion"):
            return "Algebra Lineal"
        elif(palabra == "Cual es el prerequisito de sistemas multiagente"):
            return "Introduccion a la Inteligencia Artificial"
        elif(palabra == "materias pasan a libre eleccion"):
            return "Las materias que pasan a ser libre eleccion son: Electronica digital y Teoria de la gestion"
        elif(palabra == "donde puedo firmar para cambiarme de pensum"):
            return "En la oficinal M8A -205"
        elif(palabra == "como se llama el monitor de cambio de pensum"):
            return "Angel Racini. Correo: M8A-205"
        elif(palabra == "Prerequisito"):
            return "Especifique de que materia"
        elif(palabra == "Cuando queda activo el nuevo pensum"):
            return "En el 2020-1"
        elif(palabra == "Cuales fueron los principales cambios"):
            return "Tienes que ver menos creditos de fundamentacion y en general menos creditos para poder graduarte"
        elif(palabra == "Donde puedo reservar citas"):
            return "Las citas las puedes reservar en: https://actualizacion-pensum-sistemas.appointlet.com"
        elif(palabra == "Cuantos creditos de fundamentacion optativa debo ver"):
            return "16 creditos"
        elif(palabra == "Debo ver fisica 2"):
            return "No, ya no debes verla obligatoriamente"
        elif(palabra == "Debo ver ecuaciones difenciales"):
            return "No, pasa a ser optativa"
        elif(palabra == "Prerequisito de Estructura de datos"):
            return "Calculo integral y POO"
        elif (palabra == "Prerequisito de POO programacion objetos"):
            return "Ingeniería de Software"
        elif(palabra == "Correo del monitor"):
            return "arracinim@unal.edu.co"
        elif(palabra == "Cual es el sentido de la vida"):
            return "La vida no tiene sentido cuando estudias Ing de Sistemas"
        elif(palabra == "Alguna vez alguien me amará"):
            return "Eres muy feo"
        else:
            return "Reeplanté la pregunta o para mayor duda escriba al correo: arracinim@unal.edu.co"



