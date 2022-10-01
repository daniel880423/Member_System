def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max = 1
    test_item = nums[0]
    count = 1
    count_2 = 1
    for i in nums[1::]:
        if i == test_item:
            count+=1
        else:
            test_item = i
            count_2 = count
            count = 1
 
        if max < count_2 :
            max = count_2
        elif max < count :
            max = count
    return max




if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    