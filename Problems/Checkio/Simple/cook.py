# https://py.checkio.org/ru/mission/3-chefs/
# задача по ООП


class AbstractCook:
    def __init__(self, drink=None, food=None):
        self.drink_name = drink
        self.food_name = food
        self.food_list = []
        self.drink_list = []

    def add_food(self, food_amount, food_cost):
        self.food_list.append((food_amount, food_cost))

    def add_drink(self, drink_amount, drink_cost):
        self.drink_list.append((drink_amount, drink_cost))

    def total(self):
        t_f_cost = sum([item[0] * item[1] for item in self.food_list])
        t_d_cost = sum([item[0] * item[1] for item in self.drink_list])
        t_cost = t_f_cost + t_d_cost
        return f'{self.food_name}: {t_f_cost}, {self.drink_name}: {t_d_cost}, Total: {t_cost}'


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__(drink='Tea', food='Sushi')


class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__(drink='Compote', food='Dumplings')


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__(drink='Juice', food='Pizza')


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
