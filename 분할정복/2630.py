""" 색종이 만들기 """

import sys
input = sys.stdin.readline
white, blue = 0, 0

def check(x, y, n):
    global white, blue
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2 )
                check(x+n//2, y+n//2, n//2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


if __name__ == "__main__":
    paper = []
    n = int(input())
    for _ in range(n):
        x = list(map(int, input().split()))
        paper.append(x)

    check(0, 0, n)
    print(white)
    print(blue)
