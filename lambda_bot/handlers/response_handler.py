import json

def formElicitSlotWithTemplateResponse(session_attributes, slot_to_elicit, template, slots, intent):
    return {
		"sessionState": {
            "sessionAttributes": session_attributes,
			"dialogAction": {
				"type": "ElicitSlot",
				"slotToElicit": slot_to_elicit,

			},
			"intent": {
                "name": intent,
                "slots": slots,
                "state": "InProgress"
            },
		},

		"messages": [{
			"contentType": "CustomPayload",
			"content": json.dumps(template, separators=(',', ':'))
		}],
    }


def formTerminalResponse(session_attributes, slots, intent, message):
    return {
        "sessionState": {
			"dialogAction": {
				"type": "Close"
			},
            "intent": {
                "name": intent,
                "state": "Fulfilled"
            }
        },
        "messages": [{
            "contentType": "PlainText",
            "content": message
        }]
    }

def formDelegateResponse(session_attributes, slots, intent, message = None):
    
    response = {
        "sessionState": {
                "sessionAttributes": session_attributes,
                "dialogAction": {
                    "type": "Delegate"
                },
                "intent": {
                    "name": intent,
                    "slots": slots,
                    "state": "InProgress"
                }
            }
    }
    
    if message is not None:
        response["messages"] = [{
            "contentType": "PlainText",
            "content": message
        }]

    return response


def formElicitIntentResponse(intentName, messageText):
    return {
        "sessionState": {
            "dialogAction": {
                "type": "ElicitIntent",
                "intentName": intentName,
            }
        },
        "messages": [{
            "contentType": "PlainText",
            "content": messageText
        }]
    }

def formElicitSlotResponse(session_attributes, slot_to_elicit, slots, intent):
    return {
		"sessionState": {
            "sessionAttributes": session_attributes,
			"dialogAction": {
				"type": "ElicitSlot",
				"slotToElicit": slot_to_elicit,

			},
			"intent": {
                "name": intent,
                "slots": slots,
                "state": "InProgress"
            },
		}
    }
