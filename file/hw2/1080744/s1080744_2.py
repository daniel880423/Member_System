def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count=0
    for i in range(len(lst)):
        if i==0:
            if lst[i]%2==0:
                continue;
            else:
                count+=1    
                lst[i]+=1
        else:
            if lst[i-1]<lst[i]:
                if lst[i]%2==0:
                    continue;
                else:
                    count+=1
                    lst[i]+=1
            else:
                count+=(lst[i-1]-lst[i]+2)
                lst[i]=lst[i-1]+2
    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    