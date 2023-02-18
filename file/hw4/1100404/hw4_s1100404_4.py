def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if Str == "": #處理到最後剛剛好變成空字串
        return True
    if len(Str) >= 10:
        if Str[0:5] == Str[-1:-6:-1]:
            Str = Str[5:-5]
            return homework_4(Str)
        else:
            return False
            
    if Str[0] == Str[-1]:
        Str = Str[1:-1]
        return homework_4(Str)
    else:
        return False
        



if __name__ == '__main__':
    Str = "abcdefggfedcba"
    print(homework_4(Str))
    