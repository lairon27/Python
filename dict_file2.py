animals = {}
def animal(animals):
    try:
         f = open('animals.txt')
         for line in f:
             name, life, speed, population = line.split()
             animals[name] = [int(life), int(speed), int(population)]
         print(animals)
         f.close()
    except:
        print('Error file')

def faster(animals):
    for v in animals:
        m = max(animals.items(), key=lambda l: l[1][1])
    print('The faster animal is', m)

def populations(animals):
    for v in animals:
        q = min(animals.items(), key=lambda p: p[1][2])
    print('Animal with the smallest population', q)

animal(animals)
faster(animals)
populations(animals)
