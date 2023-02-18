def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step = 0     #紀錄步數
    if lst[0] % 2 != 0:     #第一個數字若為奇數
        lst[0] += 1     #變偶數
        step += 1     #紀錄步數
    else:
        step = 0     #第一個數字若為偶數則不動

    for i in range(1,len(lst)):     #從第二個數字開始比
            if lst[i] <= lst[i-1]:     #若i <= 前一個數字
                i_ex = lst[i]     #i_ex:保留當前數字i
                lst[i] = lst[i-1] + 2     #i變為 比前一數字大且為偶數
                step += lst[i] - i_ex     #紀錄i的步數
            elif (lst[i] > lst[i-1]) & (lst[i] % 2 != 0):     #若i > 前一個數字 & 為奇數
                lst[i] += 1     #變偶數
                step += 1     #紀錄步數
                
    return step

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    