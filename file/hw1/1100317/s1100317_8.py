def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l = len(nums)
    max = 0
    n = 1
    for i in range(0,l-1):
        if nums[i]==nums[i+1]:
            n+=1
            if i==l-2 and n>max:
                max = n
        else:
            if n>max:
                max = n
                n=1
            else:
                n=1
    return max

if __name__ == '__main__':
    lst =   [10, 11, 54, 54, 21, 61, 61, 61, 12, 1000, 100, 1000, 1000, 1000, 1000, 999, 999, 999]	

    print(homework_1(lst))