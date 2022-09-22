from re import TEMPLATE
from handlers.user_input_handler import *
from constants.constants import INTERACTIVE_OPTIONS, START_INTENT, CREATE_TICKET_INTENT, CREATE_TICKET_OPTIONS

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
    print('Current intent: ', current_intent)

    # HANDLE INTENT 'startIntent'
    if current_intent == START_INTENT:
        if event["sessionState"]["intent"]["slots"]["primero"] is None:
            return createSimpleListPickerFromOptions(session_attributes, slot_to_elicit, slots, current_intent)

        elif len(template) > 0:
            return handleInteractiveOptionResponseElicitAnotherIntent(session_attributes, template[0])

        elif slot_to_elicit is None:
            return handleElicitSlot(session_attributes, slot_to_elicit, slots)
    
    elif current_intent == CREATE_TICKET_INTENT:
        print('En create ticket')
        if slots.get("ticketType")['value']['originalValue'] == CREATE_TICKET_OPTIONS['TITLE_ORDER_TICKET'] and slots.get("orderNumber") is None:
                return handleElicitSlot(session_attributes, "orderNumber", slots, current_intent)
        else:
            if slots.get("title") is None:
                print('En otro ticket')
                return handleElicitSlot(session_attributes, "title", slots, current_intent)

            else:
                # if slot_to_elicit is None:
                #     print("en terminal response")
                #     return handlerTerminalResponse(session_attributes, slots)
                return handlerDelegate(session_attributes, slots, current_intent)
