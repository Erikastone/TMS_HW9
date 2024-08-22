class Pizza:
    def __init__(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza(size=None, cheese=None, pepperoni=None, mushrooms=None, onions=None, bacon=None)

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def add_pepperoni(self, pepperoni):
        self.pizza.pepperoni = pepperoni
        return self

    def add_mushrooms(self, mushrooms):
        self.pizza.mushrooms = mushrooms
        return self

    def add_onions(self, onions):
        self.pizza.onions = onions
        return self

    def add_bacon(self, bacon):
        self.pizza.bacon = bacon
        return self

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return self.builder.pizza

builder = PizzaBuilder()
pizza_director = PizzaDirector(builder)

my_pizza = pizza_director.make_pizza()
builder.add_cheese("mozzarella").add_pepperoni(True).add_mushrooms(True).add_onions(False).add_bacon(True).set_size(23)

print(f"My delicious pizza: {my_pizza.__dict__}")