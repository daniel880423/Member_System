def homework_2(lst):
    step=0                   #計算步數
    for i in lst:
        if i<=i-1 or i%2!=0: #lst中前一位大於後一位或除2有餘時
            i+=1
            step+=(i+1)
    return step

if __name__ == '__main__':
    lst =   [1,1,1]
    print(homework_2(lst))