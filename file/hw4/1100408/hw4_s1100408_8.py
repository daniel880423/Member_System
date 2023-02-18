def homework_4(Str):
    if len(Str)<100:
        if len(Str)<2:          #長度0或1代表不用判斷了
            return True
        elif Str[0]!=Str[-1]:   #第一項不等於最後一項(False)
            return False
        else:
            return homework_4(Str[1:-1])    #遞迴並且把頭尾刪掉
    else:
        temp = ''.join(reversed(Str[-100:]))   #用反轉加快進行反轉倒數1000
        if Str[0:100] != temp:                 #如果跟Str前1000個不一樣False
            return False
        else:
            return homework_4(Str[100:-100])  #遞迴刪掉頭尾100筆

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    