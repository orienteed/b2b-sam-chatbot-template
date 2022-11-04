def request_create_ticket_handler(session_attributes, slots):

    from zammad_requests.create_ticket import create_ticket
    from constants.constants import SESSION_ATTRIBUTES, CREATE_TICKET_INTENT_SLOTS
    from constants.messages import get_ticket_type_zammad

    MAGENTO_TOKEN = SESSION_ATTRIBUTES['MAGENTO_TOKEN']

    TICKET_TYPE = CREATE_TICKET_INTENT_SLOTS['TICKET_TYPE']
    ORDER_NUMBER = CREATE_TICKET_INTENT_SLOTS['ORDER_NUMBER']
    TITLE = CREATE_TICKET_INTENT_SLOTS['TITLE']
    DESCRIPTION = CREATE_TICKET_INTENT_SLOTS['DESCRIPTION']

    magento_token = session_attributes.get(MAGENTO_TOKEN)[1:]

    ticket_type = get_ticket_type_zammad()[slots.get(TICKET_TYPE)['value']['originalValue']]

    order_number = slots.get(ORDER_NUMBER)
    
    if order_number is not None:
        order_number = order_number['value']['originalValue']

    title = slots.get(TITLE)['value']['originalValue']

    description = slots.get(DESCRIPTION)['value']['originalValue']

    message = create_ticket(ticket_type, title, description, magento_token, order_number)

    return message


def check_ticket_states_handler(session_attributes, input):

    from constants.constants import SESSION_ATTRIBUTES
    from zammad_requests.check_ticket_state import check_ticket_states

    MAGENTO_TOKEN = SESSION_ATTRIBUTES['MAGENTO_TOKEN']

    magento_token = session_attributes.get(MAGENTO_TOKEN)[1:]

    ticket_number = input

    state = check_ticket_states(ticket_number, magento_token)

    return state