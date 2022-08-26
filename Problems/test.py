﻿# noinspection SpellCheckingInspection
VOWELS = "AEIOUaeiou"


class Chat:
    def __init__(self):
        self.history = []

    def connect_human(self, human):
        human.chat = self

    def connect_robot(self, robot):
        robot.chat = self

    def show_human_dialogue(self):
        return ''.join([f'{prefix} {msg}\n' for prefix, msg, _ in self.history])[:-1]

    def show_robot_dialogue(self):
        return ''.join([f'{prefix} {code_msg}\n' for prefix, _, code_msg in self.history])[:-1]


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
