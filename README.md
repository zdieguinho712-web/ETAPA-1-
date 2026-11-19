# ETAPA-1-

foi editado a MAXIMO_SIMULTANEO = 2 
estava como 3 por isso o programa estava dando errado <img width="1152" height="864" alt="Captura de Tela (1)" src="https://github.com/user-attachments/assets/0c59a284-505a-454f-8011-e1cfee635bbd" />

EVIDENCIA 3 def processar_pedido(numero):
    with semafaro:
        time.sleep(0.1)
        with trava:
            if principal["online"] and principal["estoque"] > 0:
                principal["estoque"] -= 1
                pedidos_confirmados.append(numero)

                # Atualização imediata da réplica (replicação síncrona)
                if replica["online"]:
                    replica["estoque"] = principal["estoque"]<img width="1279" height="1023" alt="DD" src="https://github.com/user-attachments/assets/939e0d74-6d66-4c9f-88e4-01355b90bbed" />

                    
