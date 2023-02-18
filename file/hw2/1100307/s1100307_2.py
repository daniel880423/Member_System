def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans = 0
    if (lst[0]%2)!=0:                          #看第一個是不是偶數
        lst[0]+=1
        ans+=1
    for i in range(1,len(lst)):                #一個一個拿出來檢查
        if lst[i]<=lst[i-1]:                   #如果比較少
            ans+=lst[i-1]+2-lst[i]             #加上他們的差距加2
            lst[i]=lst[i-1]+2                  #把它變成比上一個大2
            continue
        if (lst[i]%2)!=0:                      #如果比較大直街判斷是否為偶數
            lst[i]+=1                          #不是的話加一遍偶數
            ans+=1
    








    return ans

if __name__ == '__main__':
    lst = [13, 22, 4, 29, 46, 22, 29, 36]
    print(homework_2(lst))
    