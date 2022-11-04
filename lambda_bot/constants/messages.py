def get_create_ticket_options():
    from utils.locale import Locale

    locale = Locale()
    CREATE_TICKET_OPTIONS = {
        "CARD_TITLE": locale.get_i18n().t("CREATE_TICKET_OPTIONS:CARD_TITLE", locale=locale.get_locale()),
        "CARD_SUBTITLE": locale.get_i18n().t("CREATE_TICKET_OPTIONS:CARD_SUBTITLE", locale=locale.get_locale()),
        "TITLE_SUPPORT_TICKET": locale.get_i18n().t("CREATE_TICKET_OPTIONS:TITLE_SUPPORT_TICKET", locale=locale.get_locale()),
        "SUBTITLE_SUPPORT_TICKET": locale.get_i18n().t("CREATE_TICKET_OPTIONS:SUBTITLE_SUPPORT_TICKET", locale=locale.get_locale()),
        "TITLE_ORDER_TICKET": locale.get_i18n().t("CREATE_TICKET_OPTIONS:TITLE_ORDER_TICKET", locale=locale.get_locale()),
        "SUBTITLE_ORDER_TICKET": locale.get_i18n().t("CREATE_TICKET_OPTIONS:SUBTITLE_ORDER_TICKET", locale=locale.get_locale()),
        "TITLE_ENHANCEMENT_TICKET": locale.get_i18n().t("CREATE_TICKET_OPTIONS:TITLE_ENHANCEMENT_TICKET", locale=locale.get_locale()),
        "SUBTITLE_ENHANCEMENT_TICKET": locale.get_i18n().t("CREATE_TICKET_OPTIONS:SUBTITLE_ENHANCEMENT_TICKET", locale=locale.get_locale()),
    }

    return CREATE_TICKET_OPTIONS


def get_chatbot_options():

    from utils.locale import Locale

    locale = Locale()

    CHATBOT_OPTIONS = {
        "CARD_TITLE": locale.get_i18n().t("CHATBOT_OPTIONS:CARD_TITLE", locale=locale.get_locale()),
        "CARD_SUBTITLE": locale.get_i18n().t("CHATBOT_OPTIONS:CARD_SUBTITLE", locale=locale.get_locale()),
        "TITLE_CREATE_TICKET": locale.get_i18n().t("CHATBOT_OPTIONS:TITLE_CREATE_TICKET", locale=locale.get_locale()),
        "SUBTITLE_CREATE_TICKET": locale.get_i18n().t("CHATBOT_OPTIONS:SUBTITLE_CREATE_TICKET", locale=locale.get_locale()),
        "TITLE_TICKET_STATUS": locale.get_i18n().t("CHATBOT_OPTIONS:TITLE_TICKET_STATUS", locale=locale.get_locale()),
        "SUBTITLE_TICKET_STATUS": locale.get_i18n().t("CHATBOT_OPTIONS:SUBTITLE_TICKET_STATUS", locale=locale.get_locale()),
        "TITLE_TALK_TO_AGENT": locale.get_i18n().t("CHATBOT_OPTIONS:TITLE_TALK_TO_AGENT", locale=locale.get_locale()),
        "SUBTITLE_TALK_TO_AGENT": locale.get_i18n().t("CHATBOT_OPTIONS:SUBTITLE_TALK_TO_AGENT", locale=locale.get_locale()),
    }

    return CHATBOT_OPTIONS


def get_interactive_options():
    from constants.constants import CREATE_TICKET_INTENT, CREATE_TICKET_INTENT_SLOTS

    INTERACTIVE_OPTIONS = {
        "CREATE_TICKET": {
            "input": get_chatbot_options()["TITLE_CREATE_TICKET"],
            "intent": CREATE_TICKET_INTENT,
            "slots": {
                CREATE_TICKET_INTENT_SLOTS["TICKET_TYPE"]: None,
                CREATE_TICKET_INTENT_SLOTS["ORDER_NUMBER"]: None,
                CREATE_TICKET_INTENT_SLOTS["TITLE"]: None,
                CREATE_TICKET_INTENT_SLOTS["DESCRIPTION"]: None,
            },
        }
    }

    return INTERACTIVE_OPTIONS


