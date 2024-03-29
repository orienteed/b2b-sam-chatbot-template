import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

B2BSTORE_URL = os.getenv("B2BSTORE_URL")

def check_ticket_states(ticket_number, magento_token):

    from constants.constants import ZAMMAD_HEADERS
    from constants.messages import get_check_ticket_states_messages

    headers = {
        ZAMMAD_HEADERS["AUTHORIZATION"]: "Bearer " + magento_token,
        ZAMMAD_HEADERS["CSR_AUTHORIZATION"]: magento_token,
        ZAMMAD_HEADERS["CONTENT_TYPE"]: "application/json",
    }

    posible_states = get_ticket_states(headers)

    url = f"{B2BSTORE_URL}/csr/api/v1/tickets/search?search=number:{ticket_number}&filters=%7B%22status%22:%20%5B%5D,%20%22type%22:%20%5B%5D%7D"

    ticket_data = json.loads(requests.get(url, headers=headers).content.decode())

    if not "error" in ticket_data and len(ticket_data["tickets"]) > 0:
        ticket_id = ticket_data["tickets"][0]
        state_id = ticket_data["assets"]["Ticket"][str(ticket_id)]["state_id"]

        state = posible_states[str(state_id)]
        translated_state = get_check_ticket_states_messages()[str(state)]

        return get_check_ticket_states_messages(ticket_number, translated_state).get("TICKET_FOUND")

    else:
        return get_check_ticket_states_messages(ticket_number).get("TICKET_NOT_FOUND")


def get_ticket_states(headers):

    return json.loads(requests.get(f"{B2BSTORE_URL}/csr/api/v1/ticket_states/", headers=headers).content.decode())
