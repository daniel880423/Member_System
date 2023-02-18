def homework_6(nodes): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # 請使用 Prim Algorithms / Kruskal Algorithms
    answer = 0
    AD = nodes[0]
    SUP = [AD]
    nodes.remove(AD)
    while(nodes): #當nodes節點未連接
        distance = 200 
        for R in nodes: #在未接過的節點中選出
            for AD in SUP: #選一個AD與R連接 
                if abs(AD[0]-R[0])+abs(AD[1]-R[1]) < distance: 
                    distance = abs(AD[0]-R[0])+abs(AD[1]-R[1]) 
                    minR = R #連接節點最短距離的R
        SUP.append(minR) #將要連接的R放入SUP   
        nodes.remove(minR) #將已連接的R移出nodes
        answer+=distance
    return answer

if __name__ == '__main__':
    nodes = [[0,0],[2,6],[3,9],[6,4],[7,1]]
    print(homework_6(nodes))
    # 22