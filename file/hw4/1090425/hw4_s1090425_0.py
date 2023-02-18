def homework_4(Str):
    if Str == "":
        return True 
    if Str[0] != Str[-1]:
        return False
    else:
        return homework_4(Str[1:-1]) 

if __name__ == '__main__':
    Str = "abbA"
    print(homework_4(Str))
    