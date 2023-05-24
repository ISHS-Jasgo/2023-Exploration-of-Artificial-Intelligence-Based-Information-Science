class Pokemon:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def say(self):
        print(f"Hello, I'm {self.name}")

    def attack(self):
        print(f"{self.name} launched an area attack")

    def attack_target(self, target):
        print(f"{self.name} launched an area attack to {target.name}")


class Pikachu(Pokemon):
    def attack(self):
        print(f"{self.name} launched a thunderbolt")

    def attack_target(self, target):
        print(f"{self.name} launched a thunderbolt to {target.name}")


class Squirtle(Pokemon):
    def attack(self):
        print(f"{self.name} launched a water gun")


class Charizard(Pokemon):

    def attack(self):
        super().attack()
        print(f"{self.name} launched a fireball")


class Digimon:
    pass


if __name__ == "__main__":
    pikachu = Pikachu("pikachu", 1, 35)
    pikachu.say()
    squirtle = Squirtle("squirtle", 1, 44)
    charizard = Charizard("charizard", 36, 78)
    charizard.say()

    pikachu.attack_target(squirtle)
    pikachu.attack()
    squirtle.attack()
    charizard.attack()

    print(squirtle.name)
    print(squirtle)

    print(issubclass(Squirtle, Pokemon))
    print(issubclass(Digimon, Pokemon))

    print(pikachu.name, pikachu.level, pikachu.hp)
    print(pikachu)

    print(charizard.name, charizard.level, charizard.hp)
    print(charizard)
