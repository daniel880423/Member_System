def homework_4(Str): 
    if len(Str) < 3:
        return True
    if Str[0:2] == Str[-1]+Str[-2]:
        return homework_4(Str[2:-2])
    else:
        return False
if __name__ == '__main__':
    Str = "A00100A"
    print(homework_4(Str))
    