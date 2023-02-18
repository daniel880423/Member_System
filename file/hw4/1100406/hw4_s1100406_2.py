def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    return Str==Str[::-1] #將參數倒過來寫，並和原參數比對，回傳布林值

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    