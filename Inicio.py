import time
from Agentes import AgenteInterfaz, AgenteChat, AgenteInterprete

if __name__ == '__main__':
    Agente1 = AgenteChat.AgenteChat("agentechat@404.city", "123456")
    Agente2 = AgenteInterfaz.AgenteInterfaz("agentehumano@404.city", "123456")
    Agente3 = AgenteInterprete.AgenteInterprete("agenteinterprete@404.city", "123456")

    Agente1.start()
    time.sleep(5)
    Agente3.start()
    time.sleep(5)
    Agente2.start()