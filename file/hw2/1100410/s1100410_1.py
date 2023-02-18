def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    ans = 0
    if lst[0]%2!=0: #如果第0項為奇數，加1
        lst[0]+=1   #將lst[0]的值直接修改+1
        ans+=1      #ans加1
    check = lst[0]  #設check為第1項

    for i in range(1,len(lst)):             #判斷第1項到最後一項
        if(lst[i]%2!=0 or lst[i]<=check):   #有兩種可能需要改數字，第1種是其值為奇數，第2種是他的值<=check的值
            if lst[i]<=check:               #如果是他的值<=check的值
                ans+=(check+2)-lst[i]       #ans加[check加2(比check大的最小偶數)-第i項的值]
                lst[i]=check+2              #將第i項修改為check加2(比check大的最小偶數)
                check = lst[i]              #將check改為修改後的第i項
                
            else:                           #如果是其值為奇數，且值大於前項的值
                ans+=1                      #ans加1
                lst[i]+=1                   #將此項修改為此項的值加1
                check = lst[i]              #將check改為修改後的第i項
    return ans                              #回傳ans

if __name__ == '__main__':
    lst = [2,2]
    print(homework_2(lst))
    