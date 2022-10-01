def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    time = len(nums)
    index = 0
    count = 0
    max = 0
    while index < time-1:
        n = nums[index]
        m = nums[index+1]
        if n == m:
            count +=1
            index +=1
        else:
            count = 0
            index +=1
        if count > max:
            max = count
    
    return max+1








if __name__ == '__main__':
    lst = [0,0,1,1,1,1,1,1,1,0,0,0,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,]
    print(homework_1(lst))
    