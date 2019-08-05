from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

#VARIABLE GLOBAL
pregunta = "cuando me puedo cambiar de pensum"

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
                print("Respuesta: "+texto)

    class enviarMensaje(OneShotBehaviour):
        async def run(self):
            message = Message()
            message.sender = "agentehumano@404.city"
            message.to = "agenteinterprete@404.city"
            message.body = "Pregunta: " + pregunta
            message.set_metadata("performative", "inform")
            await self.send(message)
            print("Comportamiento terminado")

    async def setup(self):
        print("Agente Interfaz en Ejecucion")
        comportamiento = self.recibirMensaje()
        comportamiento2 = self.enviarMensaje()
        self.add_behaviour(comportamiento2)
        self.add_behaviour(comportamiento)