def start_intent_handler(input, event, session_attributes, slots, current_intent, template, slot_to_elicit):

    from constants.constants import START_INTENT_SLOTS, CREATE_TICKET_INTENT_SLOTS, CHECK_TICKET_STATUS_INTENT_SLOTS, ELICIT_START_INTENT_SLOTS, START_INTENT
    from .response_handler import formElicitSlotWithTemplateResponse, formElicitSlotResponse
    from constants.messages import (
        get_check_ticket_states_messages,
        get_interactive_options,
        get_check_ticket_status
    )

    from templates.response_cards import get_template_bot_options, get_template_create_ticket

    TICKET_TYPE = CREATE_TICKET_INTENT_SLOTS["TICKET_TYPE"]
    TICKET_NUMBER = CHECK_TICKET_STATUS_INTENT_SLOTS["TICKET_NUMBER"]

    CHECK_TICKET_INPUT = get_check_ticket_status()["input"]
    CHECK_TICKET_SLOTS = get_check_ticket_status()["slots"]
    CHECK_TICKET_INTENT = get_check_ticket_status()["intent"]

    ELICIT_TICKET_NUMBER_MESSAGE = get_check_ticket_states_messages()["ELICIT_TICKET_NUMBER_MESSAGE"]

    TEMPLATE_BOT_OPTIONS = get_template_bot_options()

    START_INTENT_OPTIONS = START_INTENT_SLOTS["OPTIONS"]

    INTERACTIVE_OPTIONS = get_interactive_options()

    if event["sessionState"]["intent"]["slots"][START_INTENT_OPTIONS] is None:
        return formElicitSlotWithTemplateResponse(session_attributes, slot_to_elicit, TEMPLATE_BOT_OPTIONS, slots, current_intent)

    elif len(template) > 0:
        return formElicitSlotWithTemplateResponse(
            session_attributes,
            TICKET_TYPE,
            get_template_create_ticket(),
            INTERACTIVE_OPTIONS[template[0]]["slots"],
            INTERACTIVE_OPTIONS[template[0]]["intent"],
        )

    elif slot_to_elicit is None:
        if input == CHECK_TICKET_INPUT:
            return formElicitSlotResponse(
                session_attributes, TICKET_NUMBER, CHECK_TICKET_SLOTS, CHECK_TICKET_INTENT, message=ELICIT_TICKET_NUMBER_MESSAGE
            )

        else:
            return formElicitSlotWithTemplateResponse(session_attributes, START_INTENT_SLOTS['OPTIONS'], TEMPLATE_BOT_OPTIONS, ELICIT_START_INTENT_SLOTS, START_INTENT)
