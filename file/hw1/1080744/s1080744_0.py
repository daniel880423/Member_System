def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    count=1
    max_count=1
    
    for i in range(1,len(nums)):
        
        if nums[i]==nums[i-1]:
            count+=1  
        else:
            if max_count<count:
                max_count=count
                count=1
            else:
                count=1
    if max_count<count:
        max_count=count
     
    return max_count

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    