def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lenlst = len(lst)
    lst.append(None)
    count = 0
    for i in range(lenlst):
        if lst[i]%2 !=0:
            lst[i]= lst[i]+1
            count+=1
            
        else:
            continue
    for i in range(lenlst): 
        if i == lenlst-1:
            break
        
        if lst[i]>lst[i+1]:
            lst[i+1]=lst[i]+2
            count = count+lst[i]
        
        if lst[i]==lst[i+1]:
            lst[i+1]+=2
            count+=2
        if lst[i]<lst[i+1]:
            continue

    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    