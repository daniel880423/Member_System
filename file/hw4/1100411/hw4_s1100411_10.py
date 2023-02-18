def homework_4(Str): 
    str1 = list(Str)
    if str1[0] == str1[-1]:
        str1.remove(str1[0])
        str1.pop()
        if len(str1) == 1 or len(str1) == 0:
            return True
        else:
            homework_4(str1)
        return True
    else:
        return False
if __name__ == '__main__':
    Str = "A00100A"
    print(homework_4(Str))
    