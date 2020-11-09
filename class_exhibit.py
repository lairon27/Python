class Exhibit:
    def __init__(self, name = '', author = '', price = '', date = '') :
        self.__name = name
        self.__author = author
        self.__price = price
        self.__date = date
    def output(self):
        print(f"Name of exhibit: {self.__name}\tAuthor: {self.__author}\tPrice: {self.__price}$\tDate of creation: {self.__date}year")
    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @property
    def date(self):
        return self.__date

l = []
def file_read():
    try:
        with open('Exhibits.txt', 'r') as f:
            for line in f:
                n, a, p, d = line.split()
                l.append(Exhibit(n, a, float(p), int(d)))
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print('Wrong value')

def file_output():
    for elem in l:
        elem.output()

def age():
    for elem in l:
        age = 2020 - elem.date
        print("Age of exhibit:", age, "years")

def cost():
    for elem in l:
        if elem.date < 1400:
            print("New price:", elem.price * 1.75, "$")
        elif elem.date < 1600:
            print("New price:", elem.price * 1.5, "$")
        elif elem.date < 1800:
            print("New price:", elem.price * 1.25, "$")
        elif elem.date < 2000:
            print("New price:", elem.price * 1.15, "$")
        else:
            print('The same price')

def menu():
    while True:
        n = int(input("Show information about exhibits - 1 \nHow old the exhibits are - 2 \nThe new price of exhibits - 3 \nEnter number:"))
        if n == 1:
            print("~Information~")
            file_read()
            file_output()
        elif n == 2:
            print("~Age~")
            age()
        elif n == 3:
            print("~New price~")
            cost()
        else:
            print("BYE!")
        v = int(input("If you want continue enter - 1 \texit - 2\nEnter number:"))
        if v == 1:
            continue
        else:
            print("BYE!")
            break

menu()