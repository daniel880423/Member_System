def homework_2(lst): 
    ans=[]
    num=0
    if lst[0]%2!=0:
            ans.append(lst[0]+1)
            num+=1
    else:
        ans.append(lst[0])
    for i in range(1,len(lst)):
        temp=ans[i-1]
        if lst[i]<=temp:
            temp+=2
            ans.append(temp)
            num+=temp-lst[i]
        elif lst[i]%2==0:
            ans.append(lst[i])
        else:
            ans.append(lst[i]+1)  
            num+=1 
    return num

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    