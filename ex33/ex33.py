# coding: utf-8


i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", str(numbers))
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)

# for은 리스트, while은 조건식