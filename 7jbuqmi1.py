# s = open("24_2419.txt").readline()
# s = s.replace('A', ' ').replace('B', ' ')
# max_len = 0
# for i in s.split():
#     max_len = max(max_len, len(i))
# print(max_len)
# print(max(len(c) for c in s.split()))

s = open('24_2427.txt').readline()
c = m = s[0]
for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        c += s[i]
        m = max(m, c, key=len)
    else:
        c = s[i]
print(m)

s = open('24_1145.txt').readline()
s = s.replace('D', 'D D')
print(min(len(c) for c in s.split() if c[0] == 'D' and c[len(c) - 1] == 'D' and len(c) > 2))

s = open('24_1146.txt').readline()
for c in 'ABCEF':
    s = s.replace(c, ' ')
s = s.split()
print(min(len(c) for c in s))

s = open('24_2250.txt').readline()
s = s.split('A')
m = -10000
for i in range(len(s) - 1):
    sub = s[i] + "A" + s[i + 1]
    m = max(m, len(sub))
print(m)

s = open('24_2251.txt').readline()
m = 0
s = s.split('D')
for i in range(len(s) - 2):
    sub = s[i] + 'D' + s[i + 1] + 'D' + s[i + 2]
    m = max(len(sub), m)
print(m)

s = open('24_4602.txt').readline()
s = s.replace('O', 'A').replace('C', 'B').replace('D', 'B')
sub = 'BA'
print(sub in s)
while sub in s:
    sub += 'BA'
print(len(sub) // 2)

s = open('24_4642.txt').readline()
s = s.replace('B', 'A').replace('2', '1')
sub = 'A1' * 34
print(sub in s)
while sub in s:
    sub += 'A1'
print(len(sub) / 2)


s = open('24_4643.txt').readline()
s = s.replace('B', 'A').replace('2', '1')
s = s.replace('11A', '*')
s = s.replace('1', ' ').replace('A', ' ')
print(max(len(c) for c in s.split()))

s = open('24_4546.txt').readline()
s = s.replace('B', '*')

c = m = 0
for i in range(0, len(s) - 2, 3):
    sub = s[i] + s[i + 2]
    if sub == "AA" or sub == "CC":
        c += 1
        m = max(m, c)
    else:
        c = 0
c = 0
for i in range(1, len(s) - 2, 3):
    sub = s[i] + s[i + 2]
    if sub == "AA" or sub == "CC":
        c += 1
        m = max(m, c)
    else:
        c = 0
c = 0
for i in range(2, len(s) - 2, 3):
    sub = s[i] + s[i + 2]
    if sub == "AA" or sub == "CC":
        c += 1
        m = max(m, c)
    else:
        c = 0

print(m)

# s = open('24_5171.txt').readline()
# sub = 'CA'
# while sub in s:
#     sub += 'CA'
# print(len(sub) / 2)
# sub = 27 * 'CA'
# print(sub in s)

s = open('24_2497.txt').readline()
print(s.count('XVIII'))

s = open('24_223.txt').readline()
print(s.count('TIK') + s.count('TOK'))

s = open('24_314.txt').readline()
print(s.count('OCK') - s.count('STOCK'))

s = open('24_279.txt').readline()
print(s.count('BOSS') - (s.count('JBOSS') + s.count('BOSSJ') - s.count('JBOSSJ')))

s = open('24_2498.txt').readline()
while 'XIXIX' in s:
    s = s.replace('XIXIX', 'XIX XIX')
print(s.count('XIX'))
c = 0
for i in range(len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] == 'XIX':
        c += 1
print(c)

s = open('24_2499.txt').readline()
c = 0
for i in range(len(s) - 3):
    sub = s[i] + s[i + 1] + s[i + 2] + s[i + 3]
    if sub == 'XXXX':
        c += 1
print(c)

s = open('24_2500.txt').readline()
c = 0
for i in range(len(s) - 3):
    sub = s[i] + s[i + 2] + s[i + 3]
    if sub == "GME":
        c += 1
print(c)

s = open('24_2501.txt').readline()
c = 0
for i in range(len(s) - 4):
    sub = s[i] + s[i + 2] + s[i + 4]
    if sub == 'AAA':
        c += 1
print(c)

c = 0
with open('24_859.txt') as file:
    for line in file:
        if line.count('S') == line.count('X'):
            c += 1
print(c)

c = 0
with open('24_587.txt') as file:
    for line in file:
        res = (line.count('B') - line.count('A')) / line.count('B')
        if res > 0 and (res - 0.05) > 0.0001:
            c += 1
print(c)

c = 0
with open('24_2502.txt') as file:
    for line in file:
        flag = 0
        for j in range(len(line) - 3):
            sub = line[j] + line[j + 2] + line[j + 3]
            if sub == 'KGE':
                flag = 1
        if flag:
            c += 1
print(c)

with open('24_2503.txt') as file:
    c = 0
    for line in file:
        c_oao = 0
        c_aoa = 0
        for j in range(len(line) - 2):
            sub = line[j] + line[j + 1] + line[j + 2]
            if sub == 'OAO':
                c_oao += 1
            elif sub == 'AOA':
                c_aoa += 1
        if c_aoa > c_oao:
            c += 1
print(c)

s = open('24_1143.txt').readline()
c = 0
for i in range(len(s) - 6):
    if s[i] == 'A' and s[i + 6] == 'F':
        c += 1
for i in range(len(s) - 7):
    if s[i] == 'A' and s[i + 7] == 'F':
        c += 1
for i in range(len(s) - 8):
    if s[i] == 'A' and s[i + 8] == 'F':
        c += 1
for i in range(len(s) - 9):
    if s[i] == 'A' and s[i + 9] == 'F':
        c += 1
print(c)

s = open('24_836.txt').readline()
c = 0
for i in range(len(s) - 4):
    if s[i] == s[i + 4] and s[i + 1] == s[i + 3]:
        c += 1
print(c)

s = open('24_2506.txt').readline().strip()
d = {x: s.count(x) for x in sorted(set(s))}
print(max(d))
print(d.keys())
print(d.values())

s = open('24_2509.txt').readline().strip()
d = {x: s.count(x) for x in sorted(set(s))}
print(max(d.values()) - min(d.values()))

s = open('24_2505.txt').readline().strip()
d = {x: 0 for x in sorted(set(s))}
for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        d[s[i + 1]] += 1
print(max(d.values()))

s = open('24_2504.txt').readline().strip()
d = {x: 0 for x in sorted(set(s))}
c = 0
for i in range(len(s) - 4):
    if s[i] + s[i + 1] + s[i + 3] + s[i + 4] == 'CBBC':
        d[s[i + 2]] += 1

with open('24_2508.txt') as file:
    q = 0
    q_max = 0
    cur_line = ''
    for line in file:
        q = line.count('Q')
        if q >= q_max:
            q_max = q
            cur_line = line
cur_line = cur_line.strip()
d = {x: cur_line.count(x) for x in sorted(cur_line)}
print(min(d.values()))
#'C': 22

ans = 0
with open('24_2508.txt') as file:
    for line in file:
        ans += line.count('C')
print('C', ans)

m, ms = 0, ''
s1 = ''
for s in open('24_2507.txt'):
    s1 += s
    m1 = c = s[0]
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            c += s[i]
            m1 = max(m1, c, key=len)
        else:
            c = s[i]
    if len(m1) > m:
        m, ms = len(m1), s.strip()

d = {x: ms.count(x) for x in sorted(set(ms))}
m = max(d.values())
l = [i for i in d if d[i] == m]
print(l, m)
print(m, s1.count(l[0]))


