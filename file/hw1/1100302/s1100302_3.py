def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    time = len(nums)
    index = 0
    count = 0
    max = 0
    while index < time:
        try:
            n = nums[index]
            m = nums[index+1]
        except:
            break
        if n == m:
            count +=1
            index +=1
        else:
            count =0
            index +=1
        if count > max:
            max = count 

    return max+1

if __name__ == '__main__':
    lst =  [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))