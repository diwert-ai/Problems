# https://py.checkio.org/ru/mission/microwave-ovens/
class MicrowaveBase:
    def __init__(self):
        self.mm = 0
        self.ss = 0


class Microwave1(MicrowaveBase):
    def get_time(self):
        return '_'+f'{self.mm:02}:{self.ss:02}'[1:]


class Microwave2(MicrowaveBase):
    def get_time(self):
        return f'{self.mm:02}:{self.ss:02}'[:-1]+'_'


class Microwave3(MicrowaveBase):
    def get_time(self):
        return f'{self.mm:02}:{self.ss:02}'


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave

    def set_time(self, time):
        self.microwave.mm, self.microwave.ss = map(int, time.split(':'))
        self.align_time()

    def add_time(self, time):
        dimension, value = time[-1], int(time[:-1])
        if dimension == 'm':
            self.microwave.mm += value
        else:
            self.microwave.ss += value
        self.align_time()

    def del_time(self, time):
        dimension, value = time[-1], int(time[:-1])
        if dimension == 'm':
            self.microwave.mm -= value
        else:
            self.microwave.ss -= value
        self.align_time()

    def align_time(self):
        total_seconds = self.microwave.ss + self.microwave.mm * 60

        if total_seconds > 5400:
            self.microwave.ss = 0
            self.microwave.mm = 90
            return

        if total_seconds < 0:
            self.microwave.ss = 0
            self.microwave.mm = 0
            return

        self.microwave.mm += self.microwave.ss // 60
        self.microwave.ss %= 60

    def show_time(self):
        return self.microwave.get_time()


def test0():
    a = f'test {2:02}'
    print(a)
    mw = Microwave3()
    rc = RemoteControl(mw)
    rc.set_time('89:61')
    print(rc.show_time())


def test1():
    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"


def test2():
    microwave_2 = Microwave2()
    rc_7 = RemoteControl(microwave_2)
    rc_7.set_time("15:00")
    rc_7.add_time("90s")
    rc_7.add_time("12m")
    print(rc_7.show_time())


if __name__ == '__main__':
    test0()
    test1()
    test2()
