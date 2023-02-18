def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step_count = 0 #計算步數
    index = 1 #索引-比較第一項跟第二項
    for i in range(0,len(lst)):
        
        if index == len(lst): #檢驗是否為單一數
            if len(lst) != 1:
                break
            
        if len(lst) == 1:#檢驗是否為單一奇數
            if lst[i] % 2 != 0:
                lst[i] += 1
                step_count += 1
                
        else:
            while lst[index] <= lst[i]:
                lst[index] += 1
                step_count += 1
                
                if lst[index] < lst[i]:#檢驗目前數字是否比下一項大
                    lst[index] += 1
                    step_count += 1
                    
                else:
                    if  lst[index] % 2 != 0 :#檢驗下一項是否為偶數
                        lst[index] += 1
                        step_count += 1
                        
                        
                    if lst[index] == lst[i]:#檢驗目前數字與下一項是否相同
                        lst[index] += 1
                        step_count += 1
                        
                        
                    if lst[i] % 2 != 0:#檢驗目前數字是否為偶數
                        lst[i] += 1
                        step_count += 1
                   
                continue
                    
           ####以上迴圈已讓下一項比目前數字大###
           ###以下的if將檢驗當下一項比較大時，是否為奇數###
            if lst[index] % 2 != 0:#檢驗下一項是否為奇數
                lst[index] += 1
                step_count += 1
            if lst[i] %2 != 0:#檢驗目前數字是否為奇數
                lst[i] += 1
                step_count += 1
                                
            index += 1#將索引+1，接著回去跑for迴圈
       
              

    return (step_count)#回傳步數

if __name__ == '__main__':
    lst = [2]
    print(homework_2(lst))
    