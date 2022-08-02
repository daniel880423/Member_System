import os
import sys
# 載入 pymongo 套件
import pymongo
# 連線到 MongoDB 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")
# 把資料放進資料庫中

import re
class PythonToHTML:
    def __init__(self, input_py_name, hwn, id):
        # 輸入與輸出檔案名稱
        self.input_py_name = input_py_name
        self.hwn = hwn
        self.id = id

        # 定義所需資料
        self.py = str() # 檔案內容
        self.colored = list() # 已上色 index 列表，type : list[int]
        self.coloring_list = list() # 欲上色列表，type : list[list[int, int, str]]，意義為[開始index, 結束index, 著色類別]

        # 定義所有關鍵字和初始化搜尋模組與自訂類別、函式清單
        # class='module'
        self.type_list = ["type", "int", "float", "str", "tuple", "list", "dict", "set", "bool"]
        self.module_list = list()
        self.class_list = list()
        # class='str'
        self.quot_list = "\"\'"
        # class='func'
        self.func_list = ['staticmethod', 'classmethod', 'breakpoint', 'isinstance', 'issubclass', 'memoryview', 'bytearray', 'enumerate', 'frozenset', 'callable', 'property', 'reversed', 'compile', 'complex', 'delattr', 'getattr', 'globals', 'hasattr', 'setattr', 'divmod', 'filter', 'format', 'locals', 'object', 'sorted', 'aiter', 'anext', 'ascii', 'bytes', 'input', 'print', 'range', 'round', 'slice', 'super', 'eval', 'exec', 'hash', 'help', 'iter', 'next', 'open', 'repr', 'vars', 'abs', 'all', 'any', 'bin', 'chr', 'dir', 'hex', 'len', 'map', 'max', 'min', 'oct', 'ord', 'pow', 'sum', 'zip', 'id']
        self.def_list = list()
        # class='keyword1'
        self.keyword_list1 = ["nonlocal", "global", "lambda", "class", "and", "def", "not", "is", "or", "@"]
        self.bool_list = ['False', 'True', 'None']
        # class='keyword2'
        self.keyword_list2 = ["continue", "finally", "assert", "except", "import", "return", "except", "break", "raise", "while", "yield", "while", "elif", "else", "from", "pass", "with", "del", "for", "try", "as", "if", "in"]
        # class='op'
        self.op_list = "=+-*/%&|^>!~,:"
        # class='brackets'
        self.brackets_list = "()[]{}"
    def main(self): # 主程式
        self.read_py() # 讀取 py 檔，並存成 self.py(str)
        self.py = self.py.replace("<", "&lt")
        self.find_comment() # 尋找註解(class='comment')
        self.find_str() # 尋找字串(class='str')
        self.find_type() # 尋找型別(class='module')
        self.find_module() # 尋找模組(class='module')
        self.find_class() # 尋找類別(class='module')
        self.find_func() # 尋找內建函式(class='func')
        self.find_def() # 尋找自訂函式(class='func')
        self.find_keyword() # 尋找關鍵字(class='keyword1' and 'keyword2')
        self.find_bool_and_None() # 尋找布林值和空值(class='keyword1')
        self.find_lt() # 尋找 < 的 HTML格式(class='op')
        self.find_op() # 尋找運算符號(class='op')
        self.find_brackets() # 尋找括號(class='brackets')
        self.find_number() # 尋找數字(class='number')
        self.add_span() # 加入所有 span 標籤
        self.add_html_exception() # 處理 HTML 例外格式
        return self.to_html() # 轉為 HTML
    def read_py(self): # 讀取 py 檔，並存成 self.py(str)
        now = os.getcwd()
        # print(now)
        # print(type(filename), type(id))
        #-----------------------------------------------------#
        os.chdir(f"./file/hw{self.hwn}")
        sys.dont_write_bytecode = True
        sys.path.append(os.getcwd())
        #-----------------------------------------------------#
        os.chdir(f"{self.id}")
        sys.dont_write_bytecode = True
        sys.path.append(os.getcwd())
        with open(self.input_py_name, "r", encoding="utf-8") as f:
            # 頭尾加換行符號是方便做型別判斷處理，最後會刪除
            self.py = "\n"
            for line in f: self.py += line
            self.py += "\n"
            os.chdir(now)
    def find_comment(self): # 尋找註解(class='comment')
        for i in range(len(self.py)):
            if self.py[i] == "#":
                end = i + self.py[i:].find("\n")
                # line_head = i - (self.py[:i][::-1].find("\n")) - 1
                # line_tail = end
                # cmt_and_quot_list = 1
                # for j in range(line_head, line_tail):
                    
                # if (self.py[i:end].count("\"") + self.py[i:end].count("\'"))%2 == 0:
                data = [i, end, "comment"]
                self.add_coloring(data)
    def find_str(self): # 尋找字串(class='str')
        # 紀錄跨行字串引號位置
        span_dqi_list = [i for i in self.search_all('"""', self.py) if self.py[i-1]!="\\"]
        span_sqi_list = [i for i in self.search_all("'''", self.py) if self.py[i-1]!="\\"]
        span_dqi_list = [[span_dqi_list[i], span_dqi_list[i+1]+2, "str"] for i in range(0, len(span_dqi_list), 2)]
        span_sqi_list = [[span_sqi_list[i], span_sqi_list[i+1]+2, "str"] for i in range(0, len(span_sqi_list), 2)]
        span_qi_area = list()
        all_span_qi_list = span_dqi_list + span_sqi_list
        for i in range(len(all_span_qi_list)):
            span_qi_area.extend(list(range(all_span_qi_list[i][0], all_span_qi_list[i][1] + 1)))
        for i in range(len(all_span_qi_list)-1, -1, -1):
            span_list = self.search_all("\n", self.py[all_span_qi_list[i][0]:all_span_qi_list[i][1]+1])
            span_list = [ind + all_span_qi_list[i][0] for ind in span_list]
            span_list = [all_span_qi_list[i][0]] + span_list + [all_span_qi_list[i][1]]
            for j in range(len(span_list)-1):
                if j == 0: # 頭
                    all_span_qi_list.append([span_list[j], span_list[j+1]-1 , "str"])
                elif j == len(span_list)-2: # 尾
                    all_span_qi_list.append([span_list[j]+1, span_list[j+1] , "str"])
                else:
                    all_span_qi_list.append([span_list[j]+1, span_list[j+1]-1 , "str"])
            del all_span_qi_list[i]

        # 紀錄單行字串引號位置
        dqi_list = list() # double quotation index list (記錄雙引號位置)
        sqi_list = list() # single quotation index list (記錄單引號位置)
        for j in range(len(self.py)):
            if self.py[j] in "\"\'" and self.py[j-1] != "\\" and j not in self.colored: # 跳過「\'」、「\"」字元
                if j in span_qi_area:
                    continue
                else:
                    if self.py[j] == "\"": dqi_list.append(j) # 紀錄雙引號位置
                    else: sqi_list.append(j) # 紀錄單引號位置
        # 處理 2 雙引包 1 單引(或反之)
        all_list = sorted(sqi_list + dqi_list + self.search_all("\n", self.py))
        split_list = list()
        start = 0
        for i in range(len(all_list)):
            if self.py[all_list[i]]=="\n":
                split_list.append(all_list[start:i])
                start = i + 1
        for line in split_list:
            if len(line) >= 3:
                for j in range(len(line)-2):
                    if self.py[line[j]] == self.py[line[j+2]] and \
                        self.py[line[j]] != self.py[line[j+1]]:
                        if self.py[line[j+1]] == "\"":
                            dqi_list.remove(line[j+1])
                        else:
                            sqi_list.remove(line[j+1])

        # 因引號為兩兩一組出現，故把 list 分割為兩兩一組
        # (因註解與2包1和「\'」、「\"」已處理完，在程式碼無 SyntaxError 前提下，可直接分兩兩一組)
        dqi_list = [[dqi_list[j], dqi_list[j+1], "str"] for j in range(0, len(dqi_list), 2)]
        sqi_list = [[sqi_list[j], sqi_list[j+1], "str"] for j in range(0, len(sqi_list), 2)]
        # 若某單引號包裹著雙引號，或者反之，則必須把被包裹的引號對刪除，只保留外部的引號對
        for d in range(len(dqi_list)):
            for s in range(len(sqi_list)):
                compare = [dqi_list[d][0] , dqi_list[d][1], sqi_list[s][0], sqi_list[s][1]]
                # 若某對引號被包裹，則此區塊會將它們的值改為 [None, None]
                # 若無兩對比較引號皆不為 None，且無互相包裹情況，則不做任何處理
                if None not in compare:
                    if compare[0] < compare[2] < compare[3] < compare[1]:
                        sqi_list[s][0] = sqi_list[s][1] = None
                    elif compare[2] < compare[0] < compare[1] < compare[3]:
                        dqi_list[d][0] = dqi_list[d][1] = None
        # 將為 [None, None] 的引號對刪除
        # (因屬於 for 迴圈，要走訪並刪除就必須反向讀取，避免 IndexError)
        for d in range(len(dqi_list)-1, -1, -1):
            if dqi_list[d][0] == None:
                del dqi_list[d]
        for s in range(len(sqi_list)-1, -1, -1):
            if sqi_list[s][0] == None:
                del sqi_list[s]
        
        qi_list = sorted(dqi_list + sqi_list + all_span_qi_list)
        # 處理 f-string 內的{}
        for i in range(len(qi_list)-1, -1, -1):
            start = qi_list[i][0]
            end = qi_list[i][1]

            # 跳過 f-string 內的雙大括號
            py_copy = self.py[:].replace("{{", "🧡🧡").replace("}}", "🌟🌟")
            if py_copy[start-1] == "f" and "{" in py_copy[start:end+1] and "}" in py_copy[start:end+1]:
                sign_list = list()
                for j in range(len(py_copy[start:end+1])):
                    if py_copy[start + j] in "\"\'{}":
                        sign_list.append([start + j, py_copy[start + j]])
                for j in range(len(sign_list)-1):
                    cur_ind  = sign_list[j][0]
                    cur      = sign_list[j][1]
                    next_ind = sign_list[j+1][0]
                    next     = sign_list[j+1][1]
                    if cur in "\"\'" and next == "{":
                        if cur_ind + 1 == next_ind: continue
                        if j != 0: cur_ind += 1
                        next_ind -= 1
                    elif cur == "}" and next in "\"\'":
                        cur_ind += 1
                    elif cur == "}" and next == "{":
                        if cur_ind + 1 == next_ind: continue
                        cur_ind += 1
                        next_ind -= 1
                    elif cur in "\"\'" and next in "\"\'":
                        if j!=0: cur_ind += 1
                    else:
                        continue
                    qi_list.append([cur_ind, next_ind, "str"])
                    # [[1, 20, 'str'], [26, 36, 'str']]
                del qi_list[i]
        # 加入著色列表
        for qi in qi_list:
            self.add_coloring(qi)
            # 處理 f-string 的 f
            f_ind = qi[0] - 1
            if self.py[f_ind] == "f":
                self.add_coloring([f_ind, f_ind, "keyword1"])
    def find_type(self): # 尋找型別(class='module')
        sign = "\n ,()[]{}"
        self.add_coloring_and_detect_sign(self.type_list, sign, "module")
    def find_module(self): # 尋找模組(class='module')
        import_list = ["import", "from", "as", "*", ""] # 尋找匯入模組的關鍵字列表

        py_copy = "".join(self.py)
        py_copy = py_copy.split("\n")
        py_copy = [line for line in py_copy if "import" in line]
        py_copy = [item for line in py_copy for item in line.split()]

        for i in range(len(py_copy)-1, -1, -1):
            if "." in py_copy[i]:
                py_copy.extend(py_copy[i].split("."))
                del py_copy[i]

        for f in py_copy:
            m = ""
            for s in f:
                if s.isalpha() or s.isdigit() or s == "_": m += s
            self.module_list.append(m)
        self.module_list = [m for m in list(set(self.module_list)) if m not in import_list]

        sign = " \n.,()" # 模組名稱前後合法字元
        self.add_coloring_and_detect_sign(self.module_list, sign, "module")
    def find_class(self): # 尋找類別(class='module')
        for ind in self.search_all("class", self.py):
            start = ind + len("class")
            done = False
            while True:
                if self.is_name(self.py[start], first = True):
                    end = start
                    while True:
                        if not self.is_name(self.py[end], first = False):
                            done = True
                            break
                        end += 1
                if done:
                    break
                start += 1
            self.class_list.append(self.py[start:end])

        sign = " \n=:()[]{}"
        self.add_coloring_and_detect_sign(self.class_list, sign, "module")
    def find_func(self): # 尋找內建函式(class='func')
        sign = " \n+-*/%=[](){}"
        self.add_coloring_and_detect_sign(self.func_list, sign, "func")
    def find_def(self): # 尋找自訂函式(class='func')
        for ind in self.search_all("def", self.py):
            start = ind + len("def")
            done = False
            while True:
                if self.is_name(self.py[start], first = True):
                    end = start
                    while True:
                        if not self.is_name(self.py[end], first = False):
                            done = True
                            break
                        end += 1
                if done:
                    break
                start += 1
            self.def_list.append(self.py[start:end])

        sign = " \n+-*/%=.[](){}"
        self.add_coloring_and_detect_sign(self.def_list, sign, "func")
    def find_keyword(self): # 尋找關鍵字(class='keyword1' and 'keyword2')
        sign = " \n:"
        self.add_coloring_and_detect_sign(self.keyword_list1, sign, "keyword1")
        self.add_coloring_and_detect_sign(self.keyword_list2, sign, "keyword2")
    def find_bool_and_None(self): # 尋找布林值和空值(class='keyword1')
        sign = " \n:()[]{}="
        self.add_coloring_and_detect_sign(self.bool_list, sign, "keyword1")
    def find_lt(self): # 尋找 < 的 HTML格式(class='op')
        for lt in self.search_all("&lt", self.py):
            self.add_coloring([lt, lt+2, "op"])
    def find_op(self): # 尋找運算符號(class='op')
        self.add_coloring_at_single_char(self.op_list, "op")
    def find_brackets(self): # 尋找括號(class='brackets')
        self.add_coloring_at_single_char(self.brackets_list, "brackets")
    def find_number(self): # 尋找數字(class='number')
        sign = [' ', '\n', ':', '+', '-', '*', '/', '%', '=', ',', '(', ')', '[', ']', '{', '}', '>']
        detected = False
        for i in range(len(self.py)):
            if self.is_number(self.py[i]) and (self.py[i-1] in sign or self.py[i-3:i] == "&lt"):
                start = i
                detected = True
            if detected:
                if self.is_number(self.py[i]) and (self.py[i + 1] in sign or self.py[i+1:i+4] ==  "&lt"):
                    end = i
                    data = [start, end, "number"]
                    self.add_coloring(data)
                    detected = False
    def add_span(self): # 加入所有 span 標籤
        self.coloring_list.sort(reverse=True)
        for loc in self.coloring_list:
            start = loc[0]
            end = loc[1] + 1
            Class = loc[2]
            self.py = f"{self.py[:start]}<span class='{Class}'>{self.py[start:end]}</span>{self.py[end:]}"
    def add_html_exception(self): # 將程式碼內空格轉換為 HTML 格式
        py_list = []
        py_copy = self.py[:]
        while py_copy!="": # 重複執行到全部切分完
            if "<span" not in py_copy: # 若此區塊無 <span (或已切分完)則直接 pop 到 new_file_list
                py_list.append(py_copy)
                break
            start = py_copy.find("<span") # 抓取最前面的 <span
            end = py_copy.find("</span>") + 7 # 抓取最前面的 </span>
            py_list.append(py_copy[:start]) # 將 <span 前的區塊切分進 new_file_list
            py_list.append(py_copy[start:end]) # 將 <span></span> 切分進 new_file_list
            py_copy = py_copy[end:] # 將以上處理完的區塊刪除，往下輪 while 處理

        
        for i in range(len(py_list)-1, -1, -1):
            # # 刪除切分多餘的空元素
            # if py_list[i] == "":
            #     del py_list[i]
            # 將不在 span 標籤內的空字元轉為 HTML 格式(否則連續空格會被縮成一個空格)
            if not py_list[i].startswith("<span"):
                py_list[i] = py_list[i].replace(" ", "&nbsp")
            # 將在字串 span 標籤內的 < 轉為 HTML 格式(否則會被誤認為標籤符號)
            if py_list[i].startswith("<span class='str'>"):
                if "<" in py_list[i][19:-8]: # WHY?
                    py_list[i] = py_list[i][:19] + py_list[i][19:-8].replace("<", "&lt") + py_list[i][-8:]
                if py_list[i][20:-8].startswith(" "):
                    py_list[i] = py_list[i][:19] + py_list[i][19:-8].replace(" ", "&nbsp") + py_list[i][-8:]
        self.py = "".join(py_list)
    def to_html(self):
        self.py = self.py.split("\n")
        self.py = self.py[1:-1]
        # exec(f"db = client.Homework_{hwn}")  # 選擇操作 website 資料庫 (website 自行定義資料庫名稱)
        db = client.Homework_4
        collection = db.Comment_Memery
        result = collection.find_one({"StudentID":self.id})
        # print(result)
        if result != None:
            comment_by = []
            comment_time = []
            comment = []
            text = ""
            cursor = collection.find()
            # print(cursor)
            for i in cursor:
                if i["StudentID"] == self.id:
                    name = i["Name"]
                    student_dict = i["Comment_detail"]
            for k,v in student_dict.items():
                for i in v:
                    comment_by.append(k)
                    comment_time.append(i["Comment_Time"])
                    comment.append(i[f"Comment"])

            for i in range(len(comment)):
                comment[i] = comment[i].replace("<br><br>", "<br>")
                text += f"""<tr><td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;background-color: white;">{comment_time[i]}</td>
                        <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;background-color: white;">{comment_by[i]}</td>
                        <td style="border-color:#000;border-width:1px;border-style:solid;padding:5px;background-color: white;">{comment[i]}</td></tr>"""
            # print(text)

        HTML = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>記憶體程式碼</title>
                <style type="text/css">
                    .CommenT {font:100% verdana,arial,sans-serif;margin: auto;padding: 0;min-width: 500px;max-width: 600px;width: 560px; height:280px;top:0; bottom:0; left:0; right:0;}
                    table {border-spacing: 0;width: 100%;}
                    input{outline-style: none ;border: 5px solid #ccc; border-radius: 3px; border-color: #965ca1;padding: 14px 14px;width: 565px;font-size: 24px;font-family: consolas;}
                    body {font-family: consolas;background-color: #37464a;color:black}
                    .main {width: 80%;margin: 50px auto;}
                    .code {border-collapse: collapse;color: #9cdcfe;background-color:#1a1b1c;width: 100%}
                    .table_num {text-align: right;width: 40px;color: grey}
                    .keyword1 {color: #569cd6}
                    .keyword2 {color: #c586c0}
                    .op {color: #d4d4d4}
                    .func {color: #dcdcaa}
                    .str {color: #ce9178}
                    .comment {color:#6a9955;font-style:italic}
                    .brackets {color:#ffd700}
                    .module {color:#4ec9b0}
                    .number {color:#b5cea8}
                    .but {text-align: center;width: 300px;min-height: 60px;display: block;background-color: #4a77d4;border: 1px solid #3762bc;color: #fff;padding: 9px 14px;font-size: 15px;line-height: normal;border-radius: 5px;margin: 10px auto;cursor: pointer;}
                    .cmt {text-align: center;width: 150px;min-height: 40px;display: block;background-color: #4a77d4;border: 1px solid #3762bc;color: #fff;padding: 9px 14px;font-size: 15px;line-height: normal;border-radius: 5px;margin: 10px auto;cursor: pointer;}
                </style>
            </head>
            <body>
            """
            
        HTML += "<table class='code'>"
        for i in range(len(self.py)):
            HTML += "<tr>"
            HTML += f"<td class='table_num'>{i+1}</td>"
            HTML += f"<td width='10px'></td>"
            HTML += f"<td>{self.py[i]}</td>"
            HTML += "</tr>"
        HTML += "</table></br>"

        if result != None:
            HTML += """
            <div class="main">
                <table style="border-collapse:collapse;word-break:keep-all;white-space:nowrap;font-size:22px;">
                    <tr style="color:#fff;background-color:#48a6fb;font-size:22px;">
                        <th rowspan="1" style="border-color:#000;border-width:1px;border-style:solid;padding:15px;">時間</th>
                        <th rowspan="1" style="border-color:#000;border-width:1px;border-style:solid;padding:15px;">留言人</th>
                        <th rowspan="1" style="border-color:#000;border-width:1px;border-style:solid;padding:15px;">留言內容</th>
                    </tr>
            """+ text + "</table></div>"

        HTML += """
        <form class="CommenT" action="/Memerycodepage", method="POST">
            <textarea cols="48" rows="8" maxlength="100" name="Comment" required="required" style="border:5px purple double; font-size:20px;color:blue;"></textarea></br>
            <button class="cmt">提交留言</button>
        </form>
        <table border="3" width="300px" height="100px" style="border-color:#555858;" class="tabbut">
            <tr style="text-align: center;">
                <td bgcolor="#37464a">
                    <form action="/codereview" style="display:inline-block;"><button class="but" style="font-size: 23px;">程式碼審查清單</button></form>
                    <form action="/member" style="display:inline-block;"><button class="but" style="font-size: 23px;">返回會員首頁</button></form>
                </td>
            </tr>
        </table>
        </body></html>
        """
        return HTML
        
    def search_all(self, target, s): # 搜尋 py 檔內所有指定字串的 index
        return [_.start() for _ in re.finditer(target, s)]
    def add_coloring(self, data): # 新增著色區塊
        # 參數 data 格式 [頭索引 int, 尾索引 int, 著色名稱 str]
        start = data[0]
        end = data[1]
        # 若該區塊已被占用則不加入著色
        if (start in self.colored or end in self.colored):
            return
        # 若未被占用則加入到 self.coloring_list，並在 self.colored 內標註已占用
        else:
            self.coloring_list.append(data)
            self.colored.extend([i for i in range(start, end + 1)])
    def add_coloring_and_detect_sign(self, target_list, sign, class_name): # 新增著色區塊同時偵測左右字元
        for t in target_list:
            for start in self.search_all(t, self.py):
                end = start + len(t) - 1
                if self.py[start - 1] in sign and self.py[end + 1] in sign:
                    data = [start, end, class_name]
                    self.add_coloring(data)
    def add_coloring_at_single_char(self, target_list, class_name): # 新增單字元著色區塊
        for i in range(len(self.py)):
            if self.py[i] in target_list:
                data = [i, i, class_name]
                self.add_coloring(data)
    def is_name(self, s, first): # 確認是否為合法命名
        if first:
            return s.isalpha() or s == "_"
        else:
            return s.isdigit() or s.isalpha() or s == "_"
    def is_number(self, s): # 確認是否為數字(int float 皆可判斷)
        return s.isdigit() or s == "."


def memery_read_python_file(filename, id, hwn): 
    now = os.getcwd()
    pth = PythonToHTML(f"{filename}.py", hwn, id)
    html = pth.main()
    #-----------------------------------------------------#
    os.chdir("./templates")
    sys.dont_write_bytecode = True
    sys.path.append(os.getcwd())
    #-----------------------------------------------------#
    with open("Memerycodepage.html", "w", encoding="utf-8") as f:
        f.write(html)
        os.chdir(now)
    # print("---------------------------------------------")
