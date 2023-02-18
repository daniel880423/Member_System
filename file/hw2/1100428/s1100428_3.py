def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    if lst[0] % 2 != 0:                     #第一位數不等於0 
        lst[0] += 1                         #讓他變成偶數
        count += 1                          #步數+1
    for i in range(1,len(lst)):
        if lst[i] <= lst[i-1]:              #(第二項開始)在後項比前項小的狀況下
            count += lst[i-1] + 2 - lst[i]  #步數=後項-前項
            lst[i] = lst[i-1] + 2           #後項=前項的數+2

        elif lst[i] %2 != 0:                #在後項比前項大的狀況且不為偶數 
            lst[i]+=1                       #將之變為偶數
            count+=1                        #步數+1

    return count

if __name__ == '__main__':
    lst = [37, 28, 20]
    print(homework_2(lst))
    