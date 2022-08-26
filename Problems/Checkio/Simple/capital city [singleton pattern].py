# https://py.checkio.org/ru/mission/capital-city/
# Ваша задача - реализовать класс Capital(), для которого можно было бы создать
# только один объект с глобальным доступом к нему, а все последующие создаваемые
# экземпляры этого класса не перезаписывали бы первый (и единственный) экземпляр.
# Также вам необходимо реализовать метод name() который возвращает название столицы.


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class Capital:
    def __init__(self, city_name):
        self.city_name = city_name

    def name(self):
        return self.city_name


def test0():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Morocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    test0()
