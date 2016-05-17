# -*-coding:utf8

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# 리스트에는 숫자나 문자열이 들어갈 수 있고 리스트 안에 리스트를 넣을 수 있다.

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruits in fruits:
    print "A fruit of type: %s" % fruits

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i


# for문은 여러 변수들을 나열할 수 있다??    결과문 참조
# range()는 등차수열을 만들어 준다고 보면 됨