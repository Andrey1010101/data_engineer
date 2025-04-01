


class Numen:
    hands: int
    foots: int
    head: int
    eyes: int
    age: int
    sex: int
    name: str

    def __init__(self, v_name):
        self.hands = 2
        self.foots = 2
        self.head = 1
        self.eyes = 2
        self.age = 30
        self.sex = 1
        self.name = v_name

    def mobilization(self):
        if self.sex == 1:
            self.hands = self.hands / 2
            self.foots = self.foots / 2
            self.eyes = self.eyes / 2

    def see_info(self):
        print(f'heads = {str(self.hands)}')
        print(f'foots = {str(self.foots)}')
        print(f'head = {str(self.head)}')
        print(f'eyes = {str(self.eyes)}')
        print(f'age = {str(self.age)}')
        print(f'sex = {str(self.sex)}')
        print(f'name = {str(self.name)}')

o_petya = Numen("Petya")
o_petya.see_info()

o_vasya = Numen("Vasya")
o_vasya.mobilization()
o_vasya.see_info()