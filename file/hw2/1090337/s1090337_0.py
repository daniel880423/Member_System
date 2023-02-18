def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    n=len(lst)  #總共幾項
    a=max(lst)  #最大值
    b=min(lst)  #最小值
    d=0         #前一項最後的值
    ans=0       #幾步
    if n>1000 or a>10000 or b<1:   #偵錯
        print("error")
        return
    else:
        for i in range(0,n):  #提取每項的值
            c=lst[i]          #第i項的值
            while True:       #是否遞增
                if c<=d:
                    c=c+2
                    ans=ans+2
                else:
                    break
            if c%2!=0:       #是否為偶數
                c=c+1
                ans=ans+1     
            d=c      #紀錄第i項最終的值
        return ans   #回傳

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    