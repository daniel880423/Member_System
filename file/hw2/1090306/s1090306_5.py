def homework_2(lst):
    s=0
    w=0
    for i in lst:
        if (w == 0):
            if i % 2 != 0:
                s=s+1
                lst[w]=lst[w]+s
        else:
            if lst[w-1]<lst[w]:
                if lst[w] % 2 != 0:
                    d=((lst[w]+1) - lst[w])
                    s = s + d
                    lst[w]=lst[w]+d
            else:  
                if lst[w-1] % 2 == 0 and lst[w] % 2 == 0:
                    d=((lst[w-1]+2) - lst[w])
                    lst[w]=lst[w]+d
                    s = s + d      
                elif lst[w-1] % 2 != 0 and lst[w] % 2 != 0:
                    d=((lst[w-1]+1) - lst[w])
                    lst[w]=lst[w]+d
                    s = s + d
                elif lst[w-1] % 2 == 0 and lst[w] % 2 != 0:
                    d=((lst[w-1]+2) - (lst[w]))
                    lst[w]=lst[w]+d
                    s = s + d
                elif lst[w-1] % 2 != 0 and lst[w] % 2 == 0:
                    d=((lst[w-1]+3) - lst[w])
                    lst[w]=lst[w]+d
                    s = s + d
        w=w+1
    return s

if __name__ == '__main__':
    lst = [1]
    print(homework_2(lst))
    