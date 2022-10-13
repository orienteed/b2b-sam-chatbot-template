class Article():
    def __init__(self, subject, body, order_number=None):
        self.subject = subject
        self.body = body
        if order_number is not None:
            self.body = self.body + "\n\nThis ticket was created from the chatbot\n---------------------\n\nOrder number: {}".format(order_number)

        self.order_number = order_number

    def set_subject(self, subject):
        self.subject = subject

    def set_body(self, body):
        self.body = body

    def set_order_number(self, order_number):
        self.order_number = order_number

    def get_subject(self):
        return self.subject

    def get_body(self):
        return self.body

    def get_order_number(self):
        return self.order_number

    def to_dict(self):
        return {
            'subject': self.subject,
            'body': self.body
        }