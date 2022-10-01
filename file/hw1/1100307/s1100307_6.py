def homework_1(nums): 
    a = 1                                               
    b = 1
    for i in range(len(nums)-1):                       #讀取nums
        if nums[i] == nums[i+1]:               #判斷若是一樣加一
            b +=1
        else:                    
            if b>a:                      #不一樣判斷跟最大值大小，若大則max變count
                a = b
            b =1
    if b > a:
        a = b
    return a








    

if __name__ == '__main__':
    lst = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    print(homework_1(lst))
    