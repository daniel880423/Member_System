def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

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
    Str = "AAAAAaaaaa"
    print(homework_4(Str))
    