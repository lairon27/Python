import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('tips.csv')

def menu():
    while True:
        n = int(input(
            "Хто дає більші чайові: курці чи ні- 1 \nЧайові по днях тижня - 2 \nЧайові в залежності від часу( обід, вечеря…) - 3 \nГістограма рахунків (список, 100, 8) - 4 \nСкаттер рахунок-чайові - 5\nЗалежність чайових від статі клієнта - 6\nInput:"))
        if n == 1:
            print("~Хто дає більші чайові: курці чи ні~")
            print(f"Більші чайові залишають\n {df.groupby(['smoker']).agg({'tip':sum})}")
            print('\n')
        elif n == 2:
            print("~Чайові по днях тижня~")
            print(df.groupby(['day']).agg({'tip':sum}))
            print('\n')
        elif n == 3:
            print("~Чайові в залежності від часу( обід, вечеря…)~")
            print(df.groupby(['time']).agg({'tip':sum}))
            print('\n')
        elif n == 4:
            print("~Гістограма рахунків (список, 100, 8)~")
            df['total_bill'].plot(kind='hist', subplots=True, figsize=(8, 8))
            plt.title("Total bill")
            plt.ylabel('')
            plt.show()
            print('\n')
        elif n == 5:
            print("~Скаттер рахунок-чайові~")
            x = df['total_bill']
            y = df['tip']
            plt.scatter(x, y)
            plt.show()
        elif n == 6:
            print("~Залежність чайових від статі клієнта~")
            print(df.groupby(['sex']).agg({'tip': sum}))
        else:
            print("BYE!")
        v = int(input("If you want continue enter - 1 \texit - 2\nEnter number:"))
        print('\n')
        if v == 1:
            continue
        else:
            print("BYE!")
            break
menu()