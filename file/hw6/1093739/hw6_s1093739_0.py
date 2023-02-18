def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    import math

    P=[]
#設定初始化參數 P=[1,2,3,4,5]
    for i in range(1,len(nodes)+1):
        P.append(i)

    edges = []
#算距離並建構節點間的距離
    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            x_distance = abs(nodes[i][0] - nodes[j][0])
            y_distance = abs(nodes[i][1] - nodes[j][1])
            edges.append ( [ i, j,x_distance + y_distance,] )



    class DisjointSet:

        def __init__(self, element_num=None):
            self._father = {}
            self._rank = {}
        # 初始化時每個元素單獨成為一個集合
            if element_num is not None:
                for i in range(element_num):
                    self.add(i)

        def add(self, x):
        # 添加新集合
        # 如果已經存在則跳過
            if x in self._father:
                return 
            self._father[x] = x
            self._rank[x] = 0

        def _query(self, x):
        # 如果father[x] == x，說明x是樹根
            if self._father[x] == x:
                return x
            self._father[x] = self._query(self._father[x])
            return self._father[x]
    
        def merge(self, x, y):
            if x not in self._father:
                self.add(x)
            if y not in self._father:
                self.add(y)
        # 查找到兩個元素的樹根
            x = self._query(x)
            y = self._query(y)
        # 如果相等，說明屬於同一個集合
            if x == y:
                return
        # 否則將樹深小的合並到樹根大的上
            if self._rank[x] < self._rank[y]:
                self._father[x] = y
            else:
                self._father[y] = x
            # 如果樹深相等，合並之後樹深+1
                if self._rank[x] == self._rank[y]:
                    self._rank[x] += 1

    # 判斷是否屬於同一個集合
        def same(self, x, y):
            return self._query(x) == self._query(y)


    disjoinset = DisjointSet(8)
# 根據邊長對邊集排序
    edges = sorted(edges, key=lambda x: x[2])
    res = 0
    for u, v, w in edges:
        if disjoinset.same(u ,v):
            continue
        disjoinset.merge(u, v)
        res += w
    return res






    

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    