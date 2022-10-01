def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(nums) == 0:
        return 0
    temp = nums[0]
    count = 0
    max = 0
    for i in nums:
        if temp == i:
            count = count +1
            
        else:
            count = 1
            temp = i
        if max<=count:
            max = count
                
            







    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    
    print(homework_1(lst))
    