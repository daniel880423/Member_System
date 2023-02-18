def homework_4(Str): 
    time = len(Str) //2 
    lens = len(Str)
    print(lens)
    if ispalindrome(time,lens,Str) == 1:
        return True
    else:
        return False
def ispalindrome(time,lens,Str):
    if time == 0:
        return 1
    if time == 1:
        if Str[time-1] == Str[lens-time]:
            return 1
        else:
            return 0
    if Str[time-1] == Str[lens-time] and Str[time-2] == Str[lens-time+1]:
        return ispalindrome(time-2,lens,Str)
    else:
        return 0
if __name__ == '__main__':
    Str = "A00100A"
    print(homework_4(Str))