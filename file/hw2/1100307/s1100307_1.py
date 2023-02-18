def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    long = len(lst)
    a = lst[0]
    count = 0
    if (a%2)!=0:
        a+=1
        count+=1
    for i in range(1,long):
        if lst[i]<=a:
            count+=a+2-lst[i]
            lst[i]=a+2
            a = lst[i]
            
        else:
            if (lst[i]%2)!=0:
                lst[i]+=1
                count+=1
            a= lst[i]
    








    return count

if __name__ == '__main__':
    lst = [13, 22, 4, 29, 46, 22, 29, 36]
    print(homework_2(lst))
    