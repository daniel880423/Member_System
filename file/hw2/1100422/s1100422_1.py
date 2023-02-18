def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    i=0
    step_count=0
    sum=0
    sum_final=0
    len_lst=len(lst)
    for i in range(len_lst):
        sum+=lst[i]
    for i in range(len_lst):
        if i==0 and lst[i]%2!=0:
            lst[i]+=1
        if i>0:
            if(lst[i]-lst[i-1])>0 and lst[i]%2!=0:
                lst[i]+=1
            if(lst[i]-lst[i-1])<=0:
                lst[i]=lst[i-1]+2
        sum_final+=lst[i]

    step_count=sum_final-sum
    return step_count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    