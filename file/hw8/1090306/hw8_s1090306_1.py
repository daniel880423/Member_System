def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    def generateBoard():
        board = list()
        for i in range(N):
            row[queens[i]] = "Q"
            board.append("".join(row))
            row[queens[i]] = "-"
        return board

    def backtrack(row: int):
        if N==0:
            solution=[]
            return solution
        if row == N:
            board = generateBoard()
            solutions.append(board)
        else:
            for i in range(N):
                if i in columns or row - i in diagonal1 or row + i in diagonal2:
                    continue
                queens[row] = i
                columns.add(i)
                diagonal1.add(row - i)
                diagonal2.add(row + i)
                backtrack(row + 1)
                columns.remove(i)
                diagonal1.remove(row - i)
                diagonal2.remove(row + i)          
    solutions = list()
    queens = [-1] * N
    columns = set()
    diagonal1 = set()
    diagonal2 = set()
    row = ["-"] * N
    backtrack(0)
    return solutions

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    