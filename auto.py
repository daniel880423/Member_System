import os, sys
import time
from guppy import hpy

try:    
    first = os.getcwd()
    # print(first)
    os.chdir(f"./file/hw{hw_num}")
    last = os.getcwd()
    # print(last)
    # 抓取 function 名稱
    s = open(f'{student_file}.py', encoding='utf-8').read()
    start = s.index('def ')
    end = s[s.index('def ')+1:].index('(')+1
    function_name = s[start: end].split()[1]
    #---------------------------------------------------------# vscode 加入環境變數
    sys.dont_write_bytecode = True
    sys.path.append(os.getcwd())
    #---------------------------------------------------------# vscode 加入環境變數
    exec(f"from {student_file} import {function_name} as func")
    exec(f"from question import hw{hw_num}_IN as In, hw{hw_num}_ANS as Ans")
    frequency = 100  # 循環次數
    score = 0  # 基本分
    avg = 2.5  # 一題幾分
    now = time.time()  # 時間複雜度
    heap = hpy()
    heap.setref()
    heap_status1 = heap.heap()  # 堆疊起點
    for f in range(frequency):
        for i in range(len(In)):
            student_Ans = func(In[i][0], In[i][1])
            if student_Ans == Ans[i]:
                if f == 0:
                    score += avg
    heap_status2 = heap.heap()  # 堆疊終點
    os.chdir(first)
    Score = int(score)
    Time = round((time.time()-now)*1000, 1)
    Memery = round(heap_status2.size/1024**1, 3)
    # string = f"\n分數:{int(score)}\n時間:{round((time.time()-now)*1000, 1)}ms\n記憶體:{round(heap_status2.size/1024**1, 3)}KB"
    # print(f"跌代次數 : {frequency} 次")
    # print(f"所花時間 : {round((time.time()-now)*1000, 2)} ms")
    # print(f"所使用記憶體 : {heap_status2.size/1024**2} MB")
    # print(f"分數 : {score} 分")
    # print(f"記憶體使用資訊 : \n{heap_status2}")  # 從 第5行 - 第14行
except NameError:
    def receive(filename, hwnum):
        global student_file,hw_num
        student_file = filename.split('.py')[0]
        hw_num = hwnum