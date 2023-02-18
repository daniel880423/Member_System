def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    step=0    #設一個算步數的變數
    tmp=0
    for i in lst:  
        if (i%2)!=0:   #如我lst取的數，除2有餘數
            i+=1    #先把從lst取出的數+1
            step+=1      #步數也+1
            
        if tmp==i:
            i+=2
            step+=2
        if tmp>i:
            x=i
            i=tmp+2
            step=step+i-x
            
        tmp=i
            




    return step

if __name__ == '__main__':
    #lst = [1,1,1]
    #lst=[2,4,6,8]
    #lst = [1,5,2,7,4]
    #lst=[1,2]
    lst=[3]

    print(homework_2(lst))
    