a = 65
n = int(input('enter loop num: '))
for i in range(0,n):
    for j in range(0,i+1):
        v = chr(a)
        print(v,end="")
        a+=1
    print("")