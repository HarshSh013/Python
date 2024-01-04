def showBoard(chess):
  for i in range(len(chess)) :
    for j in range(len(chess)) :
      print(chess[i][j], "", end = '')
    print()
  print()


def Kt(chess, n, r, c, nextmove):
    if (r<0 or c<0 or r >= n or c >= n or chess[r][c] != 0):
            return

    if (nextmove == n * n):
            chess[r][c] = nextmove
            showBoard(chess)
            chess[r][c] = 0
            return

    chess[r][c] = nextmove
    Kt(chess, n, r - 2, c + 1, nextmove + 1)
    Kt(chess, n, r - 1, c + 2, nextmove + 1)
    Kt(chess, n, r + 1, c + 2, nextmove + 1)
    Kt(chess, n, r + 2, c + 1, nextmove + 1)
    Kt(chess, n, r + 2, c - 1, nextmove + 1)
    Kt(chess, n, r + 1, c - 2, nextmove + 1)
    Kt(chess, n, r - 1, c - 2, nextmove + 1)
    Kt(chess, n, r - 2, c - 1, nextmove + 1)
    chess[r][c] = 0
def main():
    n = int(input())
    chess = []
    for i in range(n):
        a = []
    for j in range(n) :
        a.append(0)
    chess.append(a)
    row = int(input())
    col = int(input())
    print(chess, n, row, col, 1)
    main()