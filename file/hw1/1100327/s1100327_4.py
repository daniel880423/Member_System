def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    now=nums[0]#用now儲存第一個的數字
    times=0#出現次數
    maxt=0
    for i in nums:
        if now == i:#若now與i相同 times+1
            times+=1
        else:
            times=1
            now=i
        if times>maxt:
            maxt=times
    return maxt
            
            








 

if __name__ == '__main__':
    lst = [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]
    print(homework_1(lst))
    