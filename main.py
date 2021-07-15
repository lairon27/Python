class Worker:
    def __init__(self,name='',surname='',position='',year=0):
        self._surname=surname
        self._name = name
        self._position=position
        self._year=year

    @property
    def surname(self):
        return self._surname

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @property
    def year(self):
        return self._year

    def __str__(self):
        return f"Surname: {self._surname}\tName: {self._name}\tPosition: {self._position}\tYear: {self._year}"

l = []

def file_read():
    try:
        with open('text2.txt', 'r') as f:
            for line in f:
                l.append(Worker(line.split()[0], (line.split()[1]), (line.split()[2]),int(line.split()[3])))
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print('Wrong value')

def info():
    for elem in l:
        print(elem)

def experience():
    s = int(input("Enter expexience:"))
    z=0
    for elem in l:
        k = 2020 - elem.year
        if k > s:
            z+=1
            print(f'{elem.surname} {elem.name} has experience more than {s}')
    if z==0:
        print("no such experience")


file_read()
info()
experience()

