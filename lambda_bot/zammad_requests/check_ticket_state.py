import requests
import json

def check_ticket_states(ticket_number, magento_token):

    headers = {'Authorization': 'Bearer ' + magento_token, 'csr-authorization': magento_token, 'Content-Type': 'application/json'}
    filters = {
        "status": [],
        "type": [],
    }
    params = {'search': 'number:' + str(ticket_number), 'filters': json.dumps(filters)}
    posible_states = get_ticket_states(headers)
    print(posible_states)

    url = f'https://chatbot-test.orienteed.com/csr/api/v1/tickets/search?search=number:{ticket_number}&filters=%7B%22status%22:%20%5B%5D,%20%22type%22:%20%5B%5D%7D'

    ticket_data = json.loads(requests.get(url, headers=headers).content.decode())
    print(ticket_data)

    print("LEN: " + str(len(ticket_data['tickets'])))

    if not "error" in ticket_data and len(ticket_data['tickets']) > 0:
        ticket_id = ticket_data['tickets'][0]
        state_id = ticket_data['assets']['Ticket'][str(ticket_id)]['state_id']

        print("state_id: {}".format(state_id))
        print("state_ name: {}".format(posible_states[str(state_id)]))

        return "The status of the ticket " + str(ticket_number) + " is: " + posible_states[str(state_id)]

    else:
        print("Ticket not found")
        return "Ticket not found"

def get_ticket_states(headers):

    states = json.loads(requests.get('https://chatbot-test.orienteed.com/csr/api/v1/ticket_states/', headers=headers).content.decode())
    print("states: ", format(states))

    return states

