def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    a = 0           #將步驟數設為a
    l = len(lst)     #算出lst長度
    if lst[0] // 2 != 0:  #如果lst[0]是不是偶數
        lst[0] = lst[0] +1   #lst[0] + 1
        a += 1               #步驟加1  
    for i in  range(1,l):     #檢查lst[1]-lst[l-1]
        while lst[i]<lst[i-1]:     #如果小於等於前一個
            lst[i] += 1            #lst[i] +1 
            a += 1                 #步驟跟著加1  
        if lst[i] // 2 != 0:       #大於前一個後檢查是否為偶數
            lst[i] = lst[i] + 1
            a+= 1

   



    return a              #輸出a

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    