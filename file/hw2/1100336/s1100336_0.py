def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    step=0    #設一個算步數的變數
    for i in range(len(lst)-1):  
        if (lst[i]%2)!=0:   #如我lst取的數，除2有餘數
            lst[i]+=1    #先把從lst取出的數+1
            step+=1      #步數也+1
        if lst[i+1]<=lst[i]:   #如果下一個數小於或等於這次取的數
            next_lst_store=lst[i+1]   #先把原本取的下一個數用另一個變數存起來
            lst[i+1]=lst[i]+2      #把下一個數上一個數+2(這是應付下一個數小於或等於的情況)
            step=step+(lst[i+1]-next_lst_store) #把step在加上更新後的下一個數與原本下一個數的數字差距



    return step

if __name__ == '__main__':
    lst = [1,1,1]
    #lst=[2,4,6,8]
    #lst = [1,5,2,7,4]
    lst=[1,2]

    print(homework_2(lst))
    