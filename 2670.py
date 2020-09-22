import sys

N = int(sys.stdin.readline())
multi = 1.0
Nmax = -1
for _ in range(0, N):
    inputN = float(sys.stdin.readline())
    multi *= inputN
    if multi > Nmax:
        Nmax = multi
    if multi < 1.0:
        multi = 1.0

print('%.3f' % round(Nmax, 4))