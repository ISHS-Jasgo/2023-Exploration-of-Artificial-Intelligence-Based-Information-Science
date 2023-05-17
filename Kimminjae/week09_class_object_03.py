class Pokemon:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def say(self):
        print(f"Hello, I'm {self.name}")


class Pikachu(Pokemon):
    pass


class Squirtle(Pokemon):
    pass


class Charizard(Pokemon):
    pass


class Digimon:
    pass


if __name__ == "__main__":
    pikachu = Pikachu("pikachu", 1, 35)
    pikachu.say()
    squirtle = Squirtle("squirtle", 1, 44)
    charizard = Charizard("charizard", 36, 78)
    charizard.say()

    print(squirtle.name)
    print(squirtle)

    print(issubclass(Squirtle, Pokemon))
    print(issubclass(Digimon, Pokemon))

    print(pikachu.name, pikachu.level, pikachu.hp)
    print(pikachu)

    print(charizard.name, charizard.level, charizard.hp)
    print(charizard)
