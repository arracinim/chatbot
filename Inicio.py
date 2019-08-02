import time
from Agentes import AgenteInterfaz, AgenteChat, AgenteInterprete
from spade.message import Message
import gui

if __name__ == '__main__':
    Agente1 = AgenteChat.AgenteChat("agentechat@404.city", "123456")
    Agente2 = AgenteInterfaz.AgenteInterfaz("agentehumano@404.city", "123456")
    Agente3 = AgenteInterprete.AgenteInterprete("agenteinterprete@404.city", "123456")

    Agente1.start()
    time.sleep(10)
    Agente3.start()
    time.sleep(10)
    Agente2.start()

    Agente1.web.start(hostname="127.0.0.1", port="10001")
    Agente2.web.start(hostname="127.0.0.1", port="10002")
    Agente2.web.start(hostname="127.0.0.1", port="10003")


    print("Para parar la ejecucion presione CRTL + c")
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            Agente1.stop()
            Agente2.stop()
            Agente3.stop()
            print("Se ha detenido el programa")
            break;