def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    global PathLen
    global count
    l=len(nodes)
    A=[[float('inf') for a in range(l)] for a in range(l)]#創建A矩陣
    for i in nodes:#將點到點之間的距離用A矩陣記錄起來
        for j in nodes:
           if i!=j:
                A[nodes.index(i)][nodes.index(j)]=abs(i[0]-j[0])+abs(i[1]-j[1])
    print(A)
    PathLen=0     
    count=0
    for i in range(0,l):
        A[i][0]=float('inf')
    ans=prim(0,A)
    




    return ans

def prim(node,matrix):
    global PathLen
    global count
    if count!=len(matrix)-1:
        newNode=matrix[node].index(min(matrix[node]))
        PathLen+=(min(matrix[node]))
        count+=1
        matrix[node][newNode]=float('inf')
        for i in range(0,len(matrix)):
            matrix[i][node]=float('inf')
        prim(newNode, matrix)
    return PathLen
if __name__ == '__main__':
    nodes = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(homework_6(nodes))
    # 22
    