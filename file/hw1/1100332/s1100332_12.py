def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(nums) > 1000 or len(nums) <3:  #檢查list大小
        return "error"
    else:
        #for i in nums:   #檢查數字是否符合規定
            #if (type(i) is not int) or (abs(i) > 10000):
                #return "error"
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
a=[0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(homework_1(a))
    