def homework_4(Str): 
    str1 = list(Str)
    res = True
    while len(str1) > 1:
        if str1[0] == str1[-1]:
            str1.remove(str1[0])
            str1.remove(str1[-1])
            res = homework_4(str1)
        else:
            res = False
            return res
    return res


if __name__ == '__main__':
    Str = "011120"
    print(homework_4(Str))
    