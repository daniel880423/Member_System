def homework_2(lst):
    n=len(lst)  #算lst長度
    m=0         #計算上一位跟下一位的差
    step=0      #計算總步數

    if lst[0]%2!=0: #第一位不為偶數
        step+=1     #總步數+1
        lst[0]+=1   #偶數

    for i in range(1,n):
        if lst[i]<=lst[i-1]:    #前一位是否大於第一位
            m=lst[i-1]-lst[i]+1 #加多少會比前一位大且為奇數
            step+=m             #總步數++
            lst[i]+=m           #改變lst的值

        if lst[i]%2!=0: #lst[i]不為偶數
            step+=1     #總步數++      
            lst[i]+=1   #改變lst的值
 
    return step

if __name__ == '__main__':
    lst =   [38, 17, 45, 13, 25]
    print(homework_2(lst))