# https://py.checkio.org/ru/mission/text-editor/
class Text:
    def __init__(self):
        self.text = ''
        self.font = None

    def write(self, new_text):
        self.text += new_text

    def set_font(self, font_name):
        self.font = font_name

    def show(self):
        return f'[{self.font}]{self.text}[{self.font}]' if self.font else self.text

    def restore(self, old_text):
        self.text, self.font = old_text


class SavedText:
    def __init__(self):
        self.versions = dict()
        self.version = 0

    def save_text(self, text):
        self.versions[self.version] = (text.text, text.font)
        self.version += 1

    def get_version(self, number):
        return self.versions[number]


def test0():
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")


def test1():
    pass


def test2():
    pass


if __name__ == '__main__':
    test0()
    test1()
    test2()
