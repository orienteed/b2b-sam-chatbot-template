def fallback_handler(session_attributes):
    from utils.form_response import formElicitIntentTemplateBotOptionsResponse
    from templates.response_cards import get_template_bot_options
    

    TEMPLATE_BOT_OPTIONS = get_template_bot_options()


    return formElicitIntentTemplateBotOptionsResponse(session_attributes, TEMPLATE_BOT_OPTIONS)