def homework_1(nums):   
    length=len(nums) 
    lst1=[] #創建空列表放置連續次數
    count=1
    for i in range(length-1): 
        
        
        if nums[i]==nums[i+1]: #若前項等於後項則次數加一
            count+=1
            if i == length-2: #若已計算至最後一項則直接加入列表
                lst1.append(count)
        else:
            lst1.append(count)
            count=1
    

    

    max_nums = max(lst1) #找出最大值
    return max_nums

    