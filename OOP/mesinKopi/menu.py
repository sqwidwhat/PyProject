class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 1.5, {"water": 50, "coffee": 18}),
            MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24}),
            MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24}),
        ]

    def get_items(self):
        items = ""
        for item in self.menu:
            items += item.name + "/"
        return items[:-1]

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None