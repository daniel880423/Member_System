def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)<10:
        if Str[0:(len(Str)//2)]==Str[-1:-(len(Str)//2+1):-1]:
            return True
        else:
            return False
    if Str[0:5]!=Str[-1:-6:-1]:
        return False
    return homework_4(Str[5:-5])
    
    
    








if __name__ == '__main__':
    Str = "abcdefggfedcba"
    print(homework_4(Str))
    