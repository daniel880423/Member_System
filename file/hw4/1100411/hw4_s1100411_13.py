def homework_4(Str): 
    if len(Str) < 3:
        return True   #終止條件
    if Str[0:2] == Str[-1]+Str[-2]: #一次比2個字
        return homework_4(Str[2:-2])
    else:
        return False #終止條件
if __name__ == '__main__':
    Str = "A00100A"
    print(homework_4(Str))
    