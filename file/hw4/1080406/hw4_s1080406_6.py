def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    i = int(len(Str)/8)
    if len(Str) < 2:                            #如果字串長度小於2，可以判斷字串為回文數
        return True
    elif Str[i-1:0:-1]+Str[0]  != Str[-i:]:     #將字串分成兩邊，前面的字串反轉跟後面字串比對，不同的話回傳False
        return False
    return homework_4(Str[i:-i])                #將已經比對過的部分刪除，重新帶回函數
    
if __name__ == '__main__':
    Str = 'FuxkkxuF'
    print(homework_4(Str))
    