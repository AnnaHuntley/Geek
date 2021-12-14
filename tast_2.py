# не правильно работaет. не успела найти ошибку, если подскажите, буду благодарна

list_cube = []

for number in range(1, 1001):
    list_cube.append(number ** 3)

list_sum = []
suma = 0
for number in list_cube:
    digit = number % 10
    suma += digit
    number = number // 10
    list_sum.append(suma)

sum_7 = 0
for number in list_sum:
    if number % 7 == 0:
        sum_7 += number
print(sum_7)

list_17 = []
for number in list_sum:
    list_17.append(number+17)


sum_7 = 0
for number in list_17:
    if number % 7 == 0:
        sum_7 += number
print(sum_7)

