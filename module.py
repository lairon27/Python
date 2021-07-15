#Дано послідовність слів, відокремлених пропусками. Утворити нову стрічку зі слів, які одинаково читаються зліва направо і справа наліво.
s = input("Enter words:").split()
s_new = ''
for words in s:
    if words == words[::-1]:
        s_new += words + ' '
print(s_new)
