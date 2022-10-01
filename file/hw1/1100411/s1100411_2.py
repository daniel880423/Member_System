def homework_1(nums): 
    len_lst = int(len(nums))
    count_lst = []   #建立空列表來存放連續次數
    count = 1
    for i in range(len_lst-1):
        
        if nums[i] == nums[i+1]: 
            count += 1   #連續相等計數增加
            if i+1 == len_lst-1:   #因為會超過列表範圍 所以最後一項在這裡計算
                count_lst.append(count)
        else:
            count_lst.append(count)   #不相等即連續斷開 新增計數到列表
            count = 1
        
    
    count_max = max(count_lst)   #找出計數列表最大值
    return count_max


    