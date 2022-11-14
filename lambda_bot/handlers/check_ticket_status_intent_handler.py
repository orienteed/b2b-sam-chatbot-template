def check_ticket_status_handler(session_attributes, input, slots, current_intent):

    from .zammad_requests_handler import check_ticket_states_handler
    
    from utils.form_response import formElicitSlotWithTemplateResponse, formElicitSlotResponse
    from utils.manage_continue_chatbot_form import manage_continue_chatbot_form
    
    from constants.messages import get_check_ticket_states_messages, get_check_ticket_status
    from constants.constants import CHECK_TICKET_STATUS_INTENT_SLOTS
    

    from templates.response_cards import get_template_continue_chatbot


    TEMPLATE_CONTINUE_CHATBOT = get_template_continue_chatbot()
    CONTINUE_CHATBOT = CHECK_TICKET_STATUS_INTENT_SLOTS["CONTINUE_CHATBOT"]

    TICKET_NUMBER = CHECK_TICKET_STATUS_INTENT_SLOTS["TICKET_NUMBER"]

    CHECK_TICKET_SLOTS = get_check_ticket_status()["slots"]
    CHECK_TICKET_INTENT = get_check_ticket_status()["intent"]

    ELICIT_TICKET_NUMBER_MESSAGE = get_check_ticket_states_messages()["ELICIT_TICKET_NUMBER_MESSAGE"]

    if slots.get(CONTINUE_CHATBOT) is not None:
        return manage_continue_chatbot_form(slots, session_attributes, current_intent)

    else:
        if session_attributes.get("ticketNumber_elicit") is not None:
            return formElicitSlotWithTemplateResponse(
                session_attributes, CONTINUE_CHATBOT, TEMPLATE_CONTINUE_CHATBOT, slots, current_intent
            )

        else:
            if slots.get(TICKET_NUMBER) is None:
                return formElicitSlotResponse(
                    session_attributes, TICKET_NUMBER, CHECK_TICKET_SLOTS, CHECK_TICKET_INTENT, message=ELICIT_TICKET_NUMBER_MESSAGE
                )

            else:
                status = check_ticket_states_handler(session_attributes, input)
                session_attributes["ticketNumber_elicit"] = True

                return formElicitSlotWithTemplateResponse(
                    session_attributes, CONTINUE_CHATBOT, TEMPLATE_CONTINUE_CHATBOT, slots, current_intent, status
                )
