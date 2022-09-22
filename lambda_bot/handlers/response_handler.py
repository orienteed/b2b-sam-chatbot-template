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


def formTerminalResponse(session_attributes, slots):
    return {
        "sessionState": {
            "sessionAttributes": session_attributes,
			"dialogAction": {
				"type": "Close"
			},
            "intent": {
                "name": "createTicketIntent",
                "state": "Fulfilled",
                "slots": slots
            }
        },
        "messages": [{
            "contentType": "PlainText",
            "content": "Thank you for using our service. Have a nice day!"
        }]
    },

def formDelegateResponse(session_attributes, slots, intent):
    return {
        "sessionState": {
            "sessionAttributes": session_attributes,
            "dialogAction": {
                "type": "Delegate",
            },
            "intent": {
                "name": intent,
                "slots": slots,
                "state": "InProgress"
            },
        }
    }


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
