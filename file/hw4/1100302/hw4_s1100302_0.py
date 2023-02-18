def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    time = len(Str) //2 
    lens = len(Str)
    if ispalindrome(time,lens) == 1:
        return True
    else:
        return False
def ispalindrome(time,lens):
    if time == 0:
        return 1
    if Str[time-1] == Str[lens-time]:
       return  ispalindrome(time-1,lens)
    else:
        return 0

if __name__ == '__main__':
    Str = "FuxkkxuF"
    print(homework_4(Str))


