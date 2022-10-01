def homework_1(nums): 
    max = 1                                               
    count = 1
    c = len(nums)
    for i in range(c-1):                       #讀取nums
        if nums[i] == nums[i+1]:               #判斷若是一樣加一
            count +=1
        else:                    
            if count>max:                      #不一樣判斷跟最大值大小，若大則max變count
                max = count
                count = 1
            count =1
    if count >max:
        max = count
        
  
    return max








    

if __name__ == '__main__':
    lst = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    print(homework_1(lst))
    