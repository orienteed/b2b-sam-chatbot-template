import requests
import json

from models.ticket import Ticket
from models.article import Article


def create_ticket(ticket_type, title, description, magento_token, order_number=None):

    article = None

    if order_number is not None:
        article = Article(title, description, order_number)
    
    else:
        article = Article(title, description)
    
    ticket = Ticket(ticket_type, title, article)

    body = json.dumps(ticket.to_dict())

    headers = {'Authorization': 'Bearer ' + magento_token, 'csr-authorization': magento_token}

    print(body, headers)

    reply = requests.post('https://chatbot-test.orienteed.com/csr/api/v1/tickets/', data=body, headers=headers)

    print(reply.json())

    if not "error" in reply.json():
        ticket_number = reply.json()['number']
        return "Ticket created with number: " + str(ticket_number)

    else:
        return "Error creating ticket"