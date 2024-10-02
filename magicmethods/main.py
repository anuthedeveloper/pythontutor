
class MagicMethods:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MagicMethods(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        print(f"Calling the object {self}")

    

m1 = MagicMethods(20, 10)
m2 = MagicMethods(10, 40)
m3 = m1 + m2

print(m3.x)
print(m3.y)

m3()