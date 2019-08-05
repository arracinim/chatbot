from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

#VARIABLE GLOBAL
pregunta = ""

#CLAS DE AGENTE INTERFAZ
class AgenteInterfaz(Agent):
    'Este comportamiento permite establecer un mensaje'
    class recibirMensaje (CyclicBehaviour):
        async def run(self):
            #COMPORTAMIENTO SIEMPRE ESTÁ A LA ESPERA DE RECIBIR UN MENSAJE
            msg = await self.receive()
            #SI RECIBE EL MENSAJE
            if msg:
                #SE RECUPERA EL CUERPO DEL MENSAJE Y SE PROCEDE A ENVIAR EL MENSAJE
                #AL AGENTE INTERPRETE PARA SU PROCESAMIENTO
                texto = msg.body
                print("Respuesta: " + texto)

    class enviarMensaje(CyclicBehaviour):

        async def run(self):
            global pregunta
            if pregunta:
                ""
            else:
                print("Ingrese una pregunta")
                pregunta = str(input())
                message = Message()
                message.sender = "agentehumano@404.city"
                message.to = "agenteinterprete@404.city"
                message.body = pregunta
                message.set_metadata("performative", "inform")
                await self.send(message)
                pregunta = ""

        async def on_end(self):
            self.exit_code()

    async def setup(self):
        print("Agente Interfaz en Ejecucion")
        comportamiento = self.recibirMensaje()
        comportamiento2 = self.enviarMensaje()
        self.add_behaviour(comportamiento)
        self.add_behaviour(comportamiento2)
