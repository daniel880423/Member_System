def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max_count = 1
    count = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            if count > max_count:
                max_count = count
            count = 1
        else:
            count += 1
    if count > max_count:
        max_count = count
    return max_count
if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    from capital_measurement import hw1_In
    print(homework_1(lst))
    