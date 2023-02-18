
def homework_4(Str):  #遞迴
    if len(Str)<1:
        return False
    if len(Str)>10000:
        return False
    else:
        return boolanswer(Str)


def boolanswer(Str): #迴圈
    Str_len=len(Str)
    answer=True
    for i in range(Str_len//2):
        if Str[i]==Str[Str_len-1-i]: 
            continue
        if Str[i]!=Str[Str_len-1-i]:
            answer=False
            break
    return answer

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    