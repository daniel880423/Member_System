def homework_1(nums):
    Count = 1 # 計算連續次數
    Max = 1 # 計算「最大」連續次數
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]: # 兩兩一組做比對，若不同就將 Count 重設為 1
            Count = 1
        else: # 若相同則 Count + 1
            Count += 1
        if Max < Count: # 更新 Max 的數值
            Max = Count
    return Max