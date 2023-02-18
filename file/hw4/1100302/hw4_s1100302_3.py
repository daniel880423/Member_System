def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    time = len(Str) //2 
    lens = len(Str)
    if lens > 4000:
        if is_longpalindrome(time,lens,Str) == 1:
            return True
        else:
            return False
    if ispalindrome(time,lens,Str) == 1:
        return True
    else:
        return False
def ispalindrome(time,lens,Str):
    if time <= 0:
        return 1
    if Str[time-1] == Str[lens-time]:
        return ispalindrome(time-1,lens,Str)
    else:
        return 0
def is_longpalindrome(time,lens,Str):
    if time == 0:
        return 1
    if Str[time-1] == Str[lens-time] and Str[time-2] == Str[lens-time-1]:
        return is_longpalindrome(time-2,lens,Str)
    else:
        return 0


if __name__ == '__main__':
    Str = "aAa"
    print(homework_4(Str))



