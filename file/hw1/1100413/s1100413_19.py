def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py).
    maxcon = 1
    lenlst = len(nums)
    stay =0
    nums.append(None)

    for i in range(lenlst):
        
        if maxcon>stay :
            stay = maxcon
        if nums[i] == nums[i+1]:
            maxcon +=1
        else:           
            maxcon = 1


    return stay

if __name__ == '__main__':
    #lst = [0,0,1,1,1,1,0,0,0,1]
    lst = [1, 2, 2, 2, 3, 5, 2, 2, 4, 4, 4, 1, 1, 1, 1, 1]
    print(homework_1(lst))
    