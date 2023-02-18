def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 100:
        if len(Str)<2:  
            return True
        if Str[0]!=Str[-1]:
            return False
        else: 
            return homework_4(Str[1:-1])
    else:
        reverse_string = ''.join(reversed(Str[-100:]))
        if Str[0:100] != reverse_string:
            return False
        else:
            return homework_4(Str[100:-100])
        
        
if __name__ == '__main__':
    Str =   "abba"
    print(homework_4(Str))
    