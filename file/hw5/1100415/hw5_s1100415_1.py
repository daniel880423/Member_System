def homework_5(matrix, start, end, total):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    step = []
    go_through = []
    total += 1
    ans = ""
    for i in range(0, total):
        t_1 = []
        t_2 = []
        for terminal in range(0, total):
            t_1.append(101)
            t_2.append(terminal)
        step.append(t_1)
        go_through.append(t_2)
    for v in matrix:
        step[v[0]][v[1]] = v[2]
    for passby in range(0, total):
        for go in range(0, total):
            for terminal in range(0, total):
                if (step[go][passby]+step[passby][terminal] < step[go][terminal]):
                    step[go][terminal] = step[go][passby]+step[passby][terminal]
                    go_through[go][terminal] = go_through[go][passby]

    def step_calculate(ans, p, q):
        ans += str(p)
        if (p != q):
            return step_calculate(ans, go_through[p][q], q)
        else:
            return ans
    ans = step_calculate(ans, start, end)
    if step[start][end] == 101:
        return[-1,None]
    else:
        return [step[start][end], ans]


if __name__ == '__main__':
    matrix =[[1,2,1],[1,3,3],[2,1,2],[3,4,4]]
    start = 2
    end = 3
    total = 4
    print(homework_5(matrix, start, end, total))
