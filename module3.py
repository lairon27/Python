class People:
    def __init__(self, surname='', age=''):
        self._surname = surname
        self._age = age

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f"Surname: {self._surname}\tAge: {self._age}"

class Patient(People):
    def __init__(self, surname='', age='', disease=''):
        super().__init__(surname, age)
        self._disease = disease

    @property
    def disease(self):
        return self._disease

    def __str__(self):
        return f"Surname: {self._surname}\tAge: {self._age}\tDisease: {self._disease}"

class Doctor(People):
    def __init__(self, surname='', age='', specialty=''):
        super().__init__(surname, age)
        self._specialty = specialty

    @property
    def specialty(self):
        return self._specialty

    def __str__(self):
        return f"Surname: {self._surname}\tAge: {self._age}\tSpecialty: {self._specialty}"

l = []
def file_read():
    try:
        with open('text1.txt', 'r') as f:
            for line in f:
                if line[0] == 'p':
                    l.append(Patient(line.split()[1], int(line.split()[2]), line.split()[3]))
                elif line[0] == 'd':
                    l.append(Doctor(line.split()[1], int(line.split()[2]), line.split()[3]))
                else:
                    l.append(People(line.split()[1], int(line.split()[2])))
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print('Wrong value')
def info():
    for elem in l:
        print(elem)

def sort_by_surname():
    for elem in sorted(l, key=lambda j: j.surname):
        if isinstance(elem, Patient):
            print(f"Surname: {elem.surname}\tAge: {elem.age}\tDisease: {elem.disease}")
        elif isinstance(elem, Doctor):
            print(f"Surname: {elem.surname}\tAge: {elem.age}\tSpecialty: {elem._specialty}")

def oldest():
    oldest = max(l, key=lambda w: w.age)
    print(f"The oldest person is {oldest}")

def ill():
    s = input("Enter disease:")
    for elem in l:
        if isinstance(elem,Patient):
            if s == elem.disease:
                print(f'{elem.surname} sick {s}')
            else:
                continue

def surgeon():
    for elem in l:
        if isinstance(elem, Doctor):
            if elem.specialty == 'surgeon':
                if elem.age > 40:
                    print(f'Surgeon over 40 years old is {elem.surname}')
def menu():
    while True:
        n = int(input("Show information about people - 1 \nSort by surname - 2 \nSearch people with disease  - 3 \nSurgeon older than 40 - 4 \nOldest person - 5 \nEnter number:"))
        if n == 1:
            print("~Information~")
            file_read()
            info()
            print('\n')
        elif n == 2:
            print("~Sort~")
            sort_by_surname()
            print('\n')
        elif n == 3:
            print("Searching")
            ill()
            print('\n')
        elif n == 4:
            surgeon()
            print('\n')
        elif n == 5:
            oldest()
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