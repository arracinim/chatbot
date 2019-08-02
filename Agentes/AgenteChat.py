from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class AgenteChat(Agent):

    # COMPORTAMIENTO SIEMPRE A LA ESPERA QUE EL AGENTE INTERPRETE MANDE UNA RESPUESTA
    class Comportamiento(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            #SI RECIBE EL MENSAJE DEL AGENTE INTERPRETE
            if msg:
                respuesta = msg.body
                mensaje = Message()
                mensaje.to = "agentehumano@404.city"
                mensaje.set_metadata('performative','inform')
                mensaje.body = respuesta

                await self.send(mensaje)
                print("Respuesta enviada correctamente")

    async def setup(self):
        print("Agente Chat en ejecucion")
        comportamiento = self.Comportamiento()
        self.add_behaviour(comportamiento)
