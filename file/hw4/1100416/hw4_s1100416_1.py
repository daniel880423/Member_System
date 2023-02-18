def homework_4(Str): 
    lenth=len(Str)
    while True:
        if lenth<2:
            return True
            break
        elif Str[0:2]==Str[-1]+Str[-2]:
            Str=Str[2:-2]
            return homework_4(Str)
        else:
            return False
            break
    








     

if __name__ == '__main__':
    Str = "AADFDAA"
    print(homework_4(Str))
    