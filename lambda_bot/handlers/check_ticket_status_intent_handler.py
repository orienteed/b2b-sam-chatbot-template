def check_ticket_status_handler(session_attributes, input, slots, current_intent):

    from .requests_hadler import check_ticket_states_handler
    from .response_handler import formElicitSlotWithTemplateResponse, formDelegateResponse, formElicitIntentTemplateBotOptionsResponse
    from constants.messages import get_check_ticket_states_messages, get_check_ticket_status
    from constants.constants import (
        CHECK_TICKET_STATUS_INTENT_SLOTS,
        SESSION_ATTRIBUTES
    )

    from templates.response_cards import get_template_bot_options, get_template_continue_chatbot

    from .response_handler import formElicitSlotResponse

    from utils.locale import Locale

    locale = Locale()


    TEMPLATE_CONTINUE_CHATBOT = get_template_continue_chatbot()
    TEMPLATE_BOT_OPTIONS = get_template_bot_options()
    CONTINUE_CHATBOT = CHECK_TICKET_STATUS_INTENT_SLOTS["CONTINUE_CHATBOT"]

    TICKET_NUMBER = CHECK_TICKET_STATUS_INTENT_SLOTS["TICKET_NUMBER"]

    CHECK_TICKET_INPUT = get_check_ticket_status()["input"]
    CHECK_TICKET_SLOTS = get_check_ticket_status()["slots"]
    CHECK_TICKET_INTENT = get_check_ticket_status()["intent"]

    ELICIT_TICKET_NUMBER_MESSAGE = get_check_ticket_states_messages()["ELICIT_TICKET_NUMBER_MESSAGE"]

    if slots.get(CONTINUE_CHATBOT) is not None:

        if slots.get(CONTINUE_CHATBOT)["value"]["originalValue"] == locale.get_i18n().t("CONTINUE_CHATBOT_MESSAGES:TITLE_YES", locale=locale.get_locale()):
            session_attributes[SESSION_ATTRIBUTES["CONTINUE_CHATBOT"]] = None
            session_attributes["ticketNumber_elicit"] = None
            
            return formElicitIntentTemplateBotOptionsResponse(session_attributes, TEMPLATE_BOT_OPTIONS)

        else:
            return formDelegateResponse(session_attributes, slots, current_intent)

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
