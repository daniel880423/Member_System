def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    boo=True       #將答案設為True
    ans=Str[::-1]  #寫出反過來的數
    if Str==ans:   #若Str=反過來的數
        boo=True   
    else:
        boo=False
    return boo
    
if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    