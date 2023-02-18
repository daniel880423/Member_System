def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step=0
    if lst[0]%2==1:#判斷第一個元素是否為偶數，不是的話就將lst[0]+1,step也+1
                lst[0]+=1
                step+=1
    for i in range(1,len(lst)):#從lst[1]檢查到lst最後一個元素。
        if lst[i]>lst[i-1]:#大於前面一項就只檢查是否為偶數
            if lst[i]%2==1:
                lst[i]+=1
                step+=1
        else:#不大於前項就先加到比前項多1，在檢查奇偶數。
            step+=(lst[i-1]-lst[i]+1)
            lst[i]=lst[i-1]+1
            if lst[i]%2==1:
                lst[i]+=1
                step+=1
    return step

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    