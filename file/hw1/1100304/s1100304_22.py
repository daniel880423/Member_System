def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count1 = 1  #紀錄連續的數字次數
    count2 = 0  #保留連續數字的最大次數
    for n in range(0,len(nums)-1):
        if nums[n+1] == nums[n]:  #若連續出現一次 ==> count1 加一
            count1 += 1
        else:  #若不連續
            if count1 > count2:  #count2保留count1的值
                count2 = count1
                count1 = 1  #count1重新計算新的連續數
            else:
                count1 = 1  #count1重新計算新的連續數
    if count1 > count2:  #最後一段連續數與之前出現的連續數比較
        count2 = count1
  
    return count2

if __name__ == '__main__':
    lst = [-1,2,2,2,3,5,-2,2,4,4,4,-1,-1,-1,1,1]
    print(homework_1(lst))
    
    