print("Задание 1.2, Вариант 8\n")

n = int(input("Введите положительное целое число: "))

s = 0
count = 0

while n > 0:
    digit = n % 10
    s += digit
    count += 1
    n = n // 10

print(f"Сумма цифр: {s}")
print(f"Количество цифр: {count}")
