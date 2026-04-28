class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def whichAnimalIsMakingSound(self):
        print(f"{self.name} is making {self.sound} sound.")


class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.name = name
        self.sound = sound

class Dog(Animal):
    def __init__(self, name, sound, pet=True):
        super().__init__(name, sound)
        self.name = name
        self.sound = sound
        self.pet = pet

    def whichAnimalIsMakingSound(self):
        print(f"{self.name} is making {self.sound} sound and it is {'a' if self.pet else 'not a'} pet animal.")

cat = Cat('Bunty', 'meow')
cat.whichAnimalIsMakingSound()

rocky = Dog('Rocky', 'Bhao', True)
rocky.whichAnimalIsMakingSound()

scooby = Dog('Scooby', 'Bhao', False)
scooby.whichAnimalIsMakingSound()