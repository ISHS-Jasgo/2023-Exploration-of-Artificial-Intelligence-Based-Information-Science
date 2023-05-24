class PrettyMixin:
    def dump(self):
        # print(f'{self.name}')
        import pprint
        pprint.pprint(vars(self))


class Pokemon(PrettyMixin):
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp


if __name__ == '__main__':
    p1 = Pokemon("pikachu", 1, 35)
    p1.dump()
