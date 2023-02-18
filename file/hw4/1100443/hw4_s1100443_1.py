from turtle import Turtle


def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
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
    