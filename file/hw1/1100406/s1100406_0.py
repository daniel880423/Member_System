from re import A


def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    a = len(nums) #驗測資長度
    b=a-1 #修正長度
    cou=1 #連續出現次數計數器
    countlist=0 #計數器儲存器
    for i in range(0,b): #驗證前後是否相同，若相同，則計數器+1，否則將值存入計數器儲存器，並還原計數器
        c  = nums[0]
        d = nums[1]
        print("c=",c)
        print("d=",d)
        
        if c == d:
            cou=cou + 1
            print("cou=",cou)
        else:
            if cou>countlist:
                countlist = cou
            cou =1
            print("cou=",cou,"countlist=",countlist)

        del nums[0] #將用過的側資刪除
        print(nums)
 
    if cou>countlist: #驗證計數器和儲存器之值的大小，取大者回傳
        countlist = cou
    else :
        cou=countlist
    print("cou=",cou,"countlist=",countlist)    
    
    return cou #回傳資料


if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    