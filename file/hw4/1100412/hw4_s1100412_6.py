def comparison(Str,i): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) == 1:                                        #長度為1必為回文數
        return 1                                  
    if  Str[0+i] == Str[-1-i]:                                #如果前後相同,依序向後找
        output = 1                                       
        if(Str[len(Str)//2-1+i] == Str[(len(Str)-1)//2+1-i] ):#比對中間的兩個數,依序向兩側找 
            output = 1
        else:
            output = 0  
    else:
        output = False
    return output
def homework_4(Str):
    i=0  
    if comparison(Str,i) == 1 :                                  #如果前一次符合回文數
        return bool((comparison(Str,i))*comparison(Str,i+1))     #乘下一個output
    else:
        return bool(comparison(Str,i))


if __name__ == '__main__':
    Str = "Fuxxub"
    print(homework_4(Str))