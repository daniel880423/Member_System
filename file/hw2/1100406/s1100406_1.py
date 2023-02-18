def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    sum=0 #步數計數器
    a=len(lst) #驗測資長度
    b=a-1 #修正長度
    for i in range(0,b): #一次抓取兩個變數，比對是否達到偶數遞增，完成後刪除前兩個值，並將改變後的第二個值成為第一個值，
                        #重複動作直到結束
        c=lst[0] #取出第一個數
        if (c % 2)!=0: #將c強制變為偶數
            c+=1
            sum+=1
            
    
        d=lst[1] #取出第二個數
        if (d % 2)!=0: #將d強制變為偶數
            d+=1
            sum+=1
            
        

        while c >= d: #比較c,d的值，改變d的大小，直到c < d
            d+=2
            sum+=2
            
        
        lst.pop(1)  #刪除第二個側資
        lst.pop(0)  #刪除第一個側資
        lst.insert(0,d)  #將改變過的d加入成為第一個側資
        

    return sum #回傳布數

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    