def homework_4(str1): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    half=len(str1)//2
    for i in range(0,half):
        j=len(str1)-i-1
        if str1[i]!=str1[j]:
            return False
        else:
            return True
            
    return 

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    