def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lens = len(Str)
    count = lens//2
    a=0
    if palindrome(Str,count,lens,a) == 1:
        return True
    else:
        return False   
def palindrome(Str,count,lens,a):
    if count <= 0:
        return 1
    if Str[a] == Str[lens-1] and Str[a+1] == Str[lens-2] and Str[a+2] == Str[lens-3]:
        return palindrome (Str,count-2,lens-2,a+2)
    else:
        return 0
if __name__ == '__main__':
    Str = "n0t1k2r3t4n5n4t3r2k1t0n"
    print(homework_4(Str))
    
    