from constants.constants import INTERACTIVE_OPTIONS, START_INTENT_SLOTS, CREATE_TICKET_INTENT_SLOTS, CHECK_TICKET_STATUS_INTENT_SLOTS, CHECK_TICKET_STATUS, get_check_ticket_states_messages
from handlers.create_ticket_intent_handler import TICKET_TYPE
from templates.response_cards import TEMPLATES
from .response_handler import formElicitSlotWithTemplateResponse, formDelegateResponse, formElicitSlotResponse

TICKET_TYPE = CREATE_TICKET_INTENT_SLOTS['TICKET_TYPE']
TICKET_NUMBER = CHECK_TICKET_STATUS_INTENT_SLOTS['TICKET_NUMBER']

CHECK_TICKET_INPUT = CHECK_TICKET_STATUS['input']
CHECK_TICKET_SLOTS = CHECK_TICKET_STATUS['slots']
CHECK_TICKET_INTENT = CHECK_TICKET_STATUS['intent']

ELICIT_TICKET_NUMBER_MESSAGE = get_check_ticket_states_messages()['ELICIT_TICKET_NUMBER_MESSAGE']

TEMPLATE_BOT_OPTIONS = TEMPLATES['BOT_OPTIONS']

START_INTENT_OPTIONS = START_INTENT_SLOTS['OPTIONS']

def start_intent_handler(input, event, session_attributes, slots, current_intent, template, slot_to_elicit):
    if event["sessionState"]["intent"]["slots"][START_INTENT_OPTIONS] is None:
        return formElicitSlotWithTemplateResponse(session_attributes, slot_to_elicit, TEMPLATE_BOT_OPTIONS, slots, current_intent)

    elif len(template) > 0:
        return formElicitSlotWithTemplateResponse(session_attributes, TICKET_TYPE, TEMPLATES[template[0]], INTERACTIVE_OPTIONS[template[0]]['slots'], INTERACTIVE_OPTIONS[template[0]]['intent'])

    elif slot_to_elicit is None:
        if input == CHECK_TICKET_INPUT:
            return formElicitSlotResponse(session_attributes, TICKET_NUMBER, CHECK_TICKET_SLOTS, CHECK_TICKET_INTENT, message=ELICIT_TICKET_NUMBER_MESSAGE)

        return formDelegateResponse(session_attributes, slots, current_intent)