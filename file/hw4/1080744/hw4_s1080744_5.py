def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    Max=len(Str)-1  #maximun index
    Min=0           #minimun index
    if Min>=Max:
        return True
    elif Str[Min:Min+2]!=Str[Max:Max-2:-1]:
        if ((Str[Min]==Str[Max]) & (Str[Min+1]==Str[Max-1])):
          
            return True
        else:
            return False
    else:
        return homework_4(Str[Min+2:Max-1])


   

if __name__ == '__main__':
    Str = 'd0mxvky5wjlwc10fwhbc15flxkq20ygdgg25cdeko30ypbfh35qobdq40tadjx45uddem50eqcju55rbst60tsptw65blbof70iwsng75nylxxlyn57gnswi07foblb56wtpst06tusbr55ujcqe05meddu4xjdat04qdboq53hfbpy03okedc52ggdgy02qkxlf51cbhwf01cwljw5ykvxm0d'
    print(homework_4(Str))
    