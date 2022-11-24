import torch


def test0():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    t0 = torch.rand(128, 512, 512, 3)
    t0.to(device, dtype=torch.float)
    print(t0.size())
    print(torch.cuda.is_available())
    print(torch.cuda.current_device())
    print(torch.cuda.get_device_name(0))
    print('Allocated:', round(torch.cuda.memory_allocated(0) / 1024 ** 3, 1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_reserved(0) / 1024 ** 3, 1), 'GB')


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
