from importlib.resources import path
import numpy as np #用來建立空陣列
def homework_5(matrix, start, end, total,p=False):

    initial = np.array([[9999 for _ in range(total)] for _ in range(total)]) #建立一個total＊total 每個元素都趨近於無限的陣列
    A = [] 
    ans = []
    for i in range(total): #自己到自己
        initial[i][i] = 0 
    
    for i in range(len(matrix)):
        initial[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2]
    ini_lst = initial.copy()     
    
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if initial[i][j] > initial[i][k] + initial[k][j]:
                    initial[i][j] = initial[i][k] + initial[k][j]
                    if k+1 not in A:
                        A.append(k+1)
    A.append(end)
    A.insert(0, start)
    
    if initial[start - 1][end - 1] == 9999:
      ans.append(-1)
      ans.append(None)
    else:
      ans.append(initial[start - 1][end - 1])
      a=''
      for i in A:
        a = a + str(i)
      ans.append(a)

    if p == True:
      print(initial)
      print('-'*50)
      print(initial)
      print('-'*50)
      print('節點{}到節點{}的最短距離為{}'.format(start, end, initial[start - 1][end - 1]))
      print('路徑為', A)

    return ans

if __name__ == '__main__':
    matrix = [[1,2,1],[1,3,1],[3,4,1]]
    start = 1;end = 4; total = 4
    print(homework_5(matrix, start, end, total))
    