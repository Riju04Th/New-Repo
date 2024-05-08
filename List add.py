a = ([7, 8], [9, 1], [10, 7])
print("The original tuple is : " + str(a))
b = sum(list(map(sum, list(a))))
print("The summation of tuple elements are : " + str(b))