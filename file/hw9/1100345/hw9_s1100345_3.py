def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    L = len(items)
    global ans
    ans = 0

    def DFS(index, sumW, sumP):
        global ans
        if index == L:
            if sumW <= bag_size and sumP > ans:
                ans = sumP
            return
        DFS(index+1, sumW+items[index][0], sumP+items[index][1])
        DFS(index+1, sumW, sumP)
        
    DFS(0, 0, 0)

    return ans

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    