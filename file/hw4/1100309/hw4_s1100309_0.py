def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 2 :
        return True 
    if Str[0:101]!=Str[-1:-102:-1] :
        return False
    return homework_4(Str[101:-101])   #把一樣的字串刪掉

    
if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    