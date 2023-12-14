# with open('26_813.txt') as file:
#     s, n = map(int, file.readline().split()) #свободное место на диске и число пользователей
#     a = [int(x) for x in file]
# a.sort(reverse=True)
# summa = 0
# k = 0
# last_one = 0
# for i in range(len(a) // 2):
#     if summa + a[i] <= s:
#         summa += a[i]
#         k += 1
#         last_one = a[i]
#         a[i] = 0
#     if summa + a[len(a) - i - 1] <= s:
#         summa += a[len(a) - i - 1]
#         k += 1
#         last_one = a[len(a) - i - 1]
#         a[i] = 0
# a = [int(x) for x in a if x != 0]
# print(a)
# print(last_one, summa, k)

# with open('26_838.txt') as file:
#     n = int(file.readline())
#     a = [int(x) for x in file]
#
# a.sort()
# first = [max(a)]
# second = []
# a.pop(len(a) - 1)
# # print(a)
#
# for t in range(2053):
#     i = 0
#     while sum(second) <= sum(first):
#         second.append(a[i])
#         a[i] = 0
#         i += 1
#     a = [int(x) for x in a if x != 0]
#     first.append(max(a))
#     a.pop(len(a) - 1)
#
# print(a)
# print(first)
# print(sum(first))
# print(second)
# print(sum(second))
# print(len(first), len(second) + 1)

# with open('26_936.txt') as file:
#     n, s = map(int, file.readline().split())
#     a = [int(c) for c in file.readlines()]
#
# a.sort(reverse=True)
# summa = 0
# k = 0
# last = 0
#
#
# while len(a) > 0:
#     for i in range(len(a)):
#         if summa + a[i] <= s:
#             summa += a[i]
#             a[i] = 0
#     a = [int(c) for c in a if c != 0]
#     print(len(a))
#     k += 1
#     last = summa
#     summa = 0
# print(k, last)

# with open('26_1079.txt') as file:
#     n = file.readline()
#     a = [int(c) for c in file]
#
# a.sort()
# print(a)
# ans = []
#
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) % 2 == 0:
#             mid = (a[i] + a[j]) // 2
#             if a[2499] < mid < a[3750]:
#                 ans.append(mid)
# print(len(ans), min(ans))

# with open('26_1257.txt') as file:
#     n = int(file.readline())
#     a = [int(c) for c in file]
#
# a.sort()
# d = set(a)
# ans = []
#
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         summa = a[i] + a[j]
#         if summa % 2 == 1 and summa in d:
#             ans.append(summa)
# print(len(ans), max(ans))\

# with open('26_2652.txt') as file:
#     n = int(file.readline())
#     a = [int(c) for c in file]
#
# d = set(a)
# max_ans = -10 ** 10
#
# for i in d:
#     max_ans = max(max_ans, a.count(i))
#
# print(len(d), max_ans)

# with open('26_2480.txt') as file:
#     n = int(file.readline())
#     d = [c for c in file]
#
# a = [0] * 2_000_001
#
# for i in d:
#     x, y = map(int, i.split())
#     a[x] += 1
#     a[y] -= 1
#
# count, length = 0, 0
# k = 0
# st, end = -1, 0
#
# for i in range(len(a)):
#     k0 = k
#     k += a[i]
#     if k > 0 and st == -1:
#         st = i
#     if k == 0 and k0 > 0:
#         end = i
#         length += end - st
#         count += 1
#         st, end = -1, 0
#
# print(count, length)

# with open('26_2650.txt') as file:
#     l, m, n = map(int, file.readline().split())
#     d = [c for c in file]
#
# a = [0] * (l + 1)
#
# a[0] += 1
#
# for i in range(len(d)):
#     x, time = map(int, d[i].split())
#     a[x] -= 1
#     a[x + time] += 1
# a[l] -= 1
#
# # print(a.count(1), a.count(-1))
#
# ans = []
# count = 0
# k = 0
# st, end = -1, 0
#
# for i in range(len(a)):
#     k0 = k
#     k += a[i]
#     if k > 0 and st == -1:
#         st = i
#     if k == 0 and k0 > 0:
#         end = i
#         length = end - st
#         print(length)
#         if length >= m:
#             ans.append(length)
#         st, end = -1, 0
#
# print(len(ans), max(ans))

# mx = -10 ** 10
# my = -10 ** 10
# counter = 0
# a = [[0] * 9 for c in range(2000)]
# with open('26_2651.txt') as file:
#     n = int(file.readline())
#     for line in file:
#         year, tp = map(int, line.split())
#         a[year][tp] += 1
#
# for i in range(1961, 1992):
#     k = 0
#     for j in range(1, 9):
#         if a[i][j] == 0:
#             k += 1
#     counter += k
#     if k >= mx:
#         mx = k
#         my = i
#
# print(counter, my)

# for i in range(1961, 1992):
#     print(a[i])

with open('26_2653.txt') as file:
    n = file.readline()
    a = [int(c) for c in file]

a.sort()
ans = [a[0]]
print(a)
# for i in range(1, len(a)):
#     ans.append(a[i])
#     for elem in range(len(ans)):
#         ans.append(a[i] + ans[elem])

d = set()
d.add(a[0])
for i in range(1, len(a)):
    d.add(a[i])
    adding = set()
    for elem in d:
        adding.add(a[i] + elem)
    d = d.union(adding)
ans = sorted(c for c in d)
count = 0
for i in range(len(ans) - 1):
    count += (ans[i + 1] - ans[i] - 1)
print(count)
print(ans[200:])

