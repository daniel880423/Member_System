def main(Str):
    result=True
    for i in range(len(Str)//2): # 只要比字串的一半長度
        if Str[i]==Str[len(Str)-1-i]: # 第i項等於倒數第i項
            continue
        else:
            result=False
            break
    return result    

def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str)<1 or len(Str)>10000:
        return False
    else:
        return main(Str)


if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    