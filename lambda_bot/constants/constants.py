from utils.locale import Locale

locale = Locale()

TEMPLATE_TYPES = {"LISTPICKER": "ListPicker", "TIMEPICKER": "TimePicker"}

TEMPLATES = {"BOT_OPTIONS": "BOT_OPTIONS", "CREATE_TICKET": "CREATE_TICKET"}

DIALOG_ACTIONS_TYPES = {
    "CLOSE": "Close",
    "CONFIRM_INTENT": "ConfirmIntent",
    "DELEGATE": "Delegate",
    "ELICIT_INTENT": "ElicitIntent",
    "ELICIT_SLOT": "ElicitSlot",
}

INTENT_STATES = {
    "FAILED": "Failed",
    "FULFILLED": "Fulfilled",
    "FULFILLMENT_IN_PROGRESS": "FulfillmentInProgress",
    "IN_PROGRESS": "InProgress",
    "READY_FOR_FULFILLMENT": "ReadyForFulfillment",
    "WAITING": "Waiting",
}


MESSAGES_CONTENT_TYPES = {
    "CUSTOM_PAYLOAD": "CustomPayload",
    "IMAGE_RESPONSE_CARD": "ImageResponseCard",
    "PLAIN_TEXT": "PlainText",
    "SSML": "SSML",
}


ZAMMAD_HEADERS = {
    "AUTHORIZATION": "Authorization",
    "CSR_AUTHORIZATION": "api-authorization",
    "CONTENT_TYPE": "Content-Type",
}


START_INTENT = "startIntent"
CREATE_TICKET_INTENT = "createTicketIntent"
TALK_TO_AGENT_INTENT = "talkToAgentIntent"
CHECK_TICKET_STATUS_INTENT = "checkTicketStatusIntent"
FALLBACK_INTENT = "FallbackIntent"


START_INTENT_SLOTS = {"OPTIONS": "options"}

ELICIT_START_INTENT_SLOTS = {START_INTENT_SLOTS["OPTIONS"]: None}

CREATE_TICKET_INTENT_SLOTS = {
    "TICKET_TYPE": "ticketType",
    "ORDER_NUMBER": "orderNumber",
    "TITLE": "title",
    "DESCRIPTION": "description",
    "CONTINUE_CHATBOT": "continueChatbot",
}

CHECK_TICKET_STATUS_INTENT_SLOTS = {"TICKET_NUMBER": "ticketNumber", "CONTINUE_CHATBOT": "continueChatbot"}

SESSION_ATTRIBUTES = {
    "MAGENTO_TOKEN": "magento_token",
    "TITLE_ELICIT": "title_elicit",
    "DESCRIPTION_ELICIT": "description_elicit",
    "CONTINUE_CHATBOT": "continue_chatbot",
}

def get_slots_structure(input):
    SLOTS_STRUCTURE = {"shape": "Scalar", "value": {"resolvedValues": [input], "interpretedValue": input, "originalValue": input}}

    return SLOTS_STRUCTURE
