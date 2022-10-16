from pprint import pprint
class MyInt(int):
    def __add__(self, x):
        return super().__add__(x+1)

y = MyInt(int(input()))
y = y + 2
pprint(y)
