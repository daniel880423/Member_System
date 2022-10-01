def homework_1(nums): 
    m = 0
    c= 1
    for i, j in zip(nums[0:-1:], nums[1::]):
        if i == j:
            c+=1
        if i !=j:  
            m = max(m, c)
            c=1
        else:
            m = max(m, c)          
    return(m)
if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    