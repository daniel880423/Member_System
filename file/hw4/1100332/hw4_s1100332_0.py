def homework_4(Str): #1100332
    str = list(Str)#轉list
    if str[0]!=str[-1]:#step1如果頭尾不同
        return False
    elif len(str)==0 or len(str)==1:#step3如果裁完後長度剩下0或1，表示之前的頭尾對都一樣
        return True
    elif str[0]==str[-1]:#step2如果頭尾相同裁掉頭尾再跑一次函式
        st="".join(str[1:-2])#裁掉頭尾轉str
        return homework_4(st)

    

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    