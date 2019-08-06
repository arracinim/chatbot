from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

#CLASS DE AGENTE INTERFAZ
class AgenteInterfaz(Agent):
    class Mensaje(CyclicBehaviour):
        async def run(self):
            #CADA VEZ QUE SE EJECUTA EL COMPORTAMIENTO LA PREGUNTA DEBE SER NULA, PARA QUE SE CUMPLA LA CONDICION
            pregunta = ""
            #COMPORTAMIENTO SIEMPRE ESTÁ A LA ESPERA DE RECIBIR UN MENSAJE
            msg = await self.receive(timeout=2)

            #SI RECIBE EL MENSAJE
            if msg:
                #SE RECUPERA EL CUERPO DEL MENSAJE Y SE PROCEDE A ENVIAR EL MENSAJE
                #AL AGENTE INTERPRETE PARA SU PROCESAMIENTO
                texto = msg.body
                print("Respuesta: " + texto)
            elif pregunta:
                pass
            else:
                #SE SOLICITA UNA PREGUNTA
                print("Ingrese una pregunta")
                pregunta = str(input())

                # SE ELABORA LA ESTRUCTURA DEL MENSAJE ACL
                mensaje = Message()
                mensaje.sender = "agentehumano@404.city"
                mensaje.to = "agenteinterprete@404.city"
                mensaje.body = pregunta
                mensaje.set_metadata("performative", "inform")

                #SE ENVIA EL MENSAJE
                await self.send(mensaje)

    async def setup(self):
        print("Agente Interfaz en Ejecucion"+"\n")
        print("YUCA CHATBOT IS RUNNING RIGHT NOW"+"\n")
        comportamiento = self.Mensaje()
        self.add_behaviour(comportamiento)
