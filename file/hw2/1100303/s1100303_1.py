def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step=0    #將增加步數設為0
    pre=0     #前一個數字設為0
    if lst[0]%2!=0:  #如果地一個數不為偶數
        lst[0]+=1    #加一變成偶數
        step+=1      #步數加1
    for i in range(1,len(lst)): #查看lst裡的數
        if lst[i]%2!=0:     #若不為偶數
            if lst[i]<lst[i-1]:  #若比前一個數小
                pre=lst[i]
                lst[i]=lst[i-1]+2   #現在的數變為前一個數遞增偶數的最小值
                step+=(lst[i]-pre)  #改變步數值
            if lst[i]>lst[i-1]:  #若比前一個數大
                if lst[i]%2!=0:
                    lst[i]+=1
                    step+=1
        else:    #為偶數
            if lst[i]<lst[i-1]:  #比前一個數小
                pre=lst[i]
                lst[i]=lst[i-1]+2
                step+=(lst[i]-pre)
            if lst[i]==lst[i-1]:   #和前一個數相等
                lst[i]+=2          #變為遞增偶數
                step+=2
            if lst[i]>lst[i-1]:   #比前一個數大
                continue
            else:
                continue
    return step

if __name__ == '__main__':
    lst =  [1,5,2,7,4]

    print(homework_2(lst))
    