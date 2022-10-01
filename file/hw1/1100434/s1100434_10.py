def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    max = 1
    count = 1

    for i in range(len(nums)):
        if i==(len(nums)-1):
            break
        x = nums[i]
        if x == nums[i+1]:
            count+=1
            a = count
            if a > max:
                 max = a  
        else:
            count = 1
          
        
    return max

if __name__ == '__main__':
    lst = [0, 0, 1, 1, 1, 1, 0, 0, 0, 1]
    print(homework_1(lst))
    