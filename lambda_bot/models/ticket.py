from .article import Article

class Ticket():
    def __init__(self, ticket_type, title, article):
        self.title: str = title
        self.ticket_type: str = ticket_type
        self.article: Article = article

    def set_title(self, title):
        self.title = title

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

    def set_article(self, article):
        self.article = article

    def get_title(self):
        return self.title

    def get_ticket_type(self):
        return self.ticket_type

    def get_article(self):
        return self.article

    def to_dict(self):
        return {
            'title': self.title,
            'group': self.ticket_type,
            'article': self.article.to_dict()
        }
