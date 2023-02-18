def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    visit = [nodes[0]]
    global sum
    sum = 0
    def Prim(Visit, Nodes):
        global sum
        distance = 100
        for i in Visit:
            for j in Nodes:
                if j not in Visit:
                    x = i[0] - j[0]
                    y = i[1] - j[1]
                    if distance > (abs(x) + abs(y)):
                        distance = (abs(x) + abs(y))
                        Visitadd = j
        sum += distance
        Visit.append(Visitadd)
        if len(Visit) == len(Nodes):
            return sum
        else:    
            return Prim(Visit, Nodes)
                    
    Prim(visit, nodes)
    return sum

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22
    