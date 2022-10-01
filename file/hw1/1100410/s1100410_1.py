def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    check_num = nums[0]
    check_time = 1
    ans = 1
    for i in range(1,len(nums)):
        if nums[i] == check_num:
            check_time+=1
        else:
            check_num = nums[i]
            if check_time > ans:
                ans = check_time
            check_time = 1
    if check_time > ans:
        ans = check_time
    return ans

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    