def comparison(Str,i): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) == 1:                                         #長度為1必為回文數
        return 1                                  
    if  Str[0+i] == Str[len(Str)-1-i]:                        #如果前後相同,依序向後找
        output = 1                                    
        if(Str[len(Str)//2-1-i] == Str[(len(Str)-1)//2+1+i] ):#比對中間的兩個數,依序向兩側找 
            output = 1
        else:
            output = 0  
    else:
        output = 0
    if output == 1 and i < (len(Str))//4:                   #如果前一次符合回文數(一次判斷4個所以i只需到1/4長度)
        return bool(1*comparison(Str,i+1))                  #乘下一個output
    elif output == 0:                                       #如果前一次不符
        return False                                        #回傳False
    else:                                                   #全部找完
        return True                                         #回傳True
    
def homework_4(Str):  
    i=0
    return comparison(Str,i)
    

if __name__ == '__main__':
    Str ="d0mxvky5wjlwc10fwhbc15flxkq20ygdgg25cdeko30ypbfh35qobdq40tadjx45uddem50eqcju55rbst60tsptw65blbof70iwsng75nylxxlyn57gnswi07foblb56wtpst06tusbr55ujcqe05meddu4xjdat04qdboq53hfbpy03okedc52ggdgy02qkxlf51cbhwf01cwljw5ykvxm0d"
    print(homework_4(Str))
