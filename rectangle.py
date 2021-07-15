import math
class Rectangle:
    def __init__(self, name='', a='', b='', c='', d=''):
        self._name = name
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    @property
    def name(self):
        return self._name

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def d(self):
        return self._d

    def __str__(self):
        return f"Rectangle {self._name} with sides:\t{self._a};\t{self._b};\t{self._c};\t{self._d}; "

    def __eq__(self, other):
        return self._a == other._a and self._b == other._b and self._c == other._c and self._d == other._d

    def __ne__(self, other):
        return self._a != other._a or self._b != other._b or self._c != other._c or self._d != other._d

    def __gt__(self, other):
        return self.perimeter() > other.perimeter()

    def __lt__(self, other):
        return self.perimeter() < other.perimeter()

    def square(self):
        return self._a == self._b == self._c == self._d

    def diagonal(self):
        return math.sqrt(self._a ** 2 + self._b ** 2)

    def perimeter(self):
        return (self._a + self._b) * 2

    def area(self):
        return self._a * self._b

l = []
def file_read():
    try:
        with open('Data.txt', 'r') as f:
            for line in f:
                n, a, b, c, d = line.split()
                l.append(Rectangle(n, float(a), float(b), float(c), float(d)))
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print('Wrong value')

def info():
    for elem in l:
        print(elem)

def square():
    for elem in l:
        if elem.square():
            print(f'Rectangle {elem.name} is a square')
            diag = elem.diagonal()
            print("Diagonal of square =", diag)
        else:
            continue

def equal():
    name1, name2 = map(int, input("Enter names of rectangles which you want to equate: ").split())
    if l[name1 - 1] == l[name2 - 1]:
        print(f"Rectangle {name1} is equal to rectangle {name2}")
    if l[name1 - 1] != l[name2 - 1]:
        print(f"Rectangle {name1} isn't equal to rectangle {name2}")

def comparison():
    name1, name2 = map(int, input("Enter names of rectangles which you want to equate: ").split())
    if l[name1 - 1] > l[name2 - 1]:
        print(f"Perimeter of rectangle {name1} is bigger than rectangle {name2}")
    if l[name1 - 1] < l[name2 - 1]:
        print(f"Perimeter of rectangle {name1} is smaller than rectangle {name2}")

def sorting():
    for elem in sorted(l, key=lambda q: q.area()):
        print(f'Rectangle {elem.name}\tarea = {elem.area()}')

def min_per():
    minimal = min(l, key=lambda h: h.perimeter())
    print(minimal)

def menu():
    while True:
        n = int(input("Show information - 1 \nCheck for equality - 2 \nComparison of perimeters - 3 \nMin perimeter - 4 \nSort by area - 5 \nSquare - 6\nEnter number:"))
        if n == 1:
            print("~Information~")
            file_read()
            info()
            print('\n')
        elif n == 2:
            print("~EQUAL~")
            equal()
            print('\n')
        elif n == 3:
            print("~COMPARISON~")
            comparison()
            print('\n')
        elif n == 4:
            print("~MIN PERIMETER~")
            min_per()
            print('\n')
        elif n == 5:
            print("~SORT~")
            sorting()
            print('\n')
        elif n == 6:
            print("~SQUARE~")
            square()
            print('\n')
        else:
            print("BYE!")
        v = int(input("If you want continue enter - 1 \texit - 2\nEnter number:"))
        if v == 1:
            continue
        else:
            print("BYE!")
            break

menu()
