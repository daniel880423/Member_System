def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    m = 0
    c= 1
    nums.append(None)
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            c+=1
        else:
            m = max(m, c)
            c=1
    return(m)

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    