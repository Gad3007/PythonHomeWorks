class Animal:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__} имя {self.name}"


class Bird(Animal):
        def __init__(self, name: str, wingspan: int):
            super().__init__(name)
            self.wingspan = wingspan

        def wing_lenght(self, wingspan):
            return wingspan/2

        def __str__(self):
            return f"{super().__str__()} размах крыльев {self.wingspan} длина крыла {self.wing_lenght(self.wingspan)}"


class Fish(Animal):
    def __init__(self, name: str, max_depth: int):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth <= 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"

    def __str__(self):
        return f"{super().__str__()} {self.depth()}"


class Mammal(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight >= 200:
            return "Гигант"
        else:
            return "Обычный"

    def __str__(self):
        return f"{super().__str__()} {self.category()}"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:

        animal_classes = {
            'Fish': Fish,
            'Bird': Bird,
            'Mammal': Mammal
        }

        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


bird = AnimalFactory.create_animal('Bird', 'Воробей', 2)
fish = AnimalFactory.create_animal('Fish', 'Акула', 40)
fish1 = AnimalFactory.create_animal('Fish', 'Удильщик', 500)
mammal = AnimalFactory.create_animal('Mammal', 'Червяк', 0.2)
mammal1 = AnimalFactory.create_animal('Mammal', 'Слон', 200)

print(bird)
print(fish)
print(fish1)
print(mammal)
print(mammal1)
