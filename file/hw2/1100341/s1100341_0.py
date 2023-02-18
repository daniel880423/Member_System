def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    s = 0            #步數=0
    l = len(lst)     
    a = 0            #設一個a把原本的lst[i]暫放進去
    if lst[0] // 2 != 0:  #第一個不是偶數的話
        lst[0] += 1       #就+1變偶數
        s += 1            #步數跟著+1
    for i in range(1, l):
        if lst[i] <= lst[i-1]:   #後一個比前一個小於等於的話
            a = lst[i]           #先把原本的lst[i]放進a
            lst[i] += lst[i-1]   #把後一個+前一個讓後一個比前一個大
            s = lst[i] - a       #算加了多少步數 用加前一個的-原本的lst[i]
            if lst[i] // 2 != 0: #看加前一個後的是不是偶數
                lst[i] += 1      #加1變偶數
                s += 1           #步數也+1
            

                







    return s

if __name__ == '__main__':
    lst = [1, 1, 1]
    print(homework_2(lst))
    