def homework_2(lst): 
    num=0
    if lst[0]%2!=0:
            lst[0]=lst[0]+1
            num+=1
    for i in range(1,len(lst)):
        if lst[i]<=lst[i-1]:
            temp=lst[i]
            lst[i]=lst[i-1]+2
            num+=lst[i]-temp
        elif lst[i]%2!=0:
            lst[i]=lst[i]+1
            num+=1 
    return num

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    