def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count=0                    #建立一個count函數計算總共花了幾步達成目標
    if lst[0]%2 != 0:          #假設lst中的第一個函數值除二取餘數不等於0表示他是奇數  
        lst[0]+=1              #將奇數變成偶數
        count = 1              #步數+1
    for i in range(1,len(lst)):  #建立for迴圈檢查所有元素
        if lst[i]<=lst[i-1]:     #如果後項的值小於前項
            count = count + lst[i-1] + 2 - lst[i] #步數要加上大數減小數再加上2
            lst[i] = lst[i-1]+2  #並改變元素值
        if lst[i]%2 != 0:       #如果改變後的元素值為奇數
            lst[i]+=1           #將它變成偶數
            count += 1          #步數+1







    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    