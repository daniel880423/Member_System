def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    i = 0   #i為lst的index
    length = len(lst)   #lst的長度
    step = 0    #所花的步數
    
    while i <= length-1:    #lst的index由0~length-1
        if (lst[i]%2 != 0):#先將當前的數變成偶數
            lst[i]+=1
            step+=1
        if (i>0)&(lst[i]<=lst[i-1]):    #將目前位置變成前一個位置的+2
            step+=(lst[i-1]-lst[i]+2)
            lst[i]=lst[i-1]+2
        i+=1
    
    return step

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    