import time

def numNear(ff, r, c):
    N = 0
    for rr in range(r - 1, r + 2):
        for cc in range(c - 1, c + 2):
            if rr == r and cc == c:
                continue
            if ff[rr][cc] == '*':
                N = N + 1
    return N


def printField(ff):
    for line in ff:
        s = ''
        for a in line:
            s += a
        print(s)
    print()


def main():
    f = []
    f2 = []
    F = open("life.txt", "r")
    for line in F:
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        L = list(line)
        L2 = list(line)
        f.append(L)
        f2.append(L2)
    F.close()

    printField(f)
    for r in range(1, len(f) - 1):
        for c in range(1, len(f[r]) - 1):
            n = numNear(f, r, c)
            f2[r][c] = str(n)
    printField(f2)
    while True:
        n = 0
        for r in range(1, len(f) - 2):
            for c in range(1, len(f[r]) - 1):
                n = numNear(f, r, c)
                if (n == 2 or n == 3) and (f[r][c] == '*') or ((n == 3) and (f[r][c]) == '-'):
                    f2[r][c] = '*'
                else:
                    f2[r][c] = '-'
        for r in range(0, len(f)):
            for c in range(0, len(f[r])):
                f[r][c] = f2[r][c]
                if f[r][c] == '*':
                    n = n + 1
        printField(f)
        if n == 0:
            print('YOU DIED!')
            break
        time.sleep(0.3)


if __name__ == '__main__':
    main()
