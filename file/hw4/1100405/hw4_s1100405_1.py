def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    bool = False

    def reverse(Str):
        print(Str)
        if len(Str) == 0:
            
            return Str
        else: 
            return reverse(Str[1:]) + Str[0]

    if Str == reverse(Str):
        bool = True

    return bool

if __name__ == '__main__':
    Str = 'abcdefggfedcba'
    print(homework_4(Str))
    