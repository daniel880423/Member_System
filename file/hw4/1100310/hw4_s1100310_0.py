def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    if len(Str)<2:  # 什麼情況會等於回文字
        return True
    if Str[0]!=Str[-1]:  # 什麼情況不等於回文字
        return False
    return homework_4(Str[1:-1])  # 遞迴條件，Str前後比對，去掉比對後的數字(使用切片)

if __name__ == '__main__':
    Str = "abba"
    print(homework_4(Str))
    