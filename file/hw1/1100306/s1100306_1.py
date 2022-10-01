def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    len_nums = len(nums)
    n = 0
    max_count = 1
    while n <  len_nums-1:
        count = 1
        for i in range(n,len_nums-1):
            if nums[n] != nums[i+1]:
                break
            count += 1
        if max_count < count: 
                    max_count = count
        n += 1    

    return max_count


if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    