from importlib.resources import path
def homework_5(matrix, start, end, total):

    initial = [[float("inf")]*total for i in range(total)] #建立一個元素都為無限的陣列
    path = [[-1]*total for i in range(total)] #路徑都先設為-1
    for i in range(total): #自己到自己的距離
        initial[i][i] = 0     
 
    for i in range(len(matrix)): #找出已知的點到點的距離
        initial[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2]
    
    for k in range(total): 
        for i in range(total):
            for j in range(total):
                 if initial[i][k]+initial[k][j] < initial[i][j]:
                    initial[i][j] = min(initial[i][k]+initial[k][j], initial[i][j])
                    path[i][j] = k
    
    if initial[start-1][end-1] != float("inf") and initial[start-1][end-1] != 0: #如果頭到尾的距離不等於無限或零
        ans = [initial[start-1][end-1]]+[str(start)+""]
        get_path(path, start, end, ans)
        ans[1] += str(end)
    else:
        ans = [-1, None]  #頭到尾的距離等於無限或零
    return ans

def get_path(path, start, end, ans): #抓路徑的副程式
    if path[start-1][end-1] != -1:
        get_path(path, start, path[start-1][end-1]+1, ans)
        ans[1] += str(path[start-1][end-1]+1)
        get_path(path, path[start-1][end-1]+1, end, ans)


if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    