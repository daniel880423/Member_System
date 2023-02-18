def homework_4(Str): #1100332
    str = list(Str)#轉list
    ans = True
    for i in range(len(str)):
        if str[i]== str[-1-i]:
            continue
        elif str[i]!=str[-1-i]:
            ans = False
            break
    return ans



    

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    