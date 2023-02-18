def homeworpassby_5(matrix, start, end, total):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。

    step = []
    go_through = []
    total += 1
    ans = ""
    for i in range(0, total):
        tempone = []
        temptwo = []
        for terminal in range(0, total):
            tempone.append(101)
            temptwo.append(terminal)
        step.append(tempone)
        go_through.append(temptwo)
    for v in matrix:
        step[v[0]][v[1]] = v[2]
    for passby in range(0, total):
        for start in range(0, total):
            for terminal in range(0, total):
                if (step[start][passby]+step[passby][terminal] < step[start][terminal]):
                    step[start][terminal] = step[start][passby]+step[passby][terminal]
                    go_through[start][terminal] = go_through[start][passby]

    def step_calculate(ans, p, q):
        ans += str(p)
        if (p != q):
            return step_calculate(ans, go_through[p][q], e)
        else:
            return ans
    ans = step_calculate(ans, start, end)
    if step[start][end] == 101:
        return[-1,None]
    else:
        return [step[start][end], ans]


if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1
    end = 4
    total = 4
    print(homeworpassby_5(matrix, start, end, total))
