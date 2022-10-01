def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    now=nums[0]#用now儲存第一個的數字
    times=0#出現次數
    maxt=0
    for i in nums:
        if now == i:#若now與i相同 times+1
            times+=1
        else:
            if times>=maxt:
                maxt=times
                times=1
                now=i
            else: 
                times=1
                now=i 
    if maxt<=times:maxt=times        
    return maxt
            
            








 

if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    