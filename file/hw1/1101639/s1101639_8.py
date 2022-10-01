import numbers

def homework_1(nums):
    x = len(nums) #算數量
    index = 0
    count = 0
    max = 0
    while index < x-1:
        if nums[index] == nums[index+1]:#前後兩個一樣就繼續算
            count += 1
            index += 1
        else:
            count = 0 
            index += 1
        if count > max :
            max = count
    return max+1

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]


    print(homework_1(lst))
    