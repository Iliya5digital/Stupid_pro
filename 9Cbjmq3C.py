def moves(h):
    return h + 3, h * 2


def game(h):
    if h >= 33:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'


for i in range(1, 33):
    if game(i) == 'P1':
        print(i, game(i), end=' ')
        print()
# print('\n\\')
#
for i in range(1, 33):
    if game(i) == 'B1':
        print(i, game(i))

print()

for i in range(1, 33):
    if game(i) == 'P2':
        print(i, game(i))

print()

for i in range(1, 33):
    if game(i) == 'B2':
        print(i, game(i))

def moves(h):
    return h + 4, h * 3

def game(h):
    if h >= 70:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'

for i in range(1, 70):
    if game(i) == 'B2':
        print(i, game(i))

def moves(h):
    return h + 4, h * 2


def game(h):
    if h >= 35:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)):
        return 'B2'


for i in range(1, 35):
    if game(i) == 'B1':
        print(i, game(i))
from functools import lru_cache


@lru_cache(None)
def moves(h):
    return h + 3, h * 3


def game(h):
    if h >= 60:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)):
        return 'B2'


for i in range(1, 60):
    if game(i) == 'B2':
        print(i, game(i))
from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 2, b), (a, b + 2), (a * 2, b), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 75:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)):
        return 'B2'


for i in range(1, 66):
    j = 9, i
    if game(j) == 'B2':
        print(i, game(j))


from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 83:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)):
        return 'B2'


for i in range(1, 74):
    j = 9, i
    if game(j) == 'B2':
        print(i, game(j))

