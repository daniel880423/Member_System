def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    class DisjointSet:
        def __init__(self, elements):
            self.parents = [nodes for nodes in elements]
            self.count = len(self.parents)
        
        def find(self, element):
            nodes = self.parents[element]
            while self.parents[nodes] != nodes:
                nodes = self.parents[nodes]
            return nodes
        
        def union(self, u, v):
            u = self.find(u)
            v = self.find(v)
            if u != v:
                self.parents[u] = v
                self.count -= 1

        def __len__(self):
            return self.count



    

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    