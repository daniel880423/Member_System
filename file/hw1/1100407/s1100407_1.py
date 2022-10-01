def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max = 0
    i = 0
    while i < len(nums) and (len(nums)-i)>max:
        count = 1
        while i+1 < len(nums) and nums[i+1] == nums[i]:
            count+=1
            i+=1
        i+=1
        if count > max:
            max = count
    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    