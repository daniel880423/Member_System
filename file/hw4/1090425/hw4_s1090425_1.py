def homework_4(Str):
    if Str == "":
        return True 
    j=0
    k=-1
    try:
        for i in range(500):
            if Str[j] != Str[k]:
                return False
            j+=1
            k-=1
    except IndexError:
        return True
    else:
        j+=1
        return homework_4(Str[j:k]) 

if __name__ == '__main__':
    Str = "mm"
    print(homework_4(Str))
    