def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step=0
    for i in range(len(lst)):
        if i==0 :
            if lst[i]%2!=0:
                lst[i]=lst[i]+1
                step+=1
        else:
            if lst[i]<=lst[i-1]:
                step=step+(lst[i-1]-lst[i]+2)
                lst[i]=lst[i-1]+2
            else:
                if lst[i]%2!=0:
                    lst[i]=lst[i]+1
                    step+=1




    return step
if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    