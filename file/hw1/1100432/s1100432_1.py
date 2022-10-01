def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    i = 0
    counter1 = 0
    counter2 = 0
    a = len(nums)#先算list裡面元素數量
    for i in range(0,a):
        try:
            n = nums[i]
            m = nums[i+1]
        except:
            break    
        if n == m:
            counter1+=1
        else:
            counter1 = 0
        if counter1 > counter2:
            counter2 = counter1    
    return counter2+1

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))