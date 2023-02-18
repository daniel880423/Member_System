def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    lst = list(Str)
    if not lst or len(lst) == 1:
        return True
    if lst[0] == lst[-1]:
        lst.pop(0)
        lst.pop()
        return homework_4(lst)
    return False


if __name__ == '__main__':
    Str = "A00100A"
    print(homework_4(Str))
    