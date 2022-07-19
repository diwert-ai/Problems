def rec(m, l=None):
    l = l or []
    yield l
    l.append(m)
    if m != 0:
        yield from rec(m-1, l)


for l in rec(10):
    print(l)

for l in rec(2):
    print(l)



