import copy
import numpy as np
def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    r=len(nodes)  #先寫出長度

    #複製一個node，轉換成節點
    nodes1=nodes.copy() 
    for i in range(r):
        nodes1[i]=[1*(i+1)] #節點
    l=[]
    for i in range(r-1):
        for j in range(i,r-1):
            l.extend(nodes1[i])
            l.extend(nodes1[j+1])
            l.append(abs(nodes[i][0]-nodes[j+1][0])+abs(nodes[i][1]-nodes[j+1][1])) #寫出所有節點的距離
    #將各節點與節點距離分好
    step=3
    l=[l[i:i+step]for i in range (0,len(l),step)]
    l.sort(key = lambda x: x[2]) 

    p=np.arange(1,r+1,1) #寫下共幾個頂點
    #將每頂點設為一個樹
    tree=dict() #用字典表示，鍵為頂點，鍵值為樹的節點
    for i in p:
        tree[i]=i
    #尋找根結點
    def find_node(k):
        if tree[k]!=k:
            tree[k]=find_node(tree[k])
        return tree[k]
    mst=[] #設最小生成樹
    time=r-1 #循環次數
    for i in range(len(l)):
        m=l[i][0]
        n=l[i][1]
        if find_node(m)!=find_node(n):
            tree[find_node(n)]=find_node(m)
            mst.append(l[i])
            time-=1
            print(mst)
            if n==0:
                break
    ans=0
    for i in range (len(mst)): #將節點與節點間的距離相加
        ans+=(mst[i][2])

    return ans 

if __name__ == '__main__':
    nodes =    [[0,0],[2,6],[3,9],[6,4],[7,1]]

    print(homework_6(nodes))
    # 22