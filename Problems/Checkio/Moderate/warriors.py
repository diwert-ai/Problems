# https://py.checkio.org/ru/mission/the-warlords/
# цикл задач по ООП

from collections import deque


class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.warrior_behind = None
        self.max_health = health

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other, straight_mode=False):
        other.loss(self.attack)
        if type(self.warrior_behind) is Healer and not straight_mode:
            self.warrior_behind.heal(self)

    def loss(self, attack):
        self.health -= attack

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.max_health += weapon.health
        self.attack += weapon.attack


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def loss(self, attack):
        self.health -= max(0, attack - self.defense)

    def equip_weapon(self, weapon):
        super().equip_weapon(weapon)
        self.defense += weapon.defense


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 50

    def hit(self, other, straight_mode=False):
        other_health_before_hit = other.health
        super().hit(other, straight_mode)
        damage = other_health_before_hit - other.health
        self.health += self.vampirism * damage // 100

    def equip_weapon(self, weapon):
        super().equip_weapon(weapon)
        self.vampirism += weapon.vampirism


class Lancer(Warrior):
    def __init__(self):
        super().__init__(attack=6)

    def hit(self, other, straight_mode=False):
        super().hit(other, straight_mode)
        if other.warrior_behind is not None and not straight_mode:
            other.warrior_behind.loss(self.attack // 2)


class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)
        self.heal_power = 2

    def hit(self, other, straight_mode=False):
        pass

    def heal(self, other):
        other.health = min(other.max_health, other.health+self.heal_power)

    def equip_weapon(self, weapon):
        super().equip_weapon(weapon)
        self.heal_power += weapon.heal_power


class Warlord(Warrior):
    def __init__(self):
        super().__init__(attack=4, health=100)
        self.defense = 2

    def loss(self, attack):
        self.health -= max(0, attack - self.defense)

    def equip_weapon(self, weapon):
        super().equip_weapon(weapon)
        self.defense += weapon.defense


class Army:
    def __init__(self):
        self.units = deque()
        self.warlord_in = False

    def add_units(self, unit_class, num_units):
        last_unit = self.last_unit
        if unit_class is Warlord and not self.warlord_in:
            self.units.append(Warlord())
            self.warlord_in = True
            if last_unit is not None:
                last_unit.warrior_behind = self.last_unit
            return
        for i in range(num_units):
            unit = unit_class()
            if last_unit is not None:
                last_unit.warrior_behind = unit
            self.units.append(unit)
            last_unit = unit

    @property
    def is_alive(self):
        return any([unit.is_alive for unit in self.units])

    @property
    def last_unit(self):
        return self.units[len(self.units)-1] if len(self.units) > 0 else None

    def print_army(self):
        for unit in self.units:
            print(f'{type(unit).__name__} h={unit.health} a={unit.attack}', end=' ')
            unit_class = type(unit)
            if unit_class in [Defender, Warlord]:
                print(f'd={unit.defense} ', end=' ')
            if unit_class is Vampire:
                print(f'v={unit.vampirism} ', end=' ')
            if unit_class is Healer:
                print(f'hp={unit.heal_power} ', end=' ')
            print('')

    def move_units(self):
        if not self.warlord_in:
            return

        others = []
        healers = []
        lancers = []
        warlord = None

        for unit in self.units:
            if not unit.is_alive:
                continue
            unit_class = type(unit)
            if unit_class is Lancer:
                lancers.append(unit)
            elif unit_class is Warlord:
                warlord = unit
            elif unit_class is not Healer:
                others.append(unit)
            else:
                healers.append(unit)

        if warlord is None:
            self.warlord_in = False
            return

        self.units.clear()
        if lancers:
            self.units = deque([lancers[0]]) + deque(healers)
            if len(lancers) > 0:
                self.units += deque(lancers[1:]) + deque(others)
            else:
                self.units += deque(others)
        else:
            if others:
                self.units = deque([others[0]]) + deque(healers)
                if len(others) > 0:
                    self.units += deque(others[1:])
            else:
                self.units = deque(healers)
        self.units.append(warlord)

        for i in range(1, len(self.units)):
            self.units[i-1].warrior_behind = self.units[i]


def fight(unit_1, unit_2, straight_mode=False):
    while True:
        unit_1.hit(unit_2, straight_mode)
        if not unit_2.is_alive:
            break
        unit_2.hit(unit_1, straight_mode)
        if not unit_1.is_alive:
            break
    return unit_1.is_alive


class Battle:
    def __init__(self):
        pass

    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            unit_1 = army_1.units.popleft()
            unit_2 = army_2.units.popleft()
            result = fight(unit_1, unit_2)
            if result:
                army_2.move_units()
                army_1.units.appendleft(unit_1)
            else:
                army_1.move_units()
                army_2.units.appendleft(unit_2)
        return army_1.is_alive

    @staticmethod
    def straight_fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            alive_units_1 = [unit for unit in army_1.units if unit.is_alive]
            alive_units_2 = [unit for unit in army_2.units if unit.is_alive]
            number_of_duels = min(len(alive_units_1), len(alive_units_2))
            for duel in range(number_of_duels):
                unit_1 = alive_units_1[duel]
                unit_2 = alive_units_2[duel]
                if fight(unit_1, unit_2, straight_mode=True):
                    army_2.move_units()
                else:
                    army_1.move_units()
                print(f'after duel {duel}')
                print('army_1:')
                army_1.print_army()
                print('army_2:')
                army_2.print_army()

        return army_1.is_alive


class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__(health=5, attack=2)


class Shield(Weapon):
    def __init__(self):
        super().__init__(health=20, attack=-1, defense=2)


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(health=-15, attack=5, defense=-2, vampirism=10)


class Katana(Weapon):
    def __init__(self):
        super().__init__(health=-20, attack=6, defense=-5, vampirism=50)


class MagicWand(Weapon):
    def __init__(self):
        super().__init__(health=30, attack=3, heal_power=3)


class Rookie(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=1)


if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 2)
    army_1.add_units(Lancer, 3)
    army_1.add_units(Defender, 1)
    army_1.add_units(Warlord, 1)
    army_2.add_units(Warlord, 5)
    army_2.add_units(Vampire, 1)
    army_2.add_units(Rookie, 1)
    army_2.add_units(Knight, 1)
    army_1.units[0].equip_weapon(Sword())
    army_2.units[0].equip_weapon(Shield())
    army_1.move_units()
    army_2.move_units()
    print('army_1: ')
    army_1.print_army()
    print('army_2: ')
    army_2.print_army()
    battle = Battle()
    assert battle.straight_fight(army_1, army_2) is False
