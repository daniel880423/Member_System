def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    
    c=1
    max=1
    for i in range( len(nums)-1):
        if nums[i] == None:
            break
        if nums[i] == nums[i+1]:
            c+=1
            continue
        if c>max:
            max = c
        c=1







    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))

    

