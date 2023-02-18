def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    times = 0                                             #設初始步數為0          
    index=0                                               
    pre_num = lst[index]                                  #設lst中的第一個數為pre_num
    for i in lst:                                         #從lst頭開始判斷
        if i < pre_num:                                   #如果新的數大於前一個數
            times += pre_num + 2 - i                      #加所需步數
            i = pre_num + 2                               #將新的數改為大於前一個數的偶數
        else:
            if i%2 != 0 and i >= pre_num:                 #如果新的數為基數且大於等於前一個數
                times += 1                                #加所需步數
                i += 1                                    #將新的數改為大於前一個數的偶數
            elif  index != 0 and i%2 == 0 and i == pre_num: #如果新的數為偶數且等於前一個數(不判斷第一個數)
                times += 2                                #加所需步數
                i += 2                                    #將新的數改為大於前一個數的偶數
        index += 1
        pre_num = i                                       #更新前一個數的值



    return times

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    