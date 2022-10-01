import auto
import importlib
import os
def ans(studentid, filename, hwnum):
    auto.receive(studentid, filename, hwnum)
    os.chdir(auto.first)
    importlib.reload(auto)
    # Answer = auto.string
    Score = auto.Score
    Time = auto.Time
    Memory = auto.Memory
    Sheet = auto.sheet
    return Score, Time, Memory, Sheet