def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if not N:
      return []
    def generateBoard():           # 生成位置
        board = list()             # 字串轉為列表
        for i in range(N):         # 將 Q or - 放入list
            row[queens[i]] = "Q"
            board.append("".join(row))
            row[queens[i]] = "-"
        return board

    def backtrack(row: int):
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
    