import sys
sys.setrecursionlimit(2000)
def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if Str[0] == Str[-1]:
        if len(Str) == 1:
            return True
        Str = Str[1:-1]
        if len(Str) < 2:
            return True
        return homework_4(Str)
    else:
        return False
    
if __name__ == '__main__':
    Str = "22322"
    print(homework_4(Str))
    