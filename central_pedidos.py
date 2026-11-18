import threading
import time 

#servidores simulados
principal = {
    "online": True,
    "estoque":10

}

replica = {
    "online": True,
    "estoque": 10

}

#controle de concorrencia 
MAXIMO_SIMULTANEO = 2

semafaro = threading.Semaphore(MAXIMO_SIMULTANEO)
trava = threading.Lock()

pedidos_confirmados =[]

def sicronizar():
    """Copia o estoque atual do principal para a réplica."""
    with trava:
        if principal["online"] and replica["online"]:
            replica["estoque"] = principal["estoque"]


def consultar_estoque():
    """Consulta o principal e usa a réplica como alternativa."""
    if principal["online"]:
        return "PRINCIPAL", principal["estoque"]
    if replica["online"]:
        return "REPLICA", replica["estoque"]
    return "INDISPONIVEL", None


def processar_pedido(numero):
    with semafaro:
        time.sleep(0.1)

        with trava :
            if principal["estoque"]> 0:
                principal ["estoque"]-=1
                pedidos_confirmados.append(numero)

print("=== CENTRAL DE PEDIDOS ===")

print(
    "limite simultaneo:",
    MAXIMO_SIMULTANEO
)

print(
    "estoque inicial:",
    principal["estoque"]
)

trabalhadores = [
    threading.Thread(
        target = processar_pedido,
        args=(numero,)
    )
    for numero in [101,102, 103,]
]

for trabalhador in trabalhadores:
    trabalhador.start()

for trabalhador in trabalhadores:
    trabalhador.join()

print(
    "pedidos confirmados:",
    sorted(pedidos_confirmados)
)

print(
    "estoque principal:",
    principal["estoque"]
)

print(
    "replica antes:",
    replica["estoque"]
)



sicronizar()

print(
    "replica depois:",
    replica ["estoque"]

)

#simulaçao de falha 
principal["online"] = False

def consultar_estoque():
    ...

nome, estoque = consultar_estoque()

print(
    "consulta após falha:",
    nome,
    estoque
)