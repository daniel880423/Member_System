from turtle import Turtle

def homework_4(Str):
    if len(Str)==0:
        return False
    if len(Str)>10000:
        return True
    else:
        return ans(Str)
 

def ans(Str):
    result=True #先假設全部都是True
    for i in range(len(Str)//2): 
        if Str[i]==Str[len(Str)-1-i]:
            continue
        else:
            result=False 
            break
    return result


 

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    