def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    import math

    A=[]
    for i in range(len(nodes)):
        A.append(i)
    point = []
    for i in range(len(nodes)-1):
        for j in range(i+1,len(nodes)):
            x = abs(nodes[i][0] - nodes[j][0])
            y = abs(nodes[i][1] - nodes[j][1])
            point.append ([i,j,x+y,])
    point = sorted(point, key=lambda x: x[2])
    def query_def(x):
        if A[x] != x:
            A[x] = query_def(A[x])
        return A[x]
    result = 0
    for u, v, w in point:
        root_u = query_def(u)
        root_v = query_def(v)
        if root_u != root_v: 
            A[root_v] = root_u 
            result += w
    return result

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    