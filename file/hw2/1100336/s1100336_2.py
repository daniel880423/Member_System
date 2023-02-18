def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    step=0    #設一個算步數的變數
    tmp=0    #先設一個可以存數字的變數(一剛開始先射程0，不然開頭比較時可能會出問題)
    for i in lst:  
        if (i%2)!=0:   #如我lst取的數，除2有餘數
            i+=1    #先把從lst取出的數+1
            step+=1      #步數也+1
            
        if tmp==i:   #如果上一個數字和這次從lst取出的數一樣的話
            i+=2   #把這個從lst取出的數+2
            step+=2  #step也+2
        if tmp>i:   #如果這次從lst取出的數<上一個存的數
            x=i   #把這次取出的數存在另一個變數
            i=tmp+2  #把這次去出的數設為上一個數+2
            step=step+i-x  #把多的步數加進step
            
        tmp=i  #把這次取的數(已更改過的)射程tmp(也就是下一輪的上一個數)
            




    return step

if __name__ == '__main__':
    #lst = [1,1,1]
    #lst=[2,4,6,8]
    #lst = [1,5,2,7,4]
    #lst=[1,2]
    lst=[3]

    print(homework_2(lst))
    