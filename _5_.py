def f(n):
    str_n = str(n)
    first = int(str_n[0]) + int(str_n[1])
    second = int(str_n[2]) + int(str_n[3])
    return str(max(first, second)) + str(min(first, second))


for i in range(1000, 10000):
    if f(i) == "1512":
        print(i)
        break

def f(n):
    bin_n = bin(n).removeprefix('0b')
    if bin_n.count('1') % 2 == 0:
        bin_n += '1'
    else:
        bin_n += '0'

    if bin_n.count('1') % 2 == 0:
        bin_n += '1'
    else:
        bin_n += '0'

    return int(bin_n, 2)


ans = []
for i in range(1, 100000):
    if f(i) > 54:
        ans.append(f(i))
print(ans[0])

def f(n):
    bin_n = bin(n).removeprefix('0b')
    for j in range(2):
        if bin_n.count('1') % 2 == 0:
            bin_n += '0'
        else:
            bin_n += '1'
    return int(bin_n, 2)
ans = []
for i in range(1000):
    if f(i) > 96:
        ans.append(i)
print(min(ans))

def f(n):
    bin_n = bin(n).removeprefix('0b')
    for j in range(2):
        if bin_n.count('1') % 2 == 0:
            bin_n += '0'
        else:
            bin_n += '1'
    return int(bin_n, 2)

ans = []
for i in range(1000):
    if f(i) > 116:
        ans.append(f(i))
print(min(ans))

def f(x):
    first = x % 4
    second = x % 2
    third = x % 3
    return str(first) + str(second) + str(third)

for i in range(1000):
    if f(i) == "311":
        print(i)
        break

def f(n):
    str_n = str(n)
    first = int(str_n[0]) + int(str_n[1])
    second = int(str_n[1]) + int(str_n[2])
    third = int(str_n[2]) + int(str_n[3])
    ans = [first, second, third]
    ans.sort()
    ans.pop(0)
    return str(ans[1]) + str(ans[0])


a = []
for i in range(1000, 10000):
    if f(i) == '1414':
        a.append(i)
print(max(a))

def f(n):
    bin_n = bin(n).removeprefix('0b')
    for j in range(2):
        if bin_n.count('1') % 2 == 0:
            bin_n += '0'
        else:
            bin_n += '1'
    return int(bin_n, 2)


ans = []
for i in range(1000):
    ans.append(f(i))
ans.sort()
ans = [c for c in ans if 16 <= c <= 32]
cntr = 0
for i in range(16, 33):
    if i not in ans:
        cntr += 1
print(cntr)

print(ans, 33 - 16 - 4)

def f(n):
    bin_n = bin(n).removeprefix('0b')
    if len(bin_n) < 8:
        while len(bin_n) != 8:
            bin_n = '0' + bin_n
    new_str = ''
    for i in range(len(bin_n)):
        if bin_n[i] == '0':
            new_str += '1'
        else:
            new_str += '0'
    return int(new_str, 2)


for i in range(256):
    new = f(i)
    if new - i == 99:
        print(i)

def f(n):
    str_n = str(n)
    a, b, c = int(str_n[0]), int(str_n[1]), int(str_n[2])
    arr = [a, b, c]
    arr.sort()
    big = int(str(arr[2]) + str(arr[1]))
    small = int(str(arr[0]) + str(arr[1]))
    if 9 < big < 100 and 9 < small < 100:
        return big - small
    else:
        return 0


cntr = 0
for i in range(300, 401):
    if f(i) == 20:
        cntr += 1
print(cntr)

def f(n):
    str_n = str(n)
    a = int(str_n[0]) + int(str_n[3])
    b = int(str_n[1]) + int(str_n[2])
    return str(max(a, b)) + str(min(a, b))

for i in range(1000, 10000):
    if f(i) == '128':
        print(i)
        break

def f(n):
    bin_n = bin(n).removeprefix('0b')
    for i in range(2):
        if bin_n.count('1') % 2 == 0:
            bin_n += '0'
        else:
            bin_n += '1'
    return int(bin_n, 2)


ans = []
for i in range(1, 1000):
    if f(i) > 130:
        ans.append(f(i))
print(min(ans))


def f(n):
    str_n = str(n)
    a = int(str_n[0]) + int(str_n[2]) + int(str_n[4])
    b = int(str_n[1]) + int(str_n[3])
    return int(str(min(a, b)) + str(max(a, b)))


for i in range(10000, 100000):
    if f(i) == 621:
        print(i)

def f(x):
    a, b, c = x % 4, x % 3, x % 2
    s = str(a) + str(b) + str(c)
    return int(s)

ans = []
for i in range(10, 100):
    if f(i) == 220:
        ans.append(i)
print(max(ans))

def f(n):
    str_n = bin(n).removeprefix('0b')
    if len(str_n) < 8:
        while len(str_n) != 8:
            str_n = '0' + str_n
    new = ''
    for i in range(len(str_n)):
        if str_n[i] == '1':
            new += '0'
        else:
            new += '1'
    return int(new, 2)


for j in range(0, 256):
    k = f(j)
    if k - j == -21:
        print(j)
10001010 -> 01110101

def f(n):
    str_n = bin(n).removeprefix('0b')
    str_n = str_n[::-1]
    str_n = str(int(str_n))
    return int(str_n, 2)

ans = []
for i in range(1, 101):
    if f(i) == 7:
        ans.append(i)
print(max(ans))