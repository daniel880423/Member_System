def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    matrix = [[0]*len(nodes) for _ in range(len(nodes)) ]
    for i in range(len(nodes)):
        c1 = nodes[i]
        for j in range(i+1, len(nodes)):
            if i == j-1:
                matrix[i][j-1] = float("inf")
            c2 = nodes[j]
            x1_c = c1[0]
            x2_c = c2[0]
            y1_c = c1[1]
            y2_c = c2[1]
            distance = abs(x1_c-x2_c) + abs(y1_c-y2_c)
            matrix[i][j] = distance
            matrix[j][i] = distance
    matrix[len(nodes)-1][len(nodes)-1] = float("inf")
    visit = [0]
    sum = 0
    while len(visit) < len(matrix):
        min = 101
        for i in range(len(visit)):
            index = visit[i]
            for j in range(len(nodes)-1):
                tmp = matrix[index][j+1]
                if tmp == -1:
                    continue
                if tmp < min:
                    min = tmp
                    save_1 = j+1
                    save_2 = index
        matrix[save_2][save_1] = -1
        matrix[save_1][save_2] = -1
        ans = False
        for k in range(len(visit)):
            if visit[k] == save_1:
                ans = True
                break
        if ans == False:
            visit.append(save_1)
            sum += min
    return sum 

if __name__ == '__main__':
    nodes =  [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 22
    