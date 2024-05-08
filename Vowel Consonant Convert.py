import random
n = str(input('enter string: '))
a = list(n)
c = ['b','c','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
count = 0
for i in range(len(a)):
    if (a[i] == "a", "A"):
        a[i] = c[random.randint(0, 18)]
        count += 1
    elif (a[i] == "e", "E"):
        a[i] = c[random.randint(0,18)]
        count += 1
    elif (a[i] == "i", "I"):
        a[i] = c[random.randint(0,18)]
        count += 1
    elif (a[i] == "o", "O"):
        a[i] = c[random.randint(0,18)]
        count += 1
    elif (a[i] == "u", "U"):
        a[i] = c[random.randint(0,18)]
        count += 1
    else:
        a[i] = a[i]
b = "".join(map(str,a))
print(b)
print(count)