def homework_4(Str): 
    
    if len(Str) < 2: #當Str只剩一位或沒有時,回報True為回文字
        return True
    return Str[0]+Str[1] == Str[-1]+Str[-2] and homework_4(Str[2:-2])


if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    