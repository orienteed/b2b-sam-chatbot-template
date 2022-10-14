from .requests_hadler import check_ticket_states_handler
from .response_handler import formTerminalResponse

def check_ticket_status_handler(session_attributes, input, slots, current_intent):
    status = check_ticket_states_handler(session_attributes, input)
    return formTerminalResponse(session_attributes, slots, current_intent, status)