from handlers.user_input_handler import *
from constants.constants import INTERACTIVE_OPTIONS, START_INTENT, CREATE_TICKET_INTENT, CREATE_TICKET_OPTIONS, CHECK_TICKET_STATUS_INTENT, CHECK_TICKET_STATUS
from handlers.requests_hadler import *

def lambda_handler(event, context):
    print(event)

    input = event["inputTranscript"]
    current_intent = event["sessionState"]["intent"]["name"]

    slot_to_elicit = None
    if event.get("proposedNextState"):
        slot_to_elicit = event["proposedNextState"]["dialogAction"]["slotToElicit"]
        
    slots = event["sessionState"]["intent"]["slots"]
    session_attributes = event["sessionState"]["sessionAttributes"]
    template = [template for template in INTERACTIVE_OPTIONS if INTERACTIVE_OPTIONS[template]['input'] == input]

    title_elicit = None
    if session_attributes.get("title_elicit"):
        title_elicit = session_attributes["title_elicit"]

    description_elicit = None
    if session_attributes.get("description_elicit"):
        description_elicit = session_attributes["description_elicit"]


    # HANDLE INTENT 'startIntent'
    if current_intent == START_INTENT:
        if event["sessionState"]["intent"]["slots"]["primero"] is None:
            return createSimpleListPickerFromOptions(session_attributes, slot_to_elicit, slots, current_intent)

        elif len(template) > 0:
            return handleInteractiveOptionResponseElicitAnotherIntent(session_attributes, template[0])

        elif slot_to_elicit is None:
            if input == CHECK_TICKET_STATUS['input']:
                return handleElicitSlot(session_attributes, "ticketNumber", CHECK_TICKET_STATUS['slots'], CHECK_TICKET_STATUS['intent'])
            return handlerDelegate(session_attributes, slots, current_intent)
    
    elif current_intent == CREATE_TICKET_INTENT:
        if slots.get("ticketType")['value']['originalValue'] == CREATE_TICKET_OPTIONS['TITLE_ORDER_TICKET'] and slots.get("orderNumber") is None:
                return handleElicitSlot(session_attributes, "orderNumber", slots, current_intent)
        else:
            if slots.get("title") is None and title_elicit is None:
                session_attributes['title_elicit'] = True
                return handleElicitSlot(session_attributes, "title", slots, current_intent)

            if title_elicit and not description_elicit:
                session_attributes['description_elicit'] = True
                slots['title'] = {
                    'shape': 'Scalar', 
                    'value': {
                        'resolvedValues': [input], 
                        'interpretedValue': input, 
                        'originalValue': input
                    }
                }
                return handleElicitSlot(session_attributes, "description", slots, current_intent)

            if title_elicit and description_elicit:
                slots['description'] = {
                    'shape': 'Scalar', 
                    'value': {
                        'resolvedValues': [input], 
                        'interpretedValue': input, 
                        'originalValue': input
                    }
                }
                message = create_ticket_handler(session_attributes, slots)
                return handlerTerminalResponse(session_attributes, slots, current_intent, message)

            else:
                if slot_to_elicit is None:
                    create_ticket_handler(session_attributes, slots)
                return handlerDelegate(session_attributes, slots, current_intent)

    elif current_intent == CHECK_TICKET_STATUS_INTENT:
        status = check_ticket_states_handler(session_attributes, input)
        return handlerTerminalResponse(session_attributes, slots, current_intent, status)

    else:
        print("Ninguna coincidencia")
        return handlerDelegate(session_attributes, slots, current_intent)
