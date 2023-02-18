import math
def homework_5(matrix,start,end,total):
    v_num = total
    distance_0 = [[math.inf]*v_num for i in range(v_num)]
    for row in matrix:
        distance_0[row[0]-1][row[1]-1] = row[2]
    
    prior = [[-1 if distance_0[i][j] == math.inf else j for j in range(v_num)]
             for i in range(v_num)]
    for m in range(v_num):
        for i in range(v_num):
            for j in range(v_num):
                if (distance_0[i][j] > distance_0[i][m]+distance_0[m][j]):
                    distance_0[i][j] = distance_0[i][m]+distance_0[m][j]
                    prior[i][j]=prior[i][m]
                else:
                    continue
    print_l=[]
    if distance_0[start-1][end-1]==math.inf:
        print_l.append([-1,None])
    else:
        print_l.append(distance_0[start-1][end-1])
        
        if prior[start-1][end-1]==end-1:
            print_l.append(str(start)+str(end))
        else:
            path = str(start)
            x = prior[start-1][end-1]
            path+=str(x+1)
            while  prior[x][end-1]!= end-1:
                x = prior[x][end-1]
                path+=str(x+1)
            path+=str(end)
            print_l.append(path)
    
    return print_l
  

if __name__=='__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start =1;end=4;total=4
    print(homework_5(matrix,start,end,total))
    