from .response_handler import formDelegateResponse, formElicitSlotResponse, formElicitSlotWithTemplateResponse, formTerminalResponse
from templates.response_cards import TEMPLATES
from constants.constants import INTERACTIVE_OPTIONS

def handleElicitSlot(session_attributes, slot_to_elicit, slots, intent):
    print(formElicitSlotResponse(session_attributes, slot_to_elicit, slots, intent))
    return formElicitSlotResponse(session_attributes, slot_to_elicit, slots, intent)


def handlerDelegate(session_attributes, slots, intent):
    print(formDelegateResponse(session_attributes, slots, intent))
    return formDelegateResponse(session_attributes, slots, intent)

def handleInteractiveOptionResponseElicitAnotherIntent(session_attributes, template):
    print(formElicitSlotWithTemplateResponse(session_attributes, "ticketType", TEMPLATES[template], INTERACTIVE_OPTIONS[template]['slots'], INTERACTIVE_OPTIONS[template]['intent']))
    return formElicitSlotWithTemplateResponse(session_attributes, "ticketType", TEMPLATES[template], INTERACTIVE_OPTIONS[template]['slots'], INTERACTIVE_OPTIONS[template]['intent'])

def handleOtherResponse():
    pass

def handlerTerminalResponse(session_attributes, slots):
    print(formTerminalResponse(session_attributes, slots))
    return formTerminalResponse(session_attributes, slots)

def createSimpleListPickerFromOptions(session_attributes, slot_to_elicit, slots, current_intent):
    print(formElicitSlotWithTemplateResponse(session_attributes, slot_to_elicit, TEMPLATES["BOT_OPTIONS"], slots, current_intent))
    return formElicitSlotWithTemplateResponse(session_attributes, slot_to_elicit, TEMPLATES["BOT_OPTIONS"], slots, current_intent)