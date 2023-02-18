def homework_2(lst): 
    num=0
    if lst[0]%2!=0:             #判斷lst[0]偶數
            lst[0]+=1           
            num+=1
    for i in range(1,len(lst)): 
        if lst[i]<=lst[i-1]:    #判斷i是否小於等於i-1
            tmp=lst[i]
            lst[i]=lst[i-1]+2   #前一個已經是偶數所以前一個+2
            num+=lst[i]-tmp
        elif lst[i]%2!=0:       ##判斷lst[0]偶數
            lst[i]+=1
            num+=1 
    return num

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))