m = int(input("Ingrese el primer valor "))
n = int(input("Ingrese el segundo valor "))
#a
"""
if m<n:
    long=n-m
    print(m," ",n)
    for i in range(long):
        m += 1
        n -= 1
        print(m," ",n)
else:
    long=m-n
    print(m," ",n)
    for i in range(long):
        m -= 1
        n += 1
        print(m," ",n)
"""

#b

if m<n:
    long=n-m
    print(m," ",n)
    for i in range(long):
        while m<n:
            m += 1
            n -= 1
            print(m," ",n)
else:
    long=m-n
    print(m," ",n)
    for i in range(long):
        while m>n:
            m -= 1
            n += 1
            print(m," ",n)