from constants.constants import TEMPLATES, TEMPLATE_TYPES, get_chatbot_options, get_create_ticket_options

TEMPLATES = {
    TEMPLATES["BOT_OPTIONS"]: {
        "templateType": TEMPLATE_TYPES['LISTPICKER'],
        "version": "1.0",
        "data": {
            "content": {
                "title": get_chatbot_options()['CARD_TITLE'],
                "subtitle": get_chatbot_options()['CARD_SUBTITLE'],
                "elements": [
                    {
                        "title": get_chatbot_options()['TITLE_CREATE_TICKET']
                    },
                    {
                        "title": get_chatbot_options()['TITLE_TICKET_STATUS']
                    },
                    {
                        "title": get_chatbot_options()['TITLE_TALK_TO_AGENT']
                    },
                ],
            },
        }
    },

    TEMPLATES["CREATE_TICKET"]: {
        "templateType": TEMPLATE_TYPES['LISTPICKER'],
        "version": "1.0",
        "data": {
            "content": {
                "title": get_create_ticket_options()['CARD_TITLE'],
                "subtitle": get_create_ticket_options()['CARD_SUBTITLE'],
                "elements": [
                    {
                        "title": get_create_ticket_options()['TITLE_SUPPORT_TICKET']
                    },
                    {
                        "title": get_create_ticket_options()['TITLE_ORDER_TICKET']
                    },
                    {
                        "title": get_create_ticket_options()['TITLE_ENHANCEMENT_TICKET']
                    },
                ],
            },
        }
    },
}