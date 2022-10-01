def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max_time = 1       #設
    fstnum = nums[0]
    times = 1
    for i in nums[1::]:
        if i == fstnum:
            times+=1
            if times> max_time:
                max_time = times
        else:
            fstnum = i
            times = 1
    return max_time


if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    