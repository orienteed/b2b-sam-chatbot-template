TEMPLATE_TYPES = {
    'LISTPICKER': 'ListPicker',
    'TIMEPICKER': 'TimePicker'
}

TEMPLATES = {
    "BOT_OPTIONS": "BOT_OPTIONS",
    "CREATE_TICKET": "CREATE_TICKET"
}

DIALOG_ACTIONS_TYPES = {
    'CLOSE': 'Close',
    'CONFIRM_INTENT': 'ConfirmIntent',
    'DELEGATE': 'Delegate',
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


ZAMMAD_HEADERS = {
    'AUTHORIZATION': 'Authorization',
    'CSR_AUTHORIZATION': 'csr-authorization',
    'CONTENT_TYPE': 'Content-Type',
}

TICKET_TYPE_ZAMMAD = {
    'Support ticket': 'Support issue',
    'Order ticket': 'Order issue',
    'Enhancement ticket': 'Enhancement'
}

CHECK_TICKET_STATES_MESSAGES = {
    'TICKET_FOUND': 'The status of ticket {} is {}',
    'TICKET_NOT_FOUND': 'Ticket {} not found'
}

CREATE_TICKET_MESSAGES = {
    'TICKET_CREATED': 'Ticket created with number {}',
    'TICKET_NOT_CREATED': 'Error creating the ticket'
}


START_INTENT = 'startIntent'
CREATE_TICKET_INTENT = 'createTicketIntent'
TALK_TO_AGENT_INTENT = 'talkToAgentIntent'
CHECK_TICKET_STATUS_INTENT = 'checkTicketStatusIntent'


START_INTENT_SLOTS = {
    'OPTIONS': 'options'
}

CREATE_TICKET_INTENT_SLOTS = {
    'TICKET_TYPE': 'ticketType',
    'ORDER_NUMBER': 'orderNumber',
    'TITLE': 'title',
    'DESCRIPTION': 'description'
}

CHECK_TICKET_STATUS_INTENT_SLOTS = {
    'TICKET_NUMBER': 'ticketNumber'
}

SESSION_ATTRIBUTES = {
    'MAGENTO_TOKEN': 'magento_token',
    'TITLE_ELICIT': 'title_elicit',
    'DESCRIPTION_ELICIT': 'description_elicit'
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
            CREATE_TICKET_INTENT_SLOTS['TICKET_TYPE']: None,
            CREATE_TICKET_INTENT_SLOTS['ORDER_NUMBER']: None,
            CREATE_TICKET_INTENT_SLOTS['TITLE']: None,
            CREATE_TICKET_INTENT_SLOTS['DESCRIPTION']: None
        }
    }
}

CHECK_TICKET_STATUS = {
    'input': CHATBOT_OPTIONS['TITLE_TICKET_STATUS'],
    'intent': CHECK_TICKET_STATUS_INTENT,
    'slots': {
        CHECK_TICKET_STATUS_INTENT_SLOTS['TICKET_NUMBER']: None
    }
}

SLOTS_STRUCTURE = {
    'shape': 'Scalar', 
    'value': {
        'resolvedValues': [{}], 
        'interpretedValue': {}, 
        'originalValue': {}
    }
}
