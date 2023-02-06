import requests
import json

from models.ticket import Ticket
from models.article import Article
from constants.constants import ZAMMAD_HEADERS
from constants.messages import get_create_ticket_messages

import os
from dotenv import load_dotenv

load_dotenv()

B2BSTORE_URL = os.getenv("B2BSTORE_URL")


def create_ticket(ticket_type, title, description, magento_token, order_number=None):

    article = None

    if order_number is not None:
        article = Article(title, description, order_number)
    
    else:
        article = Article(title, description)
    
    ticket = Ticket(ticket_type, title, article)

    body = json.dumps(ticket.to_dict())

    headers = {ZAMMAD_HEADERS['AUTHORIZATION']: 'Bearer ' + magento_token, ZAMMAD_HEADERS['CSR_AUTHORIZATION']: magento_token, ZAMMAD_HEADERS['CONTENT_TYPE']: 'application/json'}

    reply = requests.post(f'{B2BSTORE_URL}/csr/api/v1/tickets/', data=body, headers=headers)

    if not "error" in reply.json():
        ticket_number = reply.json()['number']
        return get_create_ticket_messages(ticket_number).get('TICKET_CREATED')

    else:
        return get_create_ticket_messages().get('TICKET_NOT_CREATED')
