class Square:

    def __init__(self):    # special method __init__
        self.sides = 4


square = Square()
print(square.sides)


class Car:
    color = ""

    def __init__(self,color):
        self.color = color


car = Car("blue")    # Note: you should not pass self parameter explicitly, only color parameter

print(car.color)
