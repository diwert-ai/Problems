# https://py.checkio.org/ru/mission/dialogues/
# Ваша задача - реализовать способ связи между человеком Human(name) и
# роботом Robot(serial_number) с последующим выводом их переписки.
# Для этого вам необходимо создать класс для каждого из двоих собеседников
# и метод send() для отправки сообщений в чат, а также класс Chat как средство связи.
# Chat должен обладать следующими методами:
# connect_human() - подключает к чату человека;
# connect_robot() - подключает к чату робота;
# show_human_dialogue() - отображает диалог так, как его видит человек - обычным текстом;
# show_robot_dialogue() - отображает диалог так, как его видит робот - в виде набора нулей
# и единиц. Для простоты будем считать, что любая гласная буква ("aeiouAEIOU") в текстовом
# сообщении должна быть заменена на "0", а все остальные символы (согласные буквы, пробелы
# и специальные знаки, как ",", "!" и т.п.) на "1".

# noinspection SpellCheckingInspection
VOWELS = "AEIOUaeiou"


class Chat:
    def __init__(self):
        self.history = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, robot):
        robot.chat = self

    def show_human_dialogue(self):
        return '\n'.join([f'{prefix} {msg}' for prefix, msg, _ in self.history])

    def show_robot_dialogue(self):
        return '\n'.join([f'{prefix} {code_msg}' for prefix, _, code_msg in self.history])


class User:
    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, msg):
        if self.chat:
            self.chat.history.append([f'{self.name} said:', msg,
                                      ''.join(['0' if token in VOWELS else '1' for token in msg])])


class Human(User):
    def __init__(self, name):
        super().__init__(name=name)


class Robot(User):
    def __init__(self, name):
        super().__init__(name=name)


def test0():
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")


def test1():
    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    print(chat.show_human_dialogue())
    print(chat.show_robot_dialogue())


if __name__ == '__main__':
    test0()
    test1()
