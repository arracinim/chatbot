from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from Interprete import Interprete

class AgenteInterprete(Agent):

    # COMPORTAMIENTO DEL AGENTE, SIEMPRE ESTÁ ESPERANDO RECIBIR UN MENSAJE
    class Comportamiento(CyclicBehaviour):
        async def run(self):
            # print("Comportamiento del Agente Interprete en Ejecucion")
            msg = await self.receive()
            if msg:
                print("Mensaje recibido con contenido: {}".format(msg.body))
                print("Se procesará el mensaje y se buscará una respuesta")
                texto = msg.body
                respuesta = Interprete.interprete(texto)

                #time.sleep()
                #................................................................
                #UNA VEZ SE PROCESA EL TEXTO, SE ENVIA LA RESPUESTA AL AGENTE CHAT
                #................................................................

                mensaje = Message()
                mensaje.to = "agentechat@404.city"
                mensaje.sender = "agenteinterprete@404.city"
                mensaje.set_metadata('performative', 'inform')
                mensaje.body = respuesta

                await self.send(mensaje)
                print("Texto procesado correctamente, enviando al Agente Chat")

    # CONSTRUCTOR DEL AGENTE
    async def setup(self):
        print("Agente Interprete en Ejecucion")
        comportamiento = self.Comportamiento()
        self.add_behaviour(comportamiento)
