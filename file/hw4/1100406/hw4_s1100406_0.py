def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)<2: #判斷長度，若小於2則必定成立
        return True
    if Str[0]!=Str[-1]: #若第一個不等於最後一個，回傳False
        return False
    return homework_4(Str[1:-1]) #重複呼叫函式，並刪除首相及末項

if __name__ == '__main__':
    Str = "abcca"
    print(homework_4(Str))
    