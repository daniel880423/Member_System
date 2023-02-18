def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lens = len(Str)
    count = lens//2
    a=0
    if ispalindrome(count,lens,a) == 1:
        return True
    else:
        return False   
def ispalindrome(count,lens,a):
    start = 0
    if count == 0:
        return 1
    if Str[a] == Str[lens-1]:
        start+=1
    else:
        return 0
    return ispalindrome (count-start,lens-1,a+1)

if __name__ == '__main__':
    Str = "AAAAAaaaaa"
    print(homework_4(Str))
    
    