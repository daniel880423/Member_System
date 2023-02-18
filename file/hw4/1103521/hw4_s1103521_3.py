def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 2:  # 如果字符串只有0或1個字，那麽該字串符合回文的定義
        return True
    if Str[0] != Str[-1] or Str[1] != Str[-2]:  # 如果字符串不止一個字符，檢查字串符的第一項和最後一項是否等同
        return False
    return homework_4(Str[2:-2])  # 字串符的第一項和最後一項相同，去除字串符的第一項和最後一項，繼續進行檢查
    # 取字串[1]~[N-1] 扣掉頭尾項

if __name__ == '__main__':
    Str = "oRbBpOpXnYtYnIaWrOvTwKkPvCoFqDkXhLjYhNiNoKzWvTfZyXdOlAmVuGwBdAbGqDgAhUxKoEyNsDlHHlDSNyEoKxUhAgDqGbAdBwGuVmAlOdXyZfTvWzKoNiNhYjLhXkDqFoCvPkKwTvOrWaInYtYnXpOpBbRo"
    print(homework_4(Str))
