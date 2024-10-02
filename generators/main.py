
def mygenerators(n):
    result = 1
    for x in range(n):
        yield x ** 3

values = mygenerators(100)

for x in values:
    print(x)

def inifinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values1 = inifinite_sequence()

# print(next(values1))
# print(next(values1))
# print(next(values1))
# print(next(values1))
# print(next(values1))
# print(next(values1))
