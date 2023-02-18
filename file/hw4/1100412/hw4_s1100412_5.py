def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    Str = list(Str)
    if len(Str) == 1:                                   #長度為1必為回文數
        return True                                  
    if  Str[0] == Str[-1]:                              #如果前後相同
        del Str[0]                                      #刪掉前後
        del Str[-1]
        output = True                                       
        if len(Str)>= 2:                                      #要有兩個數才能比較
            if(Str[len(Str)//2-1] == Str[(len(Str)-1)//2+1] ):#比對中間的兩個數
                del Str[len(Str)//2-1]                        #刪掉中間的兩個數
                del Str[len(Str)//2]        
                output = True
            else:
                output = False  
    else:
        output = False
  
    if output == True and len(Str) >= 2:                #如果前一次符合回文數且還有數能判斷
        return bool((output)*homework_4(Str))           #乘下一個output
    else:
        return bool(output)

if __name__ == '__main__':
    Str = "A00100A"
    print(homework_4(Str))