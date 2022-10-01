def homework_1(nums):
    maxtime = 0      #最高連續次數
    ct = 1           #目前連續次數
    for i in range(1,len(nums)):    
        if nums[i] == nums[i-1]:    #如果連續
            ct += 1
            maxtime = max(maxtime, ct)  #更新最大連續次數 
        else:
            maxtime = max(maxtime, ct)  #更新最大連續次數
            ct = 1
    return maxtime            
if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    #print(homework_1(lst))

    