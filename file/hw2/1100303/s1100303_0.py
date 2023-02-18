def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step=0
    pre=0
    if lst[0]%2!=0:
        lst[0]+=1
        step+=1
    
    for i in range(1,len(lst)):
        if lst[i]%2!=0:

            if lst[i]<lst[i-1]:
                pre=lst[i]
                lst[i]=lst[i-1]+2
                step+=(lst[i]-pre)
            if lst[i]>lst[i-1]:
                if lst[i]%2!=0:
                    lst[i]+=1
                    step+=1
            if lst[i]==lst[i-1]:
                lst[i]+=2
                step+=2
        else:
            if lst[i]<lst[i-1]:
                pre=lst[i]
                lst[i]=lst[i-1]+2
                step+=(lst[i]-pre)
            if lst[i]>lst[i-1]:
                if lst[i]%2!=0:
                    lst[i]+=1
                    step+=1
            if lst[i]==lst[i-1]:
                lst[i]+=2
                step+=2
            else:
                continue
                step+=0

    return step

if __name__ == '__main__':
    lst =  [1,5,2,7,4]

    print(homework_2(lst))
    