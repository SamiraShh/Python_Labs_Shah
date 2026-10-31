print("Задание 2, Вариант 8\n")

s = input("Введите строку: ")
words = s.rstrip(".").split()
count = len(words)

print(f"Количество слов в строке: {count}")