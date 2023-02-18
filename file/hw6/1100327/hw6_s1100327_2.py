def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    l=len(nodes)
    A=[[float('inf') for a in range(l)] for a in range(l)]#創建A矩陣
    for i in nodes:#將點到點之間的距離用A矩陣記錄起來
        for j in nodes:
           if i!=j:
                A[nodes.index(i)][nodes.index(j)]=abs(i[0]-j[0])+abs(i[1]-j[1])    
    count=1
    UsedNode=[0]#紀錄所走過的節點
    ans=0#用來儲存路徑長度
    edge=[]#edge用來記錄已走過節點連接到的所有邊
    Inf=float('inf')
    while count<l:
        for i in UsedNode:#把走過節點的邊都放入edge
            edge+=((A[i]))
        ans+=min(edge)
        UsedNode.append(edge.index(min(edge))%l)#把能選擇的最小邊連接到的節點存入UsedNode
        for i in UsedNode:#這個迴圈用來把所有會形成環的邊都改成inf,這樣在取min的時候就不會取到
            A[i][edge.index(min(edge))%l]=Inf
            A[edge.index(min(edge))%l][i]=Inf
        edge=[]

        
        

        count += 1






    return ans


if __name__ == '__main__':
    nodes = [[3,1],[2,7],[4,8],[7,4]]
    print(homework_6(nodes))
    # 22
    