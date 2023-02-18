def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    #boolen=False   #先設一個布林變數，可先設為False或True，不設也可以
    if len(Str)<2:  #如果Str的長度小於2了，把boolen設為True(有兩種情況，【1.原本長度只有1】，【2.後面回傳的Str剩下不到2的長度】)
        boolen=True
    else:
        if Str[0]!=Str[-1]:  #如果Str裡第一個字和最後一個字不一樣
            boolen=False    #把要回傳的布林變數設為False
        else:               #如果Str裡第一個字和最後一個字一樣，就回傳忽略比較過的第一個字和最後一個字的Str
            return homework_4(Str[1:-1])

    return boolen    #最後回傳布林值


if __name__ == '__main__':
    Str = "abba"
    #Str="A0cc0A"
    #Str="Abccba"
    #Str="011120"
    #Str="abcdefggfedcba"
    #Str="AAAAAaaaaa"
    #Str="A00100A"
    #Str="FuxkkxuF"
    print(homework_4(Str))
    