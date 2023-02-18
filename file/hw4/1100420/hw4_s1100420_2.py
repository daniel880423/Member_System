def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    if len(Str)==0:
        return False
    if len(Str)>10000:
        return False
    else:
        return returnanswer(Str)

def returnanswer(Str):
    for i in range(len(Str)//2):
        if Str[i] == Str[len(Str)-1-i]:
            continue
        else:
            return False
            break
    return True


if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))