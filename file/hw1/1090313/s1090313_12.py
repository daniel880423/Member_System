def homework_1(nums):
    max = 0
    count = 1
    for i in range(0,len(nums)-1): 
        if (nums[i] == nums[i+1]):
            count += 1 
            if count > max :
                max = count
        if (nums[i] != nums[i+1]):
            if count > max : 
                max = count
            count = 1
    return max

if __name__ == '__main__':
    lst = [10, 11, 54, 54, 21, 61, 61, 61, 12]
    print(homework_1(lst))


