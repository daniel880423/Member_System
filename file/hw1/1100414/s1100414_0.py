def homework_1(nums): 
    length=len(nums)
    count=1
    Max=list()
    for i in range(length):
        if i==length-1:
            Max.append(count)
            break
        a=nums[i]
        b=nums[i+1]
        
        if a==b:
            count+=1
        else:
            Max.append(count)
            count=1
            
            
        
            
    return max(Max)



     

    

if __name__ == '__main__':
    lst = [1, 2, 2, 2, 3, 5, 2, 2, 4, 4, 4, 1, 1, 1, 1, 1]
    print(homework_1(lst))