with open('1-1.txt') as file:
    s = file.readline()
c = 1
ans = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        c += 1
        ans = max(ans, c)
    else:
        c = 1
print(ans)

with open('1-2.txt') as file:
    s = file.readline()
c = 1
ans = 0
for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) != 'IT' and (s[i] + s[i + 1]) != 'TI':
        c += 1
        ans = max(ans, c)
    else:
        c = 1
print(ans)
s = s.replace('IT', 'I T').replace('TI', 'T I')
print(max(len(c) for c in s.split()))

with open('1-3.txt') as file:
    s = file.readline()
c = 0
for i in range(len(s) - 2):
    if (s[i] in 'A E F') and (s[i + 1] in 'A B C') and (s[i + 2] in 'B C D F') and \
            (s[i] != s[i + 1]) and (s[i + 1] != s[i + 2]) and (s[i] != s[i + 2]):
        c += 1
print(c)

with open('1-4.txt') as file:
    s = file.readline()
sub = 'CAT'
while sub in s:
    sub += 'CAT'
sub = 'CAT' * 2 + ''
print(sub in s)

with open('1-3.txt') as file:
    s = file.readline()
s = s.replace('E', ' ').replace('F', ' ')
print(max(len(c) for c in s.split()))

with open('1-3.txt') as file:
    s = file.readline()
c = 0
for i in range(len(s) - 3):
    if (s[i] in 'A C E') and (s[i + 1] != s[i]) and (s[i + 1] != s[i + 2]) and (s[i + 2] in 'A D F') and (s[i + 3] == s[i]):
        c += 1
print(c)

with open('1-1.txt') as file:
    s = file.readline()
c = 1
ans = 0
for i in range(len(s) - 1):
    h = s[i] + s[i + 1]
    if h not in 'XX YY':
        c += 1
        ans = max(ans, c)
    else:
        c = 1
print(ans)
while 'XX' in s:
    s = s.replace('XX', 'X X')
while 'YY' in s:
    s = s.replace('YY', 'Y Y')
print(max(len(c) for c in s.split()))

with open('1-2.txt') as file:
    s = file.readline()
c = 0
for i in range(len(s) - 4):
    h = s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4]
    copyh = h
    h = h[::-1]
    if h == copyh:
        c +=1
print(c)

with open('2-2 (1).txt') as file:
    s = file.readline()
c = 0
for i in range(len(s) - 2):
    if s[i] <= s[i + 1] <= s[i + 2]:
        c += 1
print(c)

with open('2-2 (1).txt') as file:
    s = file.readline()
ans = []
add = s[0]
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        add += s[i + 1]
    else:
        ans.append(add)
        add = s[i + 1]
print(ans)
t = max(len(c) for c in ans)
print(t)
for i in range(len(ans)):
    if len(ans[i]) == t:
        print(ans[i], len(ans[i]), t)
        break

with open('2-3.txt') as file:
    s = file.readline()
for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(c, ' ')
s = [int(c) for c in s.split()]
ans = 0
for i in range(len(s)):
    if int(s[i]) % 2 == 1:
       ans = max(ans, s[i])
print(ans)

with open('2-4.txt') as file:
    s = file.readline()
s = s.replace('MOON', 'MOO OON')
print(max(len(c) for c in s.split()))

c = 0
with open('2-5.txt') as file:
    for line in file:
        s = line
        for i in range(len(s) - 3):
            if s[i] == 'M' and s[i + 2] == 'H' and s[i + 3] == 'P':
                c += 1
                break
print(c)

min_c = 10 ** 10
min_str = ''
cntr = 0
with open('2-5.txt') as file:
    for line in file:
        s = line
        cntr += s.count('R')
        if s.count('F') < min_c:
            min_c = s.count('F')
            min_str = s
work = min_str.strip()
d = {x: work.count(x) for x in sorted(set(work))}
print(max(d.values()))
print(d)
print('R', cntr)

ans = []
with open('2-2 (1).txt') as file:
    s = file.readline()
    for i in range(len(s) - 8):
        if s[i] <= s[i + 1] <= s[i + 2] <= s[i + 3] <= s[i + 4] <= s[i + 5] <= s[i + 6] <= s[i + 7] <= s[i + 8]:
            ans.append(s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] + s[i + 5] + s[i + 6] + s[i + 7] + s[i + 8])
print(ans[0], len(ans))

with open('2-3.txt') as file:
    s = file.readline()
for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(c, ' ')
a = [int(c) for c in s.split() if len(c) == 5 and int(c) % 3 == 0]
print(len(a))
print(a) #неправильно, учитываеются 4-е числа

with open('2-6.txt') as file:
    s = file.readline()
s = s.replace('PEP8', 'PEP EP8')
print(max(len(c) for c in s.split()))

max_len = -10 ** 10
cur_len = ''
cntr = 0
with open('2-5.txt') as file:
    for line in file:
        s = line
        c = 1
        l = s[0]
        cntr += s.count('U')
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                c += 1
                l += s[i + 1]
            else:
                if c > max_len:
                    max_len = c
                    cur_len = line
                l = s[i + 1]
                c = 1
print(cur_len)
cur_len = cur_len.strip()
d = {x: cur_len.count(x) for x in sorted(set(cur_len))}
print(min(d.values()))
print(d)
print('U', cntr)


