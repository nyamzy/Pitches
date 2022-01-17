class Jokes:
    '''
    Jokes class to define the objects
    '''
    def __init__(self, name, title, joke):
        self.name = name
        self.title = title
        self.joke = joke


class Product:
    '''
    Product class to define the objects
    '''
    def __init__(self, name, title, product):
        self.name = name
        self.title = title
        self.product = product


class Vows:
    '''
    Vows class to define the objects
    '''
    def __init__(self, name, title, vow):
        self.name = name
        self.title = title
        self.vow = vow


class Comment:

    all_comments = []

    def __init__(self, title, comment):
        self.title = title
        self.comment = comment

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()