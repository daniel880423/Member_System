def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    matrix = [[float("inf")]*len(nodes) for _ in range(len(nodes)) ] #產生n*n矩陣來儲存點之間步數
    for i in range(len(nodes)):
        c1 = nodes[i]
        for j in range(i+1, len(nodes)):
            c2 = nodes[j]
            x1_c = c1[0]    #將題目給定的數值用x,y來代表
            x2_c = c2[0]
            y1_c = c1[1]
            y2_c = c2[1]
            distance = abs(x1_c-x2_c) + abs(y1_c-y2_c)  #去算點跟點之間的距離
            matrix[i][j] = distance     #再將距離存入matrix中
            matrix[j][i] = distance
    visit = [0]     #設出發點為0，visit存放走過的點
    sum = 0         #對走過距離作加法
    while len(visit) < len(matrix):
        min = 101
        for i in range(len(visit)):
            index = visit[i]
            for j in range(len(nodes)-1):
                tmp = matrix[index][j+1]
                if tmp == -1:   #-1代表走過，不走
                    continue
                if tmp < min:
                    min = tmp
                    save_1 = j+1    #將點的x,y存到save_1,save_2
                    save_2 = index
        matrix[save_2][save_1] = -1     #將走過的點設為-1
        matrix[save_1][save_2] = -1
        ans = False
        for k in range(len(visit)):
            if visit[k] == save_1:
                ans = True
                break
        if ans == False:
            visit.append(save_1)    #將走過的點加入visit
            sum += min  #加上步數
    return sum 

if __name__ == '__main__':
    nodes =  [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 22
    