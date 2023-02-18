def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    L = len(items)
    global ans
    ans = 0

    def DFS(index, sumW, sumP):
        global ans
        print(index, sumW, sumP)
        if index == L:
            if sumW <= bag_size and sumP > ans:
                ans = sumP
                print(ans)
            return
        DFS(index+1, sumW+items[index][0], sumP+items[index][1])
        DFS(index+1, sumW, sumP)
        
    DFS(0, 0, 0)

    return ans

if __name__ == '__main__':
    bag_size = 5
    items =  [[1,45],[2,100],[3,130],[1,80],[5,220],[5,200],[1,110]]
    print(homework_9(bag_size, items))
    # 155