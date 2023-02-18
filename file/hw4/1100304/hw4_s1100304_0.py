def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) <= 1:  #若Str長度為 0~1 ==> 必為回文
        return True

    elif Str[0] != Str[-1]:  #若長度 >1 且 第一項和最後一項不同 ==> 不為回文
        return False

    else:
        ans = homework_4(Str[1:-1])  #若長度 >1 且 第一項和最後一項相同 ==> 繼續往下一項(向中間)檢查

    return ans

if __name__ == '__main__':
    Str = "abbo"
    print(homework_4(Str))