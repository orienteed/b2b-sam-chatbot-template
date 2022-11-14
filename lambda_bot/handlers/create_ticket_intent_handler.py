def create_ticket_handler(input, slots, session_attributes, current_intent, slot_to_elicit, title_elicit, description_elicit):

    from utils.form_response import formDelegateResponse, formElicitSlotResponse, formElicitSlotWithTemplateResponse
    from utils.manage_continue_chatbot_form import manage_continue_chatbot_form

    from constants.constants import get_slots_structure, CREATE_TICKET_INTENT_SLOTS, SESSION_ATTRIBUTES
    
    from .zammad_requests_handler import request_create_ticket_handler
    from constants.messages import get_create_ticket_messages, get_create_ticket_options, get_interactive_options

    from templates.response_cards import get_template_create_ticket, get_template_continue_chatbot

    
    TICKET_TYPE = CREATE_TICKET_INTENT_SLOTS['TICKET_TYPE']
    ORDER_NUMBER = CREATE_TICKET_INTENT_SLOTS['ORDER_NUMBER']
    TITLE = CREATE_TICKET_INTENT_SLOTS['TITLE']
    DESCRIPTION = CREATE_TICKET_INTENT_SLOTS['DESCRIPTION']
    CONTINUE_CHATBOT = CREATE_TICKET_INTENT_SLOTS['CONTINUE_CHATBOT']

    ELICIT_TITLE_MESSAGE = get_create_ticket_messages()['ELICIT_TITLE_MESSAGE']
    ELICIT_DESCRIPTION_MESSAGE = get_create_ticket_messages()['ELICIT_DESCRIPTION_MESSAGE']

    TITLE_ORDER_TICKET = get_create_ticket_options()['TITLE_ORDER_TICKET']

    TITLE_ELICIT = SESSION_ATTRIBUTES['TITLE_ELICIT']
    DESCRIPTION_ELICIT = SESSION_ATTRIBUTES['DESCRIPTION_ELICIT']

    TEMPLATE_TICKET_TYPE = get_template_create_ticket()

    INTERACTIVE_OPTIONS = get_interactive_options()

    TEMPLATE_CONTINUE_CHATBOT = get_template_continue_chatbot()
    
    if slots.get(TICKET_TYPE) is not None:
        if slots.get(TICKET_TYPE)['value']['originalValue'] == TITLE_ORDER_TICKET and slots.get(ORDER_NUMBER) is None:
            return formElicitSlotResponse(session_attributes, ORDER_NUMBER, slots, current_intent)
        
        if slots.get(CONTINUE_CHATBOT) is not None:
            return manage_continue_chatbot_form(slots, session_attributes, current_intent)
            
        #Bad input continue chatbot
        elif session_attributes.get('ticketNumber_elicit') is not None:
            session_attributes['ticketNumber_elicit'] = None
            return formElicitSlotWithTemplateResponse(session_attributes, CONTINUE_CHATBOT, TEMPLATE_CONTINUE_CHATBOT, slots, current_intent)

        
        else:
            if slots.get(TITLE) is None and title_elicit is None:
                session_attributes[TITLE_ELICIT] = True
                return formElicitSlotResponse(session_attributes, TITLE, slots, current_intent, ELICIT_TITLE_MESSAGE)
    
            elif title_elicit and not description_elicit:
                session_attributes[DESCRIPTION_ELICIT] = True
    
                slots[TITLE] = get_slots_structure(input)
            
                return formElicitSlotResponse(session_attributes, DESCRIPTION, slots, current_intent, ELICIT_DESCRIPTION_MESSAGE)
    
            elif title_elicit and description_elicit:
    
                slots[DESCRIPTION] = get_slots_structure(input)
    
                message = request_create_ticket_handler(session_attributes, slots)
                session_attributes['ticketNumber_elicit'] = True
                session_attributes['title_elicit'] = None
                session_attributes['description_elicit'] = None
                
                return formElicitSlotWithTemplateResponse(session_attributes, CONTINUE_CHATBOT, TEMPLATE_CONTINUE_CHATBOT, slots, current_intent, message)

            else:
                if slot_to_elicit is None:
                    request_create_ticket_handler(session_attributes, slots)

                return formDelegateResponse(session_attributes, slots, current_intent)
                
    else:
        return formElicitSlotWithTemplateResponse(session_attributes, TICKET_TYPE, TEMPLATE_TICKET_TYPE, INTERACTIVE_OPTIONS['CREATE_TICKET']['slots'], INTERACTIVE_OPTIONS['CREATE_TICKET']['intent'])