def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lst = list(Str)
    if len(lst)<2:
        return True
    if len(lst)>200:
        lst_1 = lst[0:100]
        lst_2 = lst[-1:-101:-1]
        if lst_1 == lst_2:
            for i in range(100):
                lst.pop(0)
                lst.pop()
            return homework_4(lst)

    elif lst[0] == lst[-1]:
        lst.pop(0)
        lst.pop()
        return homework_4(lst)
    return False


if __name__ == '__main__':
    Str = "a0plkticb7fivamavif7bcitklp0a"
    print(homework_4(Str))
    