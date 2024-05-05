#sum of products of a number upto 10
def product(num):
    sum = 0
    for i in range(11):
        sum += num * i
    return sum
product(15)
