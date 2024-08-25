def read_two_arrays():
    import random

    a = []
    b = []

    for i in range(20):
        a.append(random.randint(15, 30))
        b.append(random.randint(1, 10))

    print(a)
    print(b)

    c = []
    d = []
    e = []

    for x, j in zip(a, b):
        c.append(x-j)
        d.append(x+j)
        e.append(x*j)

    print(c)
    print(d)
    print(e)

read_two_arrays()