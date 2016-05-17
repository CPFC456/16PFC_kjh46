# coding: utf-8

def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b
# 더하기에 대한 함수
def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a - b
# 빼기에 대한 함수
def multiply(a, b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b
# 곱하기에 대한 함수
def divide(a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b
# 나누기에 대한 함수

print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# 변수를 입력
print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")
