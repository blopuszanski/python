'Training with the objects'

class sea_pet:
    def __init__(self, specie, size, swim):
        self.specie = specie
        self.size = size
        self.swim = swim

    def swim(self):
        print(f'Here {self.specie} Plum and I swim.')

class shark(sea_pet):
    def __init__(self, name):
        super().__init__('shark', 'M', True)
        self.teeth = True
        self.swim = True
        self.name = name

    def hunt(self):
        print(f'Here {self.name} I am going to hunt.')

class penguin(sea_pet):
    def __init__(self,name):
        super().__init__('penguin', 'S', True)
        self.fly = False
        self.name = name

    def sliding(self):
        print(f'Here {self.name} I am sliding. Am I flying {self.fly}? ')

if __name__ == '__main__':
    shark1 = shark('Richard')
    shark1.hunt()
    shark1.teeth = False
    print(shark1.teeth)

    penguin_name = input('Please give me a name of your penguin: ')
    penguin1 = penguin(penguin_name)
    penguin1.fly = input('Does penguin fly? True/False ')
    penguin1.sliding()