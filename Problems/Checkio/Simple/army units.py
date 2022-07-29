# https://py.checkio.org/ru/mission/army-units/
# задачка на ООП

class Army:
    def __init__(self, etnonim = None, soldier_names = None):
        self.etnonim = etnonim
        self.swordsman_name  = soldier_names[0] if soldier_names is not None else None
        self.lancer_name  = soldier_names[1] if soldier_names is not None else None
        self.archer_name = soldier_names[2] if soldier_names is not None else None

    def train_swordsman(self, name):
        return Swordsman(name, self.etnonim, soldier_name = self.swordsman_name)

    def train_lancer(self, name):
        return Lancer(name, self.etnonim, soldier_name = self.lancer_name)

    def train_archer(self, name):
        return Archer(name, self.etnonim, soldier_name = self.archer_name)


class Swordsman:
    def __init__(self, name, army_name, soldier_name):
        self.name = name
        self.army_name = army_name
        self.soldier_name = soldier_name

    def introduce(self):
        return self.soldier_name + ' ' + self.name + ', ' + self.army_name + ' swordsman'


class Lancer:
    def __init__(self, name, army_name, soldier_name):
        self.name = name
        self.army_name = army_name
        self.soldier_name = soldier_name

    def introduce(self):
        return self.soldier_name + ' ' + self.name + ', ' + self.army_name + ' lancer'


class Archer:
    def __init__(self, name, army_name, soldier_name):
        self.name = name
        self.army_name = army_name
        self.soldier_name = soldier_name

    def introduce(self):
        return self.soldier_name + ' ' + self.name + ', ' + self.army_name + ' archer'


class AsianArmy(Army):
    def __init__(self):
        super().__init__(etnonim='Asian', soldier_names=['Samurai', 'Ronin', 'Shinobi'])



class EuropeanArmy(Army):
    def __init__(self):
        super().__init__(etnonim='European', soldier_names=['Knight', 'Raubritter', 'Ranger'])


if __name__ == '__main__':
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"
    
    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"


