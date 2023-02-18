def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    sum=0
    a=len(lst)
    b=a-1
    for i in range(0,b):
        c=lst[0]
        if (c % 2)!=0:
            c+=1
            sum+=1
            
    
        d=lst[1]
        if (d % 2)!=0:
            d+=1
            sum+=1
            
        

        while c >= d:
            d+=2
            sum+=2
            
        
        lst.pop(1) 
        lst.pop(0)
        lst.insert(0,d)
        

    return sum

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    