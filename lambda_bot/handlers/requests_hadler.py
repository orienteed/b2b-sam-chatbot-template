from zammad_requests.create_ticket import create_ticket
from zammad_requests.check_ticket_state import check_ticket_states
from constants.constants import TICKET_TYPE_ZAMMAD

def create_ticket_handler(session_attributes, slots):
    magento_token = session_attributes.get('magento_token')[1:]

    ticket_type = TICKET_TYPE_ZAMMAD[slots.get("ticketType")['value']['originalValue']]

    order_number = slots.get("orderNumber")
    
    if order_number is not None:
        order_number = order_number['value']['originalValue']

    title = slots.get("title")['value']['originalValue']

    description = slots.get("description")['value']['originalValue']

    message = create_ticket(ticket_type, title, description, magento_token, order_number)

    return message


def check_ticket_states_handler(session_attributes, input):
    magento_token = session_attributes.get('magento_token')[1:]

    ticket_number = input

    state = check_ticket_states(ticket_number, magento_token)

    return state