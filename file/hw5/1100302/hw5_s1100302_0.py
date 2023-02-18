def homework_5(matrix, start, end, total): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
        # 一個矩陣存取節點到節點間的路徑，一個矩陣存取節點中插入的中轉點。
    point = []
    pace(start,end,matrix,point,0)
    ans = ''
    for i in point:
        a = str(i)
        ans += a
    length = 0
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            if len(point) >=2:
                if matrix[i][0] == point[0] and matrix[i][1] == point[1]:
                    length += matrix[i][2]
                    point.pop(0)
    if len(point) ==0:
        return[-1,None]
    return [length,ans]
def pace(loc1,loc2,matrix,point,checkpoint):
    error = 0
    for i in range(len(matrix)):
        if loc1 == matrix[i][0] and matrix[i][1]!= checkpoint:
            point.append(matrix[i][0])         
            pace(matrix[i][1],loc2,matrix,point,matrix[i][0])
        else:
            error +=1
        if error == len(matrix) and len(point)!=0:
            point.pop(-1)
        if loc1 == loc2:
            point.append(loc1)
            break




if __name__ == '__main__':
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
