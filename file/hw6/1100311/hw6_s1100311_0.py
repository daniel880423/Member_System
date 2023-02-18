def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    import math
    l = len(nodes)
    A = [[float("inf") for i in range(l)] for j in range(l)]          #先設置一個空矩陣
    #print(A)
    
    for i in range(l):                                                #將每一個節點距離算出並放入矩陣中
        for j in range (l):
            
            if i == j:
                A[i][j] = float("inf")
            else:
                n = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
                A[i][j] = n   
    # for i in A:
    #     print(i)
    
    visit = [0]                                          #visit長度等於nodes長度 
    sum = 0                                              #先設最小值為無限
    
    while len(visit)<l:                                           
        min  = float('inf')                              
        for i in visit:
            for j in range(l):
                if min>A[i][j] and j not in visit:       #不能重複尋找
                    min = A[i][j]                        #找出最小值並暫存i,j
                    x = i
                    y = j
                    
        A[x][y] = float("inf")                           #用過的數字變成無限，之後再抓到也不引響計算
        A[y][x] = float("inf")
        
        # print(x, y)
        visit.append(y)                                  #i是一開始的visit,j是後來找到的節點，所以將j放入visit
        #print("\n", min)
        sum += min                                       #把長度最小值加在總長度裡
        
                                             

  
    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(homework_6(nodes))
    # 20
    