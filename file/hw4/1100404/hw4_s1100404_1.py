def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) > 10000:
        return False
    if Str == "": #處理到最後剛剛好變成空字串
        return True
    if Str[0] == Str[-1]: #判斷第一個和最後一個是不是一樣
        Str = Str[1:-1] #刪除第一個和最後一個，傳給Str
        return homework_4(Str) #回傳下一層回傳的值
    else:
        return False #中間有頭尾不一樣就是False


if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    