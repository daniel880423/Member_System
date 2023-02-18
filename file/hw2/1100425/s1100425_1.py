def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step = 0                  #步數
    if lst[0] % 2 == 1:       #先用除以2的餘數判斷第一項是奇數還是偶數
        lst[0] = lst[0] + 1
        step = step + 1

    for i in range(1, len(lst)):    
        while (lst[i] % 2 == 1 or lst[i] <= lst[i - 1]):  #利用while，重複執行+1，直到當下的數字符合偶數和比前一項大的條件 
            lst[i] = lst[i] + 1                            
            step = step + 1     #計算+1的次數

    return step

if __name__ == '__main__':
    lst =  [1,1,1]
    print(homework_2(lst))
    