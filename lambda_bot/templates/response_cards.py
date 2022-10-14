from constants.constants import TEMPLATE_TYPES, CHATBOT_OPTIONS, CREATE_TICKET_OPTIONS, TEMPLATES

TEMPLATES = {
    TEMPLATES["BOT_OPTIONS"]: {
        "templateType": TEMPLATE_TYPES['LISTPICKER'],
        "version": "1.0",
        "data": {
            "content": {
                "title": CHATBOT_OPTIONS['CARD_TITLE'],
                "subtitle": CHATBOT_OPTIONS['CARD_SUBTITLE'],
                "elements": [
                    {
                        "title": CHATBOT_OPTIONS['TITLE_CREATE_TICKET']
                    },
                    {
                        "title": CHATBOT_OPTIONS['TITLE_TICKET_STATUS']
                    },
                    {
                        "title": CHATBOT_OPTIONS['TITLE_TALK_TO_AGENT']
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
                "title": CREATE_TICKET_OPTIONS['CARD_TITLE'],
                "subtitle": CREATE_TICKET_OPTIONS['CARD_SUBTITLE'],
                "elements": [
                    {
                        "title": CREATE_TICKET_OPTIONS['TITLE_SUPPORT_TICKET']
                    },
                    {
                        "title": CREATE_TICKET_OPTIONS['TITLE_ORDER_TICKET']
                    },
                    {
                        "title": CREATE_TICKET_OPTIONS['TITLE_ENHANCEMENT_TICKET']
                    },
                ],
            },
        }
    },
}