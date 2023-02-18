import math
def homework_5(matrix,start,end,total):
    v_num = total
    W = [[math.inf]*v_num for i in range(v_num)] #相鄰矩陣
    for row in matrix:
        W[row[0]-1][row[1]-1] = row[2]
    
    prior = [[-1 if W[i][j] == math.inf else j for j in range(v_num)]
             for i in range(v_num)] #初始化一個空間矩陣用來存放所經過的節點
    for m in range(v_num): 
        for i in range(v_num):
            for j in range(v_num):
                if (W[i][j] > W[i][m] + W[m][j]):
                    W[i][j] = W[i][m] + W[m][j]
                    prior[i][j]=prior[i][m]
                else:
                    continue
    print_l=[]
    if W[start-1][end-1]==math.inf:
        print_l = [-1,None]
    else:
        print_l.append(W[start-1][end-1])
        
        if prior[start-1][end-1] == end-1:
            print_l.append(str(start)+str(end))
        else:
            path = str(start)
            x = prior[start-1][end-1]
            path += str(x+1)
            while  prior[x][end-1] != end-1:
                x = prior[x][end-1]
                path += str(x+1)
            path += str(end)
            print_l.append(path)
    
    return print_l
  

if __name__=='__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start =1;end=4;total=4
    print(homework_5(matrix,start,end,total))
    