class Parent:
    def __init__ (self,name: str,age: int):
        self.name = name
        self.age = age
        self.children = [] #список детей

    def infoParent(self):
        """Сообщает информацию о родители"""

        print(f'Меня зовут {self.name}, мне {self.age} лет')

    def add_child(self, child):
        """Добавляет ребенка в список детей, если разница в возрасте
        более 16 лет"""

        if self.age - child.age >= 16:
            self.children.append(child)
            print(f"Ребенок {child.name} добавлен к {self.name}.")
        else:
            print(f'Ребенок {child.name} не добавлен к {self.name}, разница в возрасте слишком мала. ')

    def feed(self, child):
        """Кормит ребёнка, изменяя его состояние голода"""
        if child in self.children:
            child.hungry = False
            print(f'{self.name} покормил(а) {child.name}.')
        else:
            print(f'{child.name} не является ребенком {self.name}.')

    def calm(self, child):
        """Успокаивает ребенка, изменяя его состояние спокойствия"""
        if child in self.children:
            child.calm = True
            print(f'{self.name} успокоил(а) {child.name}')
        else:
            print(f'{child.name} не является ребенком {self.name}')

    def list_children(self):
        """Выводит информацию обо всех детях родителя"""
        if self.children:
            print(f'У {self.name} есть следующие дети:')
            for child in self.children:
                print(f'-{child}')
        else:
            print(f'У {self.name} нет детей.')


class Child:
    def __init__ (self, name: str, age: int):
        self.name = name
        self.age = age
        self.calm = False # Ребенок по умолчанию не спокоен
        self.hungry = True # Ребенок по умолчанию голоден


    def get_status(self):
        """Сообщает текущее состояние ребенка"""
        calm_status = "спокоен" if self.calm else "не спокоен"
        hungry_status = "сыт" if not self.hungry else "голоден"
        print(f'Ребенок {self.name} {calm_status} и {hungry_status}')

    def __str__(self):
        """ Представление объекта ребенок в виде строки"""
        return f"Ребёнок {self.name}, {self.age} лет"


parent = Parent("Мапа", 40)
child1 = Child("Сыван", 30)
child2 = Child("Сыту", 10)
child3 = Child("Сытри", 3)

#  Добавление детей к родителю

for child in [child1, child2, child3]:
    parent.add_child(child)

parent.infoParent()
parent.list_children()

# Родитель кормит и успокаивает детей

for child in parent.children:
    parent.feed(child)
    parent.calm(child)
    child.get_status()