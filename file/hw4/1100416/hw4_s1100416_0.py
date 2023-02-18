def homework_4(Str): 
    lenth=len(Str)
    while True:
        if lenth<2:
            return True
            break
        elif Str[lenth-lenth]==Str[-1]:
            Str=Str[1:-1]
            return homework_4(Str)
        else:
            return False
            break
    








     

if __name__ == '__main__':
    Str = "011120"
    print(homework_4(Str))
    