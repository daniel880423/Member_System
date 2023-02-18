from xmlrpc.client import boolean


def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    vfy = True
    if len(Str) == 1 or len(Str) == 0:
        vfy = True
    elif Str[0] == Str[-1]:
        return homework_4(Str[1:-1])
    else:
        vfy = False

    return vfy

if __name__ == '__main__':
    Str = "abbaa"
    print(homework_4(Str))
    