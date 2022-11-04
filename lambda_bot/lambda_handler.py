def lambda_handler(event, context):

    input, current_intent, slot_to_elicit, slots, session_attributes, template, title_elicit, description_elicit, continue_chatbot = setup_variables(event)

    from constants.constants import START_INTENT, CREATE_TICKET_INTENT, CHECK_TICKET_STATUS_INTENT, FALLBACK_INTENT

    from handlers.start_intent_handler import start_intent_handler
    from handlers.create_ticket_intent_handler import create_ticket_handler
    from handlers.check_ticket_status_intent_handler import check_ticket_status_handler
    from handlers.fallback_intent_handler import fallback_handler
    from handlers.response_handler import formDelegateResponse


    if current_intent == START_INTENT:
        return start_intent_handler(input, event, session_attributes, slots, current_intent, template, slot_to_elicit)
    
    elif current_intent == CREATE_TICKET_INTENT:
        return create_ticket_handler(input, slots, session_attributes, current_intent, slot_to_elicit, title_elicit, description_elicit, continue_chatbot)

    elif current_intent == CHECK_TICKET_STATUS_INTENT:
        return check_ticket_status_handler(session_attributes, input, slots, current_intent)

    elif current_intent == FALLBACK_INTENT:
        return fallback_handler(session_attributes)

    elif current_intent == "talkAgentIntent":
        return formDelegateResponse(session_attributes, slots, current_intent)

    else:
        return formDelegateResponse(session_attributes, slots, current_intent)


def setup_variables(event):

    from utils.locale import Locale
    from constants.messages import get_interactive_options

    session_attributes = event["sessionState"]["sessionAttributes"]

    locale = Locale()
    locale.set_locale(session_attributes["locale"][1:3])

    from constants.constants import SESSION_ATTRIBUTES

    input = event["inputTranscript"]
    current_intent = event["sessionState"]["intent"]["name"]
        
    slots = event["sessionState"]["intent"]["slots"]

    template = [template for template in get_interactive_options() if get_interactive_options()[template]['input'] == input]

    slot_to_elicit = None
    if event.get("proposedNextState"):
        slot_to_elicit = event["proposedNextState"]["dialogAction"]["slotToElicit"]

    title_elicit = None
    if session_attributes.get(SESSION_ATTRIBUTES['TITLE_ELICIT']):
        title_elicit = session_attributes[SESSION_ATTRIBUTES['TITLE_ELICIT']]

    description_elicit = None
    if session_attributes.get(SESSION_ATTRIBUTES['DESCRIPTION_ELICIT']):
        description_elicit = session_attributes[SESSION_ATTRIBUTES['DESCRIPTION_ELICIT']]

    continue_chatbot = None
    if session_attributes.get(SESSION_ATTRIBUTES['CONTINUE_CHATBOT']):
        continue_chatbot = session_attributes[SESSION_ATTRIBUTES['CONTINUE_CHATBOT']]

    return input, current_intent, slot_to_elicit, slots, session_attributes, template, title_elicit, description_elicit, continue_chatbot
