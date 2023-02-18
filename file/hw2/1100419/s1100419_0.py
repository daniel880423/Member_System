from re import X


def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    i=0  
    count=0 
    all=0
    all_new=0
    len_lst=len(lst)
    for i in range(len_lst):
        all+=lst[i]
    for i in range(len_lst):
        if i==0:
            if lst[i]%2!=0:
                lst[i]+=1
        if i>0:
            if (lst[i]-lst[i-1])>0 and lst[i]%2==0:
                lst[i]=lst[i]
            if (lst[i]-lst[i-1])>0 and lst[i]%2==1:
                lst[i]=lst[i]+1
            if (lst[i]-lst[i-1])<=0:
                lst[i]=lst[i-1]+2
    for i in range(len_lst):
        all_new+=lst[i]
    count=all_new-all      
    return count
 

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    