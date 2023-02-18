def homework_4(Str):
    if len(Str)<2:                            #如果字串長度變0，代表跑完都沒錯誤，即回傳True
        return True
    if Str[0]==Str[-1] and Str[1]==Str[-2]:   #一次比對四個字，如果一樣則繼續往前跑
        return homework_4(Str[2:-2])          #削掉左右兩邊各兩個字串
    
    return False                              #不對則return False

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    