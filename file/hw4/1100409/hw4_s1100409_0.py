def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    h=0
    long = len(Str)
    ct = long//2
    if PD(Str,ct,long,h) == 1:
        return True
    else:
        return False   
def PD(Str,ct,long,h):
    if ct <= 0:
        return 1
    if Str[h] == Str[long-1] and Str[h+1] == Str[long-2]:

        return PD (Str,ct-2,long-2,h+2)
    else:

        return 0
if __name__ == '__main__':

    Str = "adefggfedcba"

    print(homework_4(Str))
    
    