class BeeAndElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def Fly(self):
        return self.bee_part >= self.elephant_part

    def Trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def Eat(self, meal, value):
        if meal == "nectar":
            self.elephant_part -= value
            self.bee_part += value
        elif meal == "grass":
            self.elephant_part += value
            self.bee_part -= value
        
        self.elephant_part = max(0, min(100, self.elephant_part))
        self.bee_part = max(0, min(100, self.bee_part))

bee_part = 40
elephant_part = 60
instance = BeeAndElephant(bee_part, elephant_part)

print(f"Can it fly? {instance.Fly()}")
print(f"Trumpet sound: {instance.Trumpet()}")
print(f"Bee part: {instance.bee_part}, Elephant part: {instance.elephant_part}")