
def homework_2(lst): 
    c = 0 
    len_lst= len(lst)
    if lst[0]%2!= 0:  
        lst[0]=lst[0]+1
        c=1  
    for i in range(0,len_lst-1):
        if lst[i]>=lst[i+1]: #前>=後
            if lst[i]%2==0:  #lst[i]是偶數
                pre = lst[i+1]
                lst[i+1]= lst[i]+2
                c= lst[i+1]-pre+c
                continue
            else:         #lst[i]是奇數
               pre = lst[i]
               lst[i+1]=lst[i]+1
               c=lst[i+1]-pre+c
               count+=1
               continue
        
        if lst[i+1]>lst[i]: #後比前大
            if lst[i+1]%2 !=0:   #基數
                lst[i+1]= lst[i+1]+1
                c= c+1
                continue
    return c






if __name__ == '__main__':

    lst = [1,1,1]
    print(homework_2(lst))
    