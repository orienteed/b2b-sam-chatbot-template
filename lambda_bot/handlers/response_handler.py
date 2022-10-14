import json
from constants.constants import DIALOG_ACTIONS_TYPES, INTENT_STATES, MESSAGES_CONTENT_TYPES

def formElicitSlotWithTemplateResponse(session_attributes, slot_to_elicit, template, slots, intent):
    return {
		"sessionState": {
            "sessionAttributes": session_attributes,
			"dialogAction": {
				"type": DIALOG_ACTIONS_TYPES["ELICIT_SLOT"],
				"slotToElicit": slot_to_elicit,

			},
			"intent": {
                "name": intent,
                "slots": slots,
                "state": INTENT_STATES["IN_PROGRESS"]
            },
		},

		"messages": [{
			"contentType": MESSAGES_CONTENT_TYPES["CUSTOM_PAYLOAD"],
			"content": json.dumps(template, separators=(',', ':'))
		}],
    }


def formTerminalResponse(session_attributes, slots, intent, message):
    return {
        "sessionState": {
			"dialogAction": {
				"type": DIALOG_ACTIONS_TYPES["CLOSE"],
			},
            "intent": {
                "name": intent,
                "state": INTENT_STATES["FULFILLED"],
            }
        },
        "messages": [{
            "contentType": MESSAGES_CONTENT_TYPES["PLAIN_TEXT"],
            "content": message
        }]
    }

def formDelegateResponse(session_attributes, slots, intent, message = None):
    
    response = {
        "sessionState": {
                "sessionAttributes": session_attributes,
                "dialogAction": {
                    "type": DIALOG_ACTIONS_TYPES["DELEGATE"],
                },
                "intent": {
                    "name": intent,
                    "slots": slots,
                    "state": INTENT_STATES["IN_PROGRESS"]
                }
            }
    }
    
    if message is not None:
        response["messages"] = [{
            "contentType": MESSAGES_CONTENT_TYPES["PLAIN_TEXT"],
            "content": message
        }]

    return response


def formElicitIntentResponse(intentName, messageText):
    return {
        "sessionState": {
            "dialogAction": {
                "type": DIALOG_ACTIONS_TYPES["ELICIT_INTENT"],
                "intentName": intentName,
            }
        },
        "messages": [{
            "contentType": MESSAGES_CONTENT_TYPES["PLAIN_TEXT"],
            "content": messageText
        }]
    }

def formElicitSlotResponse(session_attributes, slot_to_elicit, slots, intent):
    return {
		"sessionState": {
            "sessionAttributes": session_attributes,
			"dialogAction": {
				"type": DIALOG_ACTIONS_TYPES["ELICIT_SLOT"],
				"slotToElicit": slot_to_elicit,

			},
			"intent": {
                "name": intent,
                "slots": slots,
                "state": INTENT_STATES["IN_PROGRESS"]
            },
		}
    }
