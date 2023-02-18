def homework_4(Str):
    half = len(Str)//2
    answer = True
    for i in range(half):
        if Str[i] != Str[-i-1]:
            answer = False
            break
    return answer 
if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    