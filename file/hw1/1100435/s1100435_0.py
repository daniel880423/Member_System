def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max = 0
    lens = len(nums)
    i = 0
    while i < lens and (lens-i)>max:
        x = nums[i]
        count = 1
        i+=1
        while i < lens and nums[i] == x:
            count+=1
            i+=1
        if count > max:
            max = count
    return max

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    