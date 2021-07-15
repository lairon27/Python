#Ввести інформацію  про  результати  іспиту n студентів  (прізвище  і  оцінка  у  100-бальній системі, наприклад, Васьків,76)і записати у словник.
# Замінити оцінку у 100-бальній  системі для кожного  студента  відповідною оцінкою у  5-ти  бальній.
# Вивести прізвища тих, хто одержав 4 або 5за іспит.
n = int(input('Enter amount of students:'))
students = {}
def student(students,n):
    for i in range(n):
        surname, mark = input().split()
        students[surname] = int(mark)
    print(students)

def marks(students):
    for k,v in students.items():
        if v <= 100 and v >= 90:
           students[k] = '5'
        if v < 90 and v > 70:
            students[k] = '4'
        if v < 70 and v > 50:
            students[k] = '3'
    print(students)

def four_or_five(students):
    for k,v in students.items():
        if v[0] == '4' or v[0] == '5':
            print(k)

student(students, n)
marks(students)
four_or_five(students)