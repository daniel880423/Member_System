def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    n=len(Str) #Str長度

    if n>10000:  #字串大小防呆
        print('error input')
        return
    elif n<10:     #剩下的小範圍
        if n<2:    #字串只有一字或已經確認到最後
            return True
        else:
            if Str[0]!=Str[-1]:  #確認是否為回文(小範圍)
                return False
            return homework_4(Str[1:-1]) #去掉已確認再跑一次
        
    else:
        if Str[0:5]!=Str[-1:-6:-1]: #確認是否為回文(大範圍)
            return False
        else:
            return homework_4(Str[5:-5]) #去掉已確認再跑一次


if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    