def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    appear_times = 0
    max_times = 0
    pre_number=nums[0]
    for i in nums:
        if(i == pre_number ):
            appear_times += 1
            max_times = max(appear_times,max_times)
        else:
            appear_times = 1
            pre_number = i


    return max_times



if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    