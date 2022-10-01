def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l = len(nums)
    index = 0
    max = 0
    while index < l:
        total = 1
        tmp = nums[index]
        while True:
            index += 1
            if index >= l:
                break
            jud = nums[index]
            if jud == tmp:
                total += 1
            else:
                break
        if total > max:
            max = total
    return max

if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]

    print(homework_1(lst))
    