def get_check_ticket_states_messages(ticket_number=None, state=None):

    from utils.locale import Locale

    locale = Locale()

    CHECK_TICKET_STATES_MESSAGES = {
        "ELICIT_TICKET_NUMBER_MESSAGE": locale.get_i18n().t(
            "CHECK_TICKET_STATES_MESSAGES:ELICIT_TICKET_NUMBER_MESSAGE", locale=locale.get_locale()
        ),
        "TICKET_FOUND": locale.get_i18n().t(
            "CHECK_TICKET_STATES_MESSAGES:TICKET_FOUND", locale=locale.get_locale(), ticket_number=ticket_number, state=state
        ),
        "TICKET_NOT_FOUND": locale.get_i18n().t(
            "CHECK_TICKET_STATES_MESSAGES:TICKET_NOT_FOUND", locale=locale.get_locale(), ticket_number=ticket_number
        ),
        "new": locale.get_i18n().t("CHECK_TICKET_STATES_MESSAGES:STATE_NEW", locale=locale.get_locale()),
        "open": locale.get_i18n().t("CHECK_TICKET_STATES_MESSAGES:STATE_OPEN", locale=locale.get_locale()),
        "closed": locale.get_i18n().t("CHECK_TICKET_STATES_MESSAGES:STATE_CLOSED", locale=locale.get_locale()),
    }

    return CHECK_TICKET_STATES_MESSAGES


def get_create_ticket_messages(ticket_number=None):
    from utils.locale import Locale

    locale = Locale()
    CREATE_TICKET_MESSAGES = {
        "ELICIT_TITLE_MESSAGE": locale.get_i18n().t("CREATE_TICKET_MESSAGES:ELICIT_TITLE_MESSAGE", locale=locale.get_locale()),
        "ELICIT_DESCRIPTION_MESSAGE": locale.get_i18n().t("CREATE_TICKET_MESSAGES:ELICIT_DESCRIPTION_MESSAGE", locale=locale.get_locale()),
        "TICKET_CREATED": locale.get_i18n().t(
            "CREATE_TICKET_MESSAGES:TICKET_CREATED", locale=locale.get_locale(), ticket_number=ticket_number
        ),
        "TICKET_NOT_CREATED": locale.get_i18n().t("CREATE_TICKET_MESSAGES:TICKET_NOT_CREATED", locale=locale.get_locale()),
    }

    return CREATE_TICKET_MESSAGES


def get_ticket_type_zammad():
    from utils.locale import Locale

    locale = Locale()
    TICKET_TYPE_ZAMMAD = {
        locale.get_i18n().t("CREATE_TICKET_OPTIONS:TITLE_SUPPORT_TICKET", locale=locale.get_locale()): "Support issue",
        locale.get_i18n().t("CREATE_TICKET_OPTIONS:TITLE_ORDER_TICKET", locale=locale.get_locale()): "Order issue",
        locale.get_i18n().t("CREATE_TICKET_OPTIONS:TITLE_ENHANCEMENT_TICKET", locale=locale.get_locale()): "Enhancement",
    }

    return TICKET_TYPE_ZAMMAD


def get_check_ticket_status():
    from constants.constants import CHECK_TICKET_STATUS_INTENT, CHECK_TICKET_STATUS_INTENT_SLOTS
    CHECK_TICKET_STATUS = {
        "input": get_chatbot_options()["TITLE_TICKET_STATUS"],
        "intent": CHECK_TICKET_STATUS_INTENT,
        "slots": {CHECK_TICKET_STATUS_INTENT_SLOTS["TICKET_NUMBER"]: None, CHECK_TICKET_STATUS_INTENT_SLOTS["CONTINUE_CHATBOT"]: None},
    }

    return CHECK_TICKET_STATUS


def get_continue_chatbot_options():
    from utils.locale import Locale

    locale = Locale()
    CONTINUE_CHATBOT_MESSAGES = {
        "CARD_TITLE": locale.get_i18n().t("CONTINUE_CHATBOT_MESSAGES:CARD_TITLE", locale=locale.get_locale()),
        "CARD_SUBTITLE": locale.get_i18n().t("CONTINUE_CHATBOT_MESSAGES:CARD_SUBTITLE", locale=locale.get_locale()),
        "TITLE_YES": locale.get_i18n().t("CONTINUE_CHATBOT_MESSAGES:TITLE_YES", locale=locale.get_locale()),
        "TITLE_NO": locale.get_i18n().t("CONTINUE_CHATBOT_MESSAGES:TITLE_NO", locale=locale.get_locale())
    }

    return CONTINUE_CHATBOT_MESSAGES
