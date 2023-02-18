def homework_2(lst): 
    #lst=list[int]
    length=len(lst)
    mini=0
    for i in range(length-1):
        if lst[i]%2!=0:
            lst[i]+=1
            mini+=1
        if lst[i+1]>lst[i]:
            d1=lst[i+1]-lst[i]
            if (d1)%2 !=0:
                lst[i+1]+=1
                mini+=1
            if (d1)%2 ==0:
                lst[i+1]=lst[i+1]
            
        if lst[i+1]<lst[i]:
            d2=lst[i]-lst[i+1]
            lst[i+1]=lst[i+1]+d2+2
            mini=mini+d2+2
        if lst[i+1]==lst[i]:
            lst[i+1]+=2
            mini+=2
        
           
    return mini

if __name__ == '__main__':
    lst = [2,4,6,8]
    print(homework_2(lst))
    