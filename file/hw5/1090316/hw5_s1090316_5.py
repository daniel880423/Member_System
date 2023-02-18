
import numpy as np

def homework_5(matrix, start, end, total, p=False):
    lst = np.array([[9999 for _ in range(total)] for _ in range(total)])
    lst_ = []
    res = []
    for i in range(total):
        lst[i][i] = 0 
    
    for i in range(len(matrix)):
        lst[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2]

    ini_lst = lst.copy()     
    
    for k in range(total):
        for i in range(total):
            for j in range(total):
                if lst[i][j] > lst[i][k] + lst[k][j]:
                    lst[i][j] = lst[i][k] + lst[k][j]
                    if k+1 not in lst_:
                        lst_.append(k+1)
    
    lst_.append(end)
    lst_.insert(0, start)
    
    if lst[start - 1][end - 1] == 9999:
      res.append(-1)
      res.append(None)
    else:
      res.append(lst[start - 1][end - 1])
      a=''
      for i in lst_:
        a = a + str(i)
      res.append(a)

    if p == True:
      print(ini_lst)
      print('-'*50)
      print(lst)
      print('-'*50)
      print('節點{}到節點{}的最短距離為{}'.format(start, end, lst[start - 1][end - 1]))
      print('路徑為', lst_)

    return res
    
    
if __name__ == '__main__':
    matrix = [[1,2,2],[1,3,1],[1,4,5],[3,4,2],[4,5,1]]
    start = 2;end = 4; total = 5
    print(homework_5(matrix, start, end, total,p=False))