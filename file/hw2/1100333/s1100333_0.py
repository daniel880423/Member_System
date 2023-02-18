def homework_2(lst): # 1100333
    def StepA(l):
        for i in range(n,1,-1):
            if l[i] <= l[i-1]:
                l[i] +=2
        return l
    def StepB(ll):
        while(1):
            ct = 0
            for i in range(1,len(ll)):
                if ll[i]<=ll[i-1]:
                    ct +=1
            if ct != 0:
                ll = StepA(ll)
            elif ct == 0:
                break
        return ll
            

    list = lst.sort()
    lst2= []
    n = len(lst)
    m = 0
    for i in range(n):
        if list[i]%2 == 0:
            lst2.append(list[i])
        elif list[i]%2 == 1:
            lst2.append(list[i]+1)
    lst2 = StepB(lst2)
    for i in range(n):
        m += lst2[i]-list
    return m

if  __name__ == '_main_':
    lst = [1,1,1]
    print(homework_2(lst))