def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    l = len(nodes)
    sumlst=[]
    length = 0
    
    for i in range(l-1):  
        for j in range(l-i-1):   
            lst= []
            d = abs(nodes[i][0]- nodes[j+1+i][0]) + abs(nodes[i][1]- nodes[j+1+i][1])  #計算每個節點和其他節點的距離
            lst.append(d)            #距離
            lst.append(i)            #起點
            lst.append(i+j+1)        #終點
            sumlst.append(lst) 
    sumlst = sorted(sumlst)          #根據距離由小到大排列
    
    p =[] 
    for i in range(l):               #初始化
        p.append(i)
    
    def find(i):                     #找出最小距離 如果跟節點不同 繼續遞迴尋找
        if p[i] == i:   
            return i
        else:      
            return find(p[i])
    
    for i in range(l):  
        if find(sumlst[i][1])!=find(sumlst[i][2]):
            p[find(sumlst[i][1] )]= find(sumlst[i][2])
            length+=sumlst[i][0]  
    return length 

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    #nodes = [[3,1],[2,7],[4,8],[47,4]]

    print(homework_6(nodes))
    # 22
    