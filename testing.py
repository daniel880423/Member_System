import auto
import importlib
import os
def ans(filename, hwnum):
    auto.receive(filename, hwnum)
    os.chdir(auto.first)
    importlib.reload(auto)
    # Answer = auto.string
    Score = auto.Score
    Time = auto.Time
    Memery = auto.Memery
    return Score, Time, Memery
# a,b,c=ans('B1.py','4')
# print(a,b,c)