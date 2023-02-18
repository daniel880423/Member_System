def homework_6(nodes):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    global sum
    visited_Node = [nodes[0]]  # 走過的NODE 先假設NODE[0]為開頭
    sum = 0

    def Prim(visited_Node, Nodes):
        distance = float("inf")  # 宣告距離變數為無限大
        global sum, Visited
        for i in visited_Node:
            for j in Nodes:  # 算走過的NODE與每個NODE
                if j not in visited_Node:  # 不走已經走過的NODE
                    distance_x = i[0] - j[0]  # 算距離
                    distance_y = i[1] - j[1]
                    if distance > (abs(distance_x) + abs(distance_y)):
                        distance = (abs(distance_x) + abs(distance_y))  # 最短路徑長
                        Visited = j  # 最短路徑長的NODE
        visited_Node.append(Visited)  # 把路徑最短的點紀錄進走過的NODE
        sum += distance
        if len(Nodes) == len(visited_Node):  # 若走過的NODE的總數 = NODE的總數 回傳值
            return sum
        else:  # 否則繼續執行下個NODE
            return Prim(visited_Node, Nodes)

    Prim(visited_Node, nodes)
    return sum


if __name__ == '__main__':
    nodes = [[0, 0], [2, 6], [3, 9], [6, 4], [7, 1]]
    print(homework_6(nodes))
    # 22