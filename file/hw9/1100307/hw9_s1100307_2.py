
def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    global maxx 
    maxx = 0
    def DFS(size,price,visit,ii):
        global maxx
        if price>maxx:
            maxx = price
        for i in range(ii,len(items)):
            if i not in visit and size <= bag_size:
                if (size + items[i][0])>bag_size:
                    continue
                DFS(size + items[i][0],price+items[i][1],visit+[i],i)
    DFS(0,0,[],0)
    return maxx
if __name__ == '__main__':
    bag_size = 25
    items = [[1, 108], [4, 129], [2, 113], [5, 62], [8, 194], [6, 61], [7, 51], [4, 110], [6, 198], [1, 194], [7, 85], [3, 87], [3, 129], [3, 117], [1, 112]]
    print(homework_9(bag_size, items))
    # 155
    