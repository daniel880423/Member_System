def homework_2(lst):                           
    c = len(lst)                                # 計算陣列中有幾個元素     
    sum = 0                                     # 計算步數
    for i in range (c):                         # 利用for迴圈來執行
        if i == 0:                              # 計算第一個元素所走的步數
            if (lst[i] % 2) == 0 :              # 如果第一個元素為偶數
                lst[i] = lst[i]      
            else:                               # 如果第一個元素為奇數
                lst[i] = lst[i]+1   
                sum = sum + 1       
        else:    
            if lst[i] > lst[i-1] :              # 如果現在的元素大於前一個元素
                if (lst[i] % 2) == 0 :          # 如果元素為偶數
                    lst[i] = lst[i]  
                else:
                    lst[i] = lst[i]+1           # 如果元素為奇數
                    sum = sum + 1 
            elif lst[i] <= lst[i-1] :           # 如果現在的元素小於或等於前一個元素
                if (lst[i-1] % 2) == 0 :        # 如果元素為偶數
                    lst[i-1] = lst[i-1]+2
                    sum = sum+lst[i-1]-lst[i]
                    lst[i] = lst[i-1]               
                else:                           # 如果元素為奇數
                    lst[i-1] = lst[i-1]+1
                    sum = sum + lst[i-1]-lst[i]
                    lst[i] = lst[i-1]           
    return sum                                  # 回傳總步數

if __name__ == '__main__':
    lst = [1,2]
    print(homework_2(lst))
    