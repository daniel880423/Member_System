def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l = len(Str)
    if l < 2:
        return False
        
    if str(Str) == str(Str)[::-1]:
        return True
    else:
        return False







if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    