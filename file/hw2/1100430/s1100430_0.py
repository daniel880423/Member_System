def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l=len(lst)
    max=0
    sum=0
    for i in range(l):
        if lst[i]>=max:
            if lst[i]%2==0:
                max=lst[i]+2
                print(sum)
            else:
                lst[i]+=1
                max=lst[i]+2
                sum+=1
                print(sum)
        else:
            n=max-lst[i]
            lst[i]+=n
            max=lst[i]+2
            sum+=n  
            print(sum)   
          
    return sum
if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    