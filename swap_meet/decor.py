from .item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length
        self.area = width * length
        self.condition = condition

    def __str__(self):
        " "
        return (f'An object of type Decor with id {self.id}. '
                f'It takes up a {self.width} by {self.length} sized space.'
        )