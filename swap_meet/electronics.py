from .item import Item
class Electronics (Item):
    def __init__ (self, condition = 0, category = "Electronics"):
        self.category = category
        self.condition = condition

    def __str__ (self):
        return "The finest clothing you could wear."


    def __str__ (self):
        return "A gadget full of buttons and secrets."