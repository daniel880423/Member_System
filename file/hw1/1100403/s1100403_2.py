from re import A


def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    
    a = nums[0] 
    n = 1  
    max = 1 
    for i in nums[1:]:  
        if i == a:  
            n+=1
            if n>max:   
                max = n
        else:
            a = i   
            n = 1   

    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    