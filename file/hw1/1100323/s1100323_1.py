def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    x = len(nums) #先算數量
    index = 0
    count = 0
    max = 0
    while index < x-1:
        if nums[index] == nums[index+1]:#前後兩個一樣的話就繼續算
            count += 1
            index += 1
        else:
            count = 0 
            index += 1
        if count > max :
            max = count
    return max+1








    return 

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    