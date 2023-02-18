def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l=len(lst)
    max=0
    sum=0
    for i in range(l):  #循環整個LIST
        if lst[i]>=max:   #判斷值是否大於等於最大值
            if lst[i]%2==0:  #判斷值是否為2的倍數
                max=lst[i]+2  #最大值+2(使得MAX更新到下個2的倍數)
            else:   #其他(不是2的倍數)
                lst[i]+=1   #值+1變2的倍數
                max=lst[i]+2   #最大值+2(使得MAX更新到下個2的倍數)
                sum+=1   #走1步
        else:    #其他(值小於最大值)
            n=max-lst[i]  #算值差多少
            lst[i]+=n  #值更新
            max=lst[i]+2  #最大值+2(使得MAX更新到下個2的倍數)
            sum+=n  #走N步
    return sum  #回傳步數
if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    