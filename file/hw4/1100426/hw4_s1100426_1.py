#from numpy import _FlatIterSelf
import sys
sys.setrecursionlimit(10000)
def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    
    if len(Str)<=0:
        return True
    if Str[0]!=Str[-1]:
        return False
    
    else:
        length = len(Str)
        Str = Str[1:-1]
        return homework_4(Str)








    

if __name__ == '__main__':
    Str = "FuxkkxuF"
    print(homework_4(Str))
    