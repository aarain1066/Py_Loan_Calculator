a = int(input())
b = int(input())

new_list = [a, b]
counter = 0
sum_num = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        new_list.append(i)
        counter += 1
        sum_num += i

print(f"{sum_num / counter}")




