def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 1
    i = 0
    j = 0
    max_n = 1
    for i in range(len(nums)-1):
        
        if nums[i] == nums[i+1]:
            count += 1
            j = count
            if j>max_n:
                max_n=j 
        else :
            count = 1
        
    return max_n

if __name__ == '__main__':
    lst = [-1, 1, 1, 0, 1, -1, 1, 0, 0, 0, 0, 1, 1, -1, 1, 0, 0, -1, -1, 0, 1, 0, -1, -1, 1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, -1, 0, 0, 0, 0, -1, -1, -1, 0, 1, 0, 1]
    print(homework_1(lst))
    
