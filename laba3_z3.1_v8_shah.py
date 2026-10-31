import math

print("Задание 3.1, Вариант 8\n")

s = list(map(int, input('Введите элементы массива: ').split()))
s_sum = sum(s)
s_prois = math.prod(s)

print(f"Список: {s}")
print(f"Сумма элементов списка: {s_sum}")
print(f"Произведение элементов списка: {s_prois}")
