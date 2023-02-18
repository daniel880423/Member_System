def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    Max=len(Str)-1  #maximun index
    Min=0           #minimun index

    if Min>=Max:
        return True
    elif Str[Min]!=Str[Max]:
        return False
    else:
        return homework_4(Str[Min+1:Max])


    return 

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    