def homework_4(Str): 
    num = len(Str)//2
    boo = True
    for i in range(num):
        if Str[i] != Str[-1-i]:
            boo = False
            break
    return boo

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    