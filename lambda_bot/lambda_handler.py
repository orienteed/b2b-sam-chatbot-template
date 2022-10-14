from constants.constants import INTERACTIVE_OPTIONS, START_INTENT, CREATE_TICKET_INTENT, CHECK_TICKET_STATUS_INTENT
from handlers.requests_hadler import *

from handlers.start_intent_handler import *
from handlers.create_ticket_intent_handler import *
from handlers.check_ticket_status_intent_handler import *
from handlers.response_handler import formDelegateResponse

def lambda_handler(event, context):

    input, current_intent, slot_to_elicit, slots, session_attributes, template, title_elicit, description_elicit = setup_variables(event)

    if current_intent == START_INTENT:
        return start_intent_handler(input, event, session_attributes, slots, current_intent, template, slot_to_elicit)
    
    elif current_intent == CREATE_TICKET_INTENT:
        return create_ticket_handler(input, slots, session_attributes, current_intent, slot_to_elicit, title_elicit, description_elicit)

    elif current_intent == CHECK_TICKET_STATUS_INTENT:
        return check_ticket_status_handler(session_attributes, input, slots, current_intent)

    else:
        return formDelegateResponse(session_attributes, slots, current_intent)

def setup_variables(event):
    input = event["inputTranscript"]
    current_intent = event["sessionState"]["intent"]["name"]
        
    slots = event["sessionState"]["intent"]["slots"]
    session_attributes = event["sessionState"]["sessionAttributes"]
    template = [template for template in INTERACTIVE_OPTIONS if INTERACTIVE_OPTIONS[template]['input'] == input]

    slot_to_elicit = None
    if event.get("proposedNextState"):
        slot_to_elicit = event["proposedNextState"]["dialogAction"]["slotToElicit"]

    title_elicit = None
    if session_attributes.get(SESSION_ATTRIBUTES['TITLE_ELICIT']):
        title_elicit = session_attributes[SESSION_ATTRIBUTES['TITLE_ELICIT']]

    description_elicit = None
    if session_attributes.get(SESSION_ATTRIBUTES['DESCRIPTION_ELICIT']):
        description_elicit = session_attributes[SESSION_ATTRIBUTES['DESCRIPTION_ELICIT']]

    return input, current_intent, slot_to_elicit, slots, session_attributes, template, title_elicit, description_elicit
