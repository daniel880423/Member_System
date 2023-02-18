import copy
def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    size = [] #先將價錢與重量分開，但不交換位置
    price = []
    for i in range(len(items)):
        size.append(items[i][0])
        price.append(items[i][1])
    
    def backtrack(start_index,bag_size,nprice,visit): #backtracking
        if bag_size == 0 or start_index==len(size):             #如果袋子重量=0或到了葉節點
            res.append(copy.deepcopy(visit))                    #則將經過的重量記錄在res裡面
            return 
        for i in range(start_index,len(size)):                  #從第一個開始找
            if size[i] <= bag_size:
                nprice+=price[i]                                #將此物品的價值加入這次的總價值
                visit.append(price[i])                          #記錄經過的點
                
                backtrack(i+1,bag_size-size[i],nprice,visit) #將起始位置加一，袋子重量減物品重量後迭代
                visit.pop()                                     #還原記錄點
            
    res=[]
    start_index = 0
    max_price = 0
    nprice = 0
    visit=[]
    backtrack(start_index,bag_size,nprice,visit)
    total = []
    for i in range(len(res)):
        total.append(sum(res[i]))
    return max(total)

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    