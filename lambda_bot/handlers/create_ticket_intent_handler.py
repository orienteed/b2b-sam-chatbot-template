from constants.constants import CREATE_TICKET_INTENT_SLOTS, CREATE_TICKET_OPTIONS, SLOTS_STRUCTURE
from constants.constants import SESSION_ATTRIBUTES

from .requests_hadler import request_create_ticket_handler
from .response_handler import formDelegateResponse, formElicitSlotResponse, formTerminalResponse

TICKET_TYPE = CREATE_TICKET_INTENT_SLOTS['TICKET_TYPE']
ORDER_NUMBER = CREATE_TICKET_INTENT_SLOTS['ORDER_NUMBER']
TITLE = CREATE_TICKET_INTENT_SLOTS['TITLE']
DESCRIPTION = CREATE_TICKET_INTENT_SLOTS['DESCRIPTION']

TITLE_ORDER_TICKET = CREATE_TICKET_OPTIONS['TITLE_ORDER_TICKET']

TITLE_ELICIT = SESSION_ATTRIBUTES['TITLE_ELICIT']
DESCRIPTION_ELICIT = SESSION_ATTRIBUTES['DESCRIPTION_ELICIT']

def create_ticket_handler(input, slots, session_attributes, current_intent, slot_to_elicit, title_elicit, description_elicit):
    if slots.get(TICKET_TYPE)['value']['originalValue'] == TITLE_ORDER_TICKET and slots.get(ORDER_NUMBER) is None:
        return formElicitSlotResponse(session_attributes, ORDER_NUMBER, slots, current_intent)
    else:
        if slots.get(TITLE) is None and title_elicit is None:
            session_attributes[TITLE_ELICIT] = True
            return formElicitSlotResponse(session_attributes, TITLE, slots, current_intent)

        if title_elicit and not description_elicit:
            session_attributes[DESCRIPTION_ELICIT] = True

            slots[TITLE] = {
                'shape': 'Scalar', 
                'value': {
                    'resolvedValues': [input], 
                    'interpretedValue': input, 
                    'originalValue': input
                }
            }
        
            return formElicitSlotResponse(session_attributes, DESCRIPTION, slots, current_intent)

        if title_elicit and description_elicit:

            slots[DESCRIPTION] = {
                'shape': 'Scalar',
                'value': {
                    'resolvedValues': [input], 
                    'interpretedValue': input, 
                    'originalValue': input
                }
            }

            message = request_create_ticket_handler(session_attributes, slots)
            return formTerminalResponse(session_attributes, slots, current_intent, message)

        else:
            if slot_to_elicit is None:
                request_create_ticket_handler(session_attributes, slots)
            return formDelegateResponse(session_attributes, slots, current_intent)