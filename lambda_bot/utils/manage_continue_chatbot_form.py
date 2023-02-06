def manage_continue_chatbot_form(slots, session_attributes, current_intent):
    from constants.constants import CREATE_TICKET_INTENT_SLOTS, SESSION_ATTRIBUTES
    from templates.response_cards import get_template_bot_options
    from .form_response import formDelegateResponse, formElicitIntentTemplateBotOptionsResponse

    from utils.locale import Locale

    locale = Locale()

    CONTINUE_CHATBOT = CREATE_TICKET_INTENT_SLOTS['CONTINUE_CHATBOT']
    TEMPLATE_BOT_OPTIONS = get_template_bot_options()

    if slots.get(CONTINUE_CHATBOT)["value"]["originalValue"] == locale.get_i18n().t("CONTINUE_CHATBOT_MESSAGES:TITLE_YES", locale=locale.get_locale()):
        session_attributes[SESSION_ATTRIBUTES["CONTINUE_CHATBOT"]] = None
        session_attributes["ticketNumber_elicit"] = None
        
        return formElicitIntentTemplateBotOptionsResponse(session_attributes, TEMPLATE_BOT_OPTIONS)

    else:
        return formDelegateResponse(session_attributes, slots, current_intent)