from constants.constants import CREATE_TICKET_INTENT_SLOTS, get_create_ticket_options, get_slots_structure
from constants.constants import SESSION_ATTRIBUTES, INTERACTIVE_OPTIONS, get_create_ticket_messages

from templates.response_cards import TEMPLATES

from .requests_hadler import request_create_ticket_handler
from .response_handler import formDelegateResponse, formElicitSlotResponse, formTerminalResponse, formElicitSlotWithTemplateResponse

TICKET_TYPE = CREATE_TICKET_INTENT_SLOTS['TICKET_TYPE']
ORDER_NUMBER = CREATE_TICKET_INTENT_SLOTS['ORDER_NUMBER']
TITLE = CREATE_TICKET_INTENT_SLOTS['TITLE']
DESCRIPTION = CREATE_TICKET_INTENT_SLOTS['DESCRIPTION']

ELICIT_TITLE_MESSAGE = get_create_ticket_messages()['ELICIT_TITLE_MESSAGE']
ELICIT_DESCRIPTION_MESSAGE = get_create_ticket_messages()['ELICIT_DESCRIPTION_MESSAGE']

TITLE_ORDER_TICKET = get_create_ticket_options()['TITLE_ORDER_TICKET']

TITLE_ELICIT = SESSION_ATTRIBUTES['TITLE_ELICIT']
DESCRIPTION_ELICIT = SESSION_ATTRIBUTES['DESCRIPTION_ELICIT']

def create_ticket_handler(input, slots, session_attributes, current_intent, slot_to_elicit, title_elicit, description_elicit):
    if slots.get(TICKET_TYPE) is not None:
        if slots.get(TICKET_TYPE)['value']['originalValue'] == TITLE_ORDER_TICKET and slots.get(ORDER_NUMBER) is None:
            return formElicitSlotResponse(session_attributes, ORDER_NUMBER, slots, current_intent)
        else:
            if slots.get(TITLE) is None and title_elicit is None:
                session_attributes[TITLE_ELICIT] = True
                return formElicitSlotResponse(session_attributes, TITLE, slots, current_intent, ELICIT_TITLE_MESSAGE)
    
            if title_elicit and not description_elicit:
                session_attributes[DESCRIPTION_ELICIT] = True
    
                slots[TITLE] = get_slots_structure(input)
            
                return formElicitSlotResponse(session_attributes, DESCRIPTION, slots, current_intent, ELICIT_DESCRIPTION_MESSAGE)
    
            if title_elicit and description_elicit:
    
                slots[DESCRIPTION] = get_slots_structure(input)
    
                message = request_create_ticket_handler(session_attributes, slots)
                return formTerminalResponse(session_attributes, slots, current_intent, message)
    
            else:
                if slot_to_elicit is None:
                    request_create_ticket_handler(session_attributes, slots)
                return formDelegateResponse(session_attributes, slots, current_intent)
                
    else:
        return formElicitSlotWithTemplateResponse(session_attributes, TICKET_TYPE, TEMPLATES['CREATE_TICKET'], INTERACTIVE_OPTIONS['CREATE_TICKET']['slots'], INTERACTIVE_OPTIONS['CREATE_TICKET']['intent'])
