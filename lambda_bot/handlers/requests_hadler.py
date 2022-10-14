from zammad_requests.create_ticket import create_ticket
from zammad_requests.check_ticket_state import check_ticket_states
from constants.constants import SESSION_ATTRIBUTES, CREATE_TICKET_INTENT_SLOTS, TICKET_TYPE_ZAMMAD

MAGENTO_TOKEN = SESSION_ATTRIBUTES['MAGENTO_TOKEN']

TICKET_TYPE = CREATE_TICKET_INTENT_SLOTS['TICKET_TYPE']
ORDER_NUMBER = CREATE_TICKET_INTENT_SLOTS['ORDER_NUMBER']
TITLE = CREATE_TICKET_INTENT_SLOTS['TITLE']
DESCRIPTION = CREATE_TICKET_INTENT_SLOTS['DESCRIPTION']

def request_create_ticket_handler(session_attributes, slots):
    magento_token = session_attributes.get(MAGENTO_TOKEN)[1:]

    ticket_type = TICKET_TYPE_ZAMMAD[slots.get(TICKET_TYPE)['value']['originalValue']]

    order_number = slots.get(ORDER_NUMBER)
    
    if order_number is not None:
        order_number = order_number['value']['originalValue']

    title = slots.get(TITLE)['value']['originalValue']

    description = slots.get(DESCRIPTION)['value']['originalValue']

    message = create_ticket(ticket_type, title, description, magento_token, order_number)

    return message


def check_ticket_states_handler(session_attributes, input):
    magento_token = session_attributes.get(MAGENTO_TOKEN)[1:]

    ticket_number = input

    state = check_ticket_states(ticket_number, magento_token)

    return state