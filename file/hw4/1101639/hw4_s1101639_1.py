def homework_4(Str):
    half = len(Str)//2
    ans = True
    for i in range(half):
        if Str[i] != Str[-i-1]:
            ans = False
            break
    return ans 
if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    