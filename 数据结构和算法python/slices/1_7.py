from timeit import Timer



def popp():
    ls = list(range(1000))
    ls.pop()

t = Timer('popp()','from __main__ import popp')

print(t.timeit(number=1000))    