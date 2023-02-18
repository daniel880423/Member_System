def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    num = len(items)                                                                                                #先找出有幾個物品
    weight = []
    value = []                                                                                                      #建立兩個空list來存放重量和價值                                                   
    for i in range (num):                                              
        weight.append(items[i][0])                                                                                  #將重量放進list
    for i in range (num):
        value.append(items[i][1])                                                                                   #將價值放進list

    ans = (knapSack(bag_size, weight, value, num))                                                                  #將答案回傳給ans並輸出
    return ans
def knapSack(bag_size, wt, val, num):
    
    if num == 0 or bag_size == 0:                                                                                   #假設背包空間是0代表放不下任何物品，沒有任何物品可都也沒辦法取得任何價值，則回傳0
        return 0

    if (wt[num-1] > bag_size):                                                                                      #如果重量直接超過背包承重，則直接看下一個物品
        return knapSack(bag_size, wt, val, num-1)
 
    else:
        return max(val[num-1] + knapSack(bag_size-wt[num-1], wt, val, num-1),knapSack(bag_size, wt, val, num-1))   #如果重量不超過背包承重則考慮兩種情況，放進背包，和不放進背包，取最大值回傳即是最佳解

 


 
if __name__ == '__main__':
    bag_size = 5
    items =  [[1,45],[2,100],[3,130],[1,80],[5,220],[5,200],[1,110]]
    print(homework_9(bag_size, items))

    # 155