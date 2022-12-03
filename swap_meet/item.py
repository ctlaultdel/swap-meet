from swap_meet import conditions
import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id else uuid.uuid4().int
        self.condition = condition
    
    def __str__(self):
        # override Item stringify method and instead return this string when str(self) called        
        return f'An object of type Item with id {self.id}'
    
    def get_category(self):
        return type(self).__name__

    def condition_description(self):
        return conditions[self.condition]