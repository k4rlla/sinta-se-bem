'''
Entregador de mensagens obtidas no ChatGPT
Script roda como um servico
'''

import sys
import requests

from django.utils import timezone
from mensagens.models import Mensagem

PROMPT = """
"""

def obtem_mensagens():
    '''
    Obtem uma lista de mensagens do ChatGPT
    '''
    mensagens = []
    # processa as mensagens aqui
    pass
    return mensagens

def main():
    mensagens = obtem_mensagens()
    for msg in mensagens:
        Mensagem.objects.create(
            data_hora=timezone.now(),
            texto = msg.texto
        )

if __name__ == '__main__':
    main()
    sys.exit(0)