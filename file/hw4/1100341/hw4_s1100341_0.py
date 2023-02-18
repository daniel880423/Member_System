def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)   
    if len(Str) <= 1:        #如果最後遞迴出來剩1或0就代表是回文數
        return True
    if Str[0] != Str[-1]:    #前後不相同就不是回文數
        return False
    return homework_4(Str[1:-1])  #遞迴range是扣掉頭尾 [1:-1]

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    