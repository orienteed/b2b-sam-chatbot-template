def get_template_create_ticket():
    from constants.constants import TEMPLATE_TYPES
    from constants.messages import get_create_ticket_options

    CREATE_TICKET = {
        "templateType": TEMPLATE_TYPES["LISTPICKER"],
        "version": "1.0",
        "data": {
            "content": {
                "title": get_create_ticket_options()["CARD_TITLE"],
                "elements": [
                    {"title": get_create_ticket_options()["TITLE_SUPPORT_TICKET"]},
                    {"title": get_create_ticket_options()["TITLE_ORDER_TICKET"]},
                    {"title": get_create_ticket_options()["TITLE_ENHANCEMENT_TICKET"]},
                ],
            },
        },
    }

    return CREATE_TICKET


def get_template_bot_options():

    from constants.constants import TEMPLATE_TYPES
    from constants.messages import get_chatbot_options

    BOT_OPTIONS = {
        "templateType": TEMPLATE_TYPES["LISTPICKER"],
        "version": "1.0",
        "data": {
            "content": {
                "title": get_chatbot_options()["CARD_TITLE"],
                "elements": [
                    {"title": get_chatbot_options()["TITLE_CREATE_TICKET"]},
                    {"title": get_chatbot_options()["TITLE_TICKET_STATUS"]},
                    {"title": get_chatbot_options()["TITLE_TALK_TO_AGENT"]},
                ],
            },
        },
    }

    return BOT_OPTIONS


def get_template_continue_chatbot():

    from constants.constants import TEMPLATE_TYPES
    from constants.messages import get_continue_chatbot_options

    CONTINUE_CHATBOT = {
        "templateType": TEMPLATE_TYPES["LISTPICKER"],
        "version": "1.0",
        "data": {
            "content": {
                "title": get_continue_chatbot_options()["CARD_TITLE"],
                "elements": [
                    {"title": get_continue_chatbot_options()["TITLE_YES"]},
                    {"title": get_continue_chatbot_options()["TITLE_NO"]},
                ],
            },
        },
    }

    return CONTINUE_CHATBOT
