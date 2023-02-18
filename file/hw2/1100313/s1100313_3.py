def homework_2(lst):
    length = len(lst)                   #list長度
    compare = lst[0]                    #一開始要比較的數字
    step = 0                            #步數
    
    if compare%2 == 1:                  #如果第一個數字是奇數
            compare+=1                  #加一步變偶數
            step+=1                     #步數+1
         
    for i in range(1, length):
        if lst[i]==compare+2:           #如果現在的數字等於下一個遞增偶數+2(ex:[2, 4])
            compare = lst[i]            #則不需要加步數，直接往下一個數字前進
            continue
        
        if lst[i]>compare:              #如果現在的數字大於要上一個要比較的數字(ex:[1, 5])
            if lst[i]%2==1:             #若是奇數
                next_even=lst[i]+1      #則下一個遞增偶數為現在的數字+1
                step+=next_even-lst[i]  #步數加上下一個遞增偶數-原本的數字
                compare=next_even       #準備往下一個數字前進，要比較的數字變為遞增偶數
                
            else:                       #若是偶數
                compare=lst[i]          #準備往下一個數字前進，要比較的數字變為遞增偶數
                
                
        elif lst[i]==compare:           #如果現在的數字等於下一個遞增偶數(ex:[1, 2]，注意這時候compare已經+1)
            step+=2                     #步數+2
                
        else:                           #如果現在的數字小於要上一個要比較的數字
            next_even=compare+2         #下一個遞增偶數=compare+2
            step+=next_even-lst[i]      #步數加上下一個遞增偶數-原本的數字  
            compare=next_even           #準備往下一個數字前進，要比較的數字變為遞增偶數
            
    return step                         #回傳總步數

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    