user = int(input())

for i in range(1, user+1):
    print(i, end=" ")
    a = str(oct(i))
    print(a[2:], end=" ")
    b = str(hex(i))
    print(b[2:].capitalize(), end=" ")
    c = str(bin(i))
    print(c[2:])
