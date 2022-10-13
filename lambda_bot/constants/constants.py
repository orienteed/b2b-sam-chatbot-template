TEMPLATE_TYPES = {
    'LISTPICKER': 'ListPicker',
    'TIMEPICKER': 'TimePicker'
}

START_INTENT = 'startIntent'
CREATE_TICKET_INTENT = 'createTicketIntent'
TALK_TO_AGENT_INTENT = 'talkToAgentIntent'
CHECK_TICKET_STATUS_INTENT = 'checkTicketStatusIntent'

TICKET_TYPE_ZAMMAD = {
    'Support ticket': 'Support issue',
    'Order ticket': 'Order issue',
    'Enhancement ticket': 'Enhancement'
}

IMAGE_URLS = {
    'CREATE_TICKET': 'https://s3.amazonaws.com/sam-chatbot-app/images/create_ticket.png',
    'TICKET_STATUS': 'https://s3.amazonaws.com/sam-chatbot-app/images/ticket_status.png',
    'TALK_TO_AGENT': 'https://s3.amazonaws.com/sam-chatbot-app/images/talk_to_agent.png'
}

DIALOG_ACTIONS_TYPES = {
    'CLOSE': 'Close',
    'CONFIRM_INTENT': 'ConfirmIntent',
    'DELERGATE': 'Delegate',
    'ELICIT_INTENT': 'ElicitIntent',
    'ELICIT_SLOT': 'ElicitSlot'
}

INTENT_STATES = {
    'FAILED': 'Failed',
    'FULFILLED': 'Fulfilled',
    'FULFILLMENT_IN_PROGRESS': 'FulfillmentInProgress',
    'IN_PROGRESS': 'InProgress',
    'READY_FOR_FULFILLMENT': 'ReadyForFulfillment',
    'WAITING': 'Waiting'
}


MESSAGES_CONTENT_TYPES = {
    'CUSTOM_PAYLOAD': 'CustomPayload',
    'IMAGE_RESPONSE_CARD': 'ImageResponseCard',
    'PLAIN_TEXT': 'PlainText',
    'SSML': 'SSML'
}

CHATBOT_OPTIONS = {
    'CARD_TITLE': 'What would you like to do?',
    'CARD_SUBTITLE': 'Please select an option below.',
    'TITLE_CREATE_TICKET': 'Create a ticket',
    'SUBTITLE_CREATE_TICKET': 'Create a ticket for a problem you are experiencing.',
    'TITLE_TICKET_STATUS': 'Check ticket status',
    'SUBTITLE_TICKET_STATUS': 'Check the status of a ticket you have already created.',
    'TITLE_TALK_TO_AGENT': 'Talk to an agent',
    'SUBTITLE_TALK_TO_AGENT': 'Talk to an agent to get help with your problem.'
}

CREATE_TICKET_OPTIONS = {
    'CARD_TITLE': 'What type of ticket would you like to create?',
    'CARD_SUBTITLE': 'Please select an option below.',
    'TITLE_SUPPORT_TICKET': 'Support ticket',
    'SUBTITLE_SUPPORT_TICKET': 'Create a ticket for a problem you are experiencing.',
    'TITLE_ORDER_TICKET': 'Order ticket',
    'SUBTITLE_ORDER_TICKET': 'Create a ticket for an order you have placed.',
    'TITLE_ENHANCEMENT_TICKET': 'Enhancement ticket',
    'SUBTITLE_ENHANCEMENT_TICKET': 'Create a ticket for an enhancement you would like to see.'
}

INTERACTIVE_OPTIONS = {
    'CREATE_TICKET': {
        'input': CHATBOT_OPTIONS['TITLE_CREATE_TICKET'],
        'intent': CREATE_TICKET_INTENT,
        'slots': {
            'ticketType': None,
            'orderNumber': None,
            'title': None,
            'description': None,
        }
    }
}

CHECK_TICKET_STATUS = {
    'input': CHATBOT_OPTIONS['TITLE_TICKET_STATUS'],
    'intent': CHECK_TICKET_STATUS_INTENT,
    'slots': {
        'ticketNumber': None
    }
}
