from datetime import datetime, timedelta
import numpy as np
import pyperclip

def prox_dias_uteis(data, dias_uteis=3):
    dias_uteis_encontrados = []
    dia_corrente = data

    while len(dias_uteis_encontrados) < dias_uteis:
        dia_corrente += timedelta(days=1)
        if np.is_busday(dia_corrente.strftime('%Y-%m-%d')):
            dias_uteis_encontrados.append(dia_corrente)

    return dias_uteis_encontrados

# Data atual
data_atual = datetime.now()
dias_uteis = prox_dias_uteis(data_atual)

# Formatar as datas com a frase desejada
datas_texto = "dias: " + ", ".join([dia.strftime("%d/%m/%Y") for dia in dias_uteis]) + " no período matutino ou vespertino"

# Copiar a frase para a área de transferência
pyperclip.copy(datas_texto)

# Exibir mensagem de sucesso
print("\nAs datas foram copiadas para a área de transferência!")
