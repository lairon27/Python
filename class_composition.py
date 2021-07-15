class Exhibit:
    def __init__(self, name = '', author = '', price = '', date = ''):
        self._name = name
        self._author = author
        self._price = price
        self._date = date
    def output(self):
        print(f"Name of exhibit: {self._name}\tAuthor: {self._author}\tPrice: {self._price}$\tDate of creation: {self._date}year")
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def price(self):
        return self._price

    @property
    def date(self):
        return self._date

class Picture(Exhibit):
    def __init__(self, name, author, price, date, genre = '', fashion = ''):
        super().__init__(name, author, price, date)
        self._genre = genre
        self._fashion = fashion
    def output(self):
        print(f"Name of exhibit: {self._name}\tAuthor: {self._author}\tPrice: {self._price}$\tDate of creation: {self._date}year\tGenre of picture: {self._genre}\tFashion: {self._fashion}")
    @property
    def fashion(self):
        return self._fashion
    @property
    def genre(self):
        return self._genre

class Sculpture(Exhibit):
    def __init__(self, name, author, price, date, material = ''):
        super().__init__(name, author, price, date)
        self._material = material
    def output(self):
        print(f"Name of exhibit: {self._name}\tAuthor: {self._author}\tPrice: {self._price}$\tDate of creation: {self._date}year\tMaterial: {self._material}")
    @property
    def material(self):
        return self._material

class Museum:
    def __init__(self, m_name=''):
        self._m_name = m_name
        self._museum = []


    def file_read(self):
        try:
            with open('Exhibits.txt', 'r') as f:
                for line in f:
                    if line[0] == 'p':
                        self._museum.append(Picture(line.split()[1], line.split()[2], float(line.split()[3]), int(line.split()[4]), line.split()[5], line.split()[6]))
                    elif line[0] == 's':
                        self._museum.append(Sculpture(line.split()[1], line.split()[2], float(line.split()[3]), int(line.split()[4]), line.split()[5]))
                    else:
                        self._museum.append(Exhibit(line.split()[1], line.split()[2], float(line.split()[3]), int(line.split()[4])))

        except FileNotFoundError:
            print("File not found")
        except ValueError:
            print('Wrong value')

    def output(self):
        print("Name of the museum Louvre", '\n')
        for elem in self._museum:
            elem.output()

    def search(self):
        while True:
            q = int(input("Find a picture by author - 1\nby genre - 2\nenter number:"))
            if q == 1:
                a = input("Surname of author: ")
                for elem in self._museum:
                    if isinstance(elem,Picture):
                        if a == elem._author:
                            print(a, "painted a picture", elem._name)
                        else:
                            continue
            elif q == 2:
                g = input("Genre of picture: ")
                for elem in self._museum:
                    if isinstance(elem,Picture):
                        if g == elem._genre:
                            print("Picture in genre", g , elem._name)
                        else:
                            continue
            b = int(input("If you want continue searching enter - 1 \texit - 2\nEnter number:"))
            if b == 1:
                continue
            else:
                print('The end')
                break

    def popular(self):
        r = {}
        for elem in self._museum:
            if isinstance(elem, Sculpture):
                r[elem._author] = elem._price
                m = max(r.items(), key=lambda l: l[1])
        print("Popular author is", m)

    def the_most_expensive(self):
        d = {}
        for elem in self._museum:
          d[elem._name] = elem._price
          m = max(d.items(), key=lambda l: l[1])
        print("The most expensive exhibit is", m)

    def add_exhibit(self):
        while True:
            e = input("If you want to add picture - p\tsculpture - s\tenter: ")
            if e == 'p':
                name = input("Enter name of picture:")
                author = input("Enter surname of author:")
                price = float(input("Enter price:"))
                date = int(input("Enter year of creation:"))
                genre = input("Enter genre of picture:")
                fashion = input("Fashionable or unfashionable:")
                exhibit = Picture(name, author, price, date, genre, fashion)
            elif e == 's':
                name = input("Enter name of sculpture:")
                author = input("Enter surname of author:")
                price = float(input("Enter price:"))
                date = int(input("Enter year of creation:"))
                material = input("Material of sculpture:")
                exhibit = Sculpture(name, author, price, date, material)
            else:
                name = input("Enter name of sculpture:")
                author = input("Enter surname of author:")
                price = float(input("Enter price:"))
                date = int(input("Enter year of creation:"))
                exhibit = Exhibit(name, author, price, date)
            self._museum.append(exhibit)
            self.output()
            b = int(input("If you want to continue enter - 1 \texit - 2\nEnter number:"))
            if b == 1:
                continue
            else:
                print('Complete')
                break

    def remove(self):
        i = 0
        name = input("Enter name of exhibit:")
        for elem in self._museum:
            if elem.name == name:
                del self._museum[i]
            i += 1
        self.output()

    def sorting(self):
        print('Select the sorting criteria:\n1 - by name\n2 - author\n3 - price'
              '\n4 - year of creation\n0 - exit')
        while True:
            sort_criteria = int(input('Enter:'))
            sorted_info = {1: sorted(self._museum, key=lambda a: a._name.split()[1]),
                           2: sorted(self._museum, key=lambda a: a._author.split()[2]),
                           3: sorted(self._museum,
                                     key=lambda a: a._price.split()[3]),
                           4: sorted(self._museum, key=lambda a: a._date)}

            if sort_criteria == 0:
                break
            elif sort_criteria in range(1, 6):
                for info in sorted_info[sort_criteria]:
                    print(info)
            else:
                print('No such option. Try again.')
                break

    def menu(self):
        while True:
            n = int(input("Show information about exhibits - 1 \nSearch picture - 2 \nPopular author - 3 \nThe most expensive exhibit - 4 \nAdd exhibit - 5 \nDelete exhibit - 6\nSort - 7\nEnter:"))
            if n == 1:
                print("~Information~")
                self.file_read()
                self.output()
                print('\n')
            elif n == 2:
                print("~SEARCHING~")
                self.search()
                print('\n')
            elif n == 3:
                print("~POPULAR~")
                self.popular()
            elif n == 4:
                print("~EXPENSIVE~")
                self.the_most_expensive()
                print('\n')
            elif n == 5:
                print("~ADD~")
                self.add_exhibit()
                print('\n')
            elif n == 6:
                print("~DELETE~")
                self.remove()
                print('\n')
            elif n==7:
                self.sorting()
                print('\n')
            else:
                print("BYE!")
            v = int(input("If you want continue enter - 1 \texit - 2\nEnter number:"))
            print('\n')
            if v == 1:
                continue
            else:
                print("BYE!")
                break
museum = Museum()
museum.menu()