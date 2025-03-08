# Builder Pattern
# Ever ordered a custom burger? You specify the bun, patty, toppings, and sauces, and voila! The Builder pattern lets you construct complex objects step by step, giving you complete control over the creation process.

class Burger:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def show_ingredients(self):
        print(f"Burger with {',' .join(self.ingredients)}")

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_cheese(self):
        self.burger.add_ingredient("cheese")
        return self

    def add_patty(self):
        self.burger.add_ingredient("patty")
        return self

    def add_tomato(self):
        self.burger.add_ingredient("tomato")
        return self

    def add_lettuce(self):
        self.burger.add_ingredient("lettuce")
        return self

    def build(self):
        return self.burger

builder = BurgerBuilder()
burger = builder.add_cheese().add_patty().add_tomato().add_lettuce().build()
burger.show_ingredients()