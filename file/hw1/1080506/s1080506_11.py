def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 1
    max = 1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            count +=1
            if max < count:
                max = count
        else:

            count =1
    return max

if __name__ == '__main__':
    lst =   [1,1,1,2,2]
    print(homework_1(lst))
    