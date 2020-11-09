#Дано послідовність слів, відокремлених комами. Надрукувати всі слова, у яких перша літера слова входить в нього ще раз.
s = input('Enter words:')
l = s.split(',')
chars = list(s)
for words in l:
    for chars in words:
        break
    if words.count(chars) > 1:
        print(words)

#Дано послідовність слів, відокремлених пропусками. Утворити нову стрічку зі слів, які починаються і закінчуються однією і тією ж буквою.
# Знайти найдовше слово утвореної стрічки.
# s = input('Enter string:').split()
# l = ''
# for words in s:
#     if words[0] == words[len(words)-1]:
#         l += words + ' '
# print(l)
# print(max(list(l.split()), key = len))

#Дано послідовність слів, відокремлених пропусками. Вивести ті слова, які одинаково читаються зліва направо і справа наліво.
# s = input("Enter words:").split()
# for words in s:
#     if words == words[::-1]:
#         print(words)

#Дано послідовність слів, відокремлених пропусками. У кожному слові перенести першу букву в кінець. Вивести змінену стрічку на екран.
# s = input("Enter words:").split()
# for words in s:
#     print(words[1:]+words[0])

