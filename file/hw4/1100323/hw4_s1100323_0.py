def homework_4(Str):
    mum = len(Str)//2
    ans = True
    for i in range(mum):
        if Str[i] != Str[-1-i]:
            ans = False
            break
    return ans
if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))