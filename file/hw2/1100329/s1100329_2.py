def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step=0                                      #預設步數為0   
    for i in range(len(lst)):                   #按照lst長度跑入迴圈   
        if i==0 :                               #如果i=0，進入(lst首位數)
            if lst[i]%2!=0:                     #如果首位數為奇數，進入
                lst[i]=lst[i]+1                 #將奇數加一
                step+=1                         #步數加一
        else:
            if lst[i]<lst[i-1]:                #如果lst現在位置比前一個位置的數值還小，進入
                step=step+lst[i-1]-lst[i]+2    #原有步數加上差距的步數並加上偶數2
                lst[i]=lst[i-1]+2               #前一個位置的數值加偶數2後，複製給現在位置的數值
            elif lst[i]==lst[i-1]:              #如果現在位置的數值=前一個位置的數值
                step+=2                         #步數加2
                lst[i]+=2                       #現在位置的值加上偶數2
            else:
                if lst[i]%2!=0:                 #如果現在的為奇數，進入
                    lst[i]=lst[i]+1             #將現在的奇數+1變成偶數
                    step+=1                     #步數加一
    return step                                 #回傳總步數


if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    