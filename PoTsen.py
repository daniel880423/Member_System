# 初始化資料庫連線
import os, sys
import time
from werkzeug.utils import secure_filename  # 過濾檔案名稱
import pymongo  # 資料庫
from testing import ans  # 計算成績
from autohtml import Html  # 輸出排名
import pandas as pd
from autocodereview import reviewHtml  # 輸出 review 表單 
from autosmallnamecodereview import smallnamereviewHtml  # 輸出 smallname review 表單 
from automistake import checkmistakeHtml  # 輸出錯誤題目表單
from outputpythonfile import read_python_file  # 輸出時間和記憶體程式碼和留言系統 / 複製程式碼
from autostudenthtml import studentHtml  # 生成學生後臺數據
from savecomment import get_comment_and_show  # 儲存學生的留言
from notperfectsavecomment import not_perfect_get_comment_and_show  # 儲存沒有滿分學生的留言
from bson.objectid import ObjectId  # 以 ObjectID 作為目標
from random import sample  # 隨機生成編號

#----------------------------------------------------# 自定義變數
Anonymous_message = True  # 匿名開關
Code_review_comment = True  # 程式碼審查開關
Upload_file = False  # 上傳作業開關
hwn = "1"  # 作業編號
ALLOWED_EXTENSIONS = set(['py'])  # 限制檔案格式
First_Path = "C:\\Users\\user\\Desktop\\論文\\Membership system"  # 首頁目錄
#----------------------------------------------------# 自定義變數

client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system   # 資料庫
collection = db.member  # 集合
# print("資料庫連線建立成功")
exec(f"db_homework = client.Homework_{hwn}")
collection_homework = db_homework.member
collection_comment_time = db_homework.Comment_Time
collection_comment_memory = db_homework.Comment_Memory

#----------------------------------------------------#

# 載入 Flask 所有的相關工具
from flask import *
app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "any string but secret"
#----------------------------------------------------# 熱更新 html 檔案
app.jinja_env.auto_reload = True  # 更新靜態文件
app.config['TEMPLATES_AUTO_RELOAD'] = True
#----------------------------------------------------# 熱更新 html 檔案

#----------------------------------------------------#   路由 route
@app.route("/")
def index():  # 首頁
    return render_template("home.html")

@app.route("/member")
def member():  # 會員頁面
    cursor = collection_homework.find()  # 取得所有資料的 cursor 物件
    if session["StudentID"] != "1104813":
        for i in cursor:
            if i["StudentID"] == session["StudentID"]:
                name = i["Name"]
                number = i["Number"]
                break
    else:
        name = "助教-孟柏岑"
        number = 0
    if "StudentID" in session:
        return render_template("member.html", message = f"{session['StudentID']}-{name}", msg = f"審查編號:{number}")
    else:
        return redirect("/")

@app.route("/forgetpassword")
def forgetpassword():  # 更改密碼頁面
    return render_template("forgetpassword.html")

@app.route("/reflash", methods=["POST"])
def reflash():  # 更改密碼處理
    # 從前端接收資料
    nickname = request.form["nickname"]
    smallname = request.form["smallname"]
    studentid = request.form["studentid"]
    password = request.form["password"]
    string = changepassword(nickname, studentid, smallname, password)
    return render_template("error.html", message=string)  # 彈性帶入資料

@app.route("/error")
def error():  # 要求字串頁面
    # /error?msg=錯誤訊息
    msg = request.args.get("msg", "發生錯誤,請聯繫客服!")
    return render_template("error.html", message=msg)  # 彈性帶入資料

@app.route("/membererror")
def membererror():  # 會員要求字串頁面
    msg = request.args.get("msg", "發生錯誤,請聯繫助教!")
    return render_template("membererror.html", message=msg)

@app.route("/register")
def register():  # 註冊頁面
    return render_template("register.html")

@app.route("/signup", methods=["POST"])
def signup():  # 註冊
    # 從前端接收資料
    nickname = request.form["nickname"]
    smallname = request.form["smallname"]
    studentid = request.form["studentid"]
    password = request.form["password"]
    if studentid.isdecimal() and len(studentid) == 7:
        result_1 = collection.find_one({  # 檢查學號是否相同
            "StudentID":studentid
        })
        if result_1 != None:
            return redirect("/error?msg=學號已經被註冊!")
        result_2 = collection.find_one({  # 檢查學號是否相同
            "Smallname":smallname
        })
        if result_2 != None:
            return redirect("/error?msg=暱稱已經被使用!")
        collection.insert_one({
            "Name":nickname,
            "StudentID":studentid,
            "Smallname":smallname,
            "Password":password
        })
        collection_homework.insert_one({
            "Name":nickname,
            "StudentID":studentid,
            "Smallname":smallname,
        })
    else:return redirect("/error?msg=請正確輸入您的學號!")
    return redirect("/error?msg=恭喜~註冊成功!")

@app.route("/signin", methods=["POST"])
def signin():  # 登入
    # 從前端取得使用者輸入
    studentid = request.form["studentid"]
    password = request.form["password"]
    result = collection.find_one({
        "$and":[
            {"StudentID":studentid,
            "Password":password}
        ]
    })
    # 如果沒有找到對應資料, 代表沒有註冊
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤!")
        # return render_template("home.html", name="帳號或密碼輸入錯誤!")
    # 登入成功, 在 Session 紀錄會員資訊, 並導向到會員頁面
    session["StudentID"] = result["StudentID"]
    return redirect("/member")

@app.route("/signout")
def signout():  # 登出
    # 移除 Session 中的會員資訊
    del session["StudentID"]
    return redirect("/")
    
@app.route("/rank1")
def rank1():  # 總表
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank1.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/rank2")
def rank2():  #　時間排名
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank2.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/rank3")
def rank3():  #　記憶體排名
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank3.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/goupload")
def goupload():  # 上傳頁面
    # 顯示上傳檔案的頁面
    if "StudentID" in session:
        if Upload_file:
            if session["StudentID"] != "1104813":
                cursor = collection_homework.find()
                for i in cursor:
                    if i["StudentID"] == session["StudentID"]:
                        if "Frequency" in i:
                            upload_freq = i["Frequency"]
                            break
                        else:
                            upload_freq = 0
                            break
            else:upload_freq = 0
            # msg = request.args.get("msg", "尚未上傳檔案!")
            return render_template("goupload.html", message = f"上傳次數:{upload_freq}")
        else:
            return redirect("/membererror?msg=此功能尚未開放!")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/upload", methods=["POST"])
def upload():  # 上傳檔案後的處理 (成績 / 複雜度 / 上傳次數)
    check_student_dir(session["StudentID"])  # 創建學生作業資料夾
    UPLOAD_FOLDER = f'C:/Users/user/Desktop/論文/Membership system/file/hw{hwn}/{session["StudentID"]}'
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  # 存放的資料夾
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制檔案大小 "16MB"
    file = request.files["file"]
    file_name = str(file.filename).split('.py')[0]
    if file and allowed_file(file.filename) and (session["StudentID"] == file_name):  # 儲存學生上傳的檔案
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    else:return redirect("/membererror?msg=檔案錯誤,請重新上傳!")
    cursor = list(collection_homework.find())
    for i in cursor:
        if i["StudentID"] == session["StudentID"]:
            # if "Frequency" in i:
            #     filename = check_student_file_rename(session["StudentID"], filename, hwn, str(i["Frequency"]))
            #     break
            # else:
            #     filename = check_student_file_rename(session["StudentID"], filename, hwn, "0")
            #     break
            freq = 0
            if "Frequency" in i:
                freq = str(i["Frequency"])
            filename = check_student_file_rename(session["StudentID"], filename, hwn, freq)
            break
    # print(filename)
    Score, Time, Memory, Sheet = ans(session["StudentID"], filename, hwn)  # 計算分數 , 時間 , 記憶體
    TimeMemory(session["StudentID"], Time, Memory, Score)  # Time and Memory 寫入資料庫
    uploadCount(session["StudentID"])  # 計算上傳次數
    # print(session["StudentID"])
    if Score == 100:
        return render_template("membererror.html", message="成功上傳!", Score=f"分數:{Score}", Time=f"時間:{Time}ms", Memory=f"記憶體:{Memory}KB")
    else:
        create_checkmistake_sheet(Sheet)
        return render_template("uploaderror.html", message="成功上傳!", Score=f"分數:{Score}", Time=f"時間:----ms", Memory=f"記憶體:----KB")

@app.route("/codereview")
def codereview():  # 程式碼審查表格頁面
    if "StudentID" in session:
        if Code_review_comment:  # 判斷是否開啟程式碼審查
            if Anonymous_message:
                create_smallname_codereview_sheet()
                return render_template("codereview.html")
            else:
                create_codereview_sheet()
                return render_template("codereview.html")
        else:
            return render_template("membererror.html", message="此功能尚未開放!")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/codereviewsheet")
def codereviewsheet():  # 顯示審查清單
    if "StudentID" in session:
        return render_template("codereviewsheet.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/Timecodepage", methods=["GET", "POST"])
def Timecodepage():  # 時間程式碼頁面
    # exec(f"global File_Name{'3'}, STUDENT_id{'3'}")
    global File_Name, STUDENT_id
    cursor = collection_homework.find()
    if Anonymous_message:
        ojid = request.args.get("msg")  # 取得此程式碼的暱稱 
        if ojid != None:   
            for i in cursor:
                if i["_id"] == ObjectId(ojid):
                    
                    if "Time_file" in i:
                        File_Name = i["Time_file"]
                        Name = i["Name"]
                        break
                    elif "Not_perfect_time_file" in i:
                        File_Name = i["Not_perfect_time_file"]
                        Name = i["Name"]
                        break
            File_Name = str(File_Name)
            STUDENT_id = (File_Name.split('_')[0].split('s'))[1]
            # copy_time_file(File_Name, hwn, STUDENT_id)  # 生成複製程式碼頁面
            read_python_file(File_Name, STUDENT_id, hwn, Name, Anonymous_message, collection_comment_time, "Time", True)  # 生成複製程式碼頁面
    else:
        FN = request.args.get("msg")  # 取得此程式碼的檔名
        if FN != None:
            File_Name = FN
            File_Name = str(File_Name)
            STUDENT_id = (File_Name.split('_')[0].split('s'))[1]
            for i in cursor:
                if i["StudentID"] == STUDENT_id:
                    Name = i["Name"]
            # copy_time_file(File_Name, hwn, STUDENT_id)  # 生成複製程式碼頁面
            read_python_file(File_Name, STUDENT_id, hwn, Name, Anonymous_message, collection_comment_time, "Time", True)  # 生成複製程式碼頁面
    if request.method == "GET":
        if "StudentID" in session:
            if Code_review_comment:  # 判斷是否開啟程式碼審查
                read_python_file(File_Name, STUDENT_id, hwn, Name, Anonymous_message, collection_comment_time, "Time")
                return render_template("Timecodepage.html")
            else:
                return render_template("membererror.html", message="此功能尚未開放!")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")
    else:
        if "StudentID" in session:
            comment = request.form["Comment"]
            comment = comment.replace("\n", "<br>").replace("\r", "<br>")
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            for i in cursor:
                if i["StudentID"] == session["StudentID"]:
                    comment_by = i["Name"]
                    smallname = i["Smallname"]
                    break
            cursor = collection_homework.find()  # cursor 一旦使用過必須重新呼叫 ***********************************************
            for i in cursor:
                if i["StudentID"] == STUDENT_id:
                    if "Time_file" in i and "Memory_file" in i:
                        name = i["Name"]
                        memory_file = i["Memory_file"]
                        time_file = i["Time_file"]
                        memory = i["Memory"]
                        Time = i["Time"]
                        frequency = i["Frequency"]
                        if Anonymous_message:  # 判斷匿名是否開啟
                            get_comment_and_show(name, STUDENT_id, File_Name, date, smallname, comment, hwn, memory, Time, memory_file, time_file, frequency, "Time")
                        else:
                            get_comment_and_show(name, STUDENT_id, File_Name, date, comment_by, comment, hwn, memory, Time, memory_file, time_file, frequency, "Time")
                        break               
                    else:
                        name = i["Name"]
                        not_perfect_memory_file = i["Not_perfect_memory_file"]
                        not_perfect_time_file = i["Not_perfect_time_file"]
                        frequency = i["Frequency"]
                        if Anonymous_message:  # 判斷匿名是否開啟
                            not_perfect_get_comment_and_show(name, STUDENT_id, File_Name, date, smallname, comment, hwn, not_perfect_memory_file, not_perfect_time_file, frequency, "Time")
                        else:
                            not_perfect_get_comment_and_show(name, STUDENT_id, File_Name, date, comment_by, comment, hwn, not_perfect_memory_file, not_perfect_time_file, frequency, "Time")
                        break
            read_python_file(File_Name, STUDENT_id, hwn, name, Anonymous_message, collection_comment_time, "Time")
            # return redirect(f"/Timecodepage?msg={sn}")
            return render_template("Timecodepage.html")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/Memorycodepage", methods=["GET", "POST"])
def Memorycodepage():  # 記憶體程式碼頁面
    global FILE_NAME, STUDENT_ID
    cursor = collection_homework.find()
    if Anonymous_message:
        ojid = request.args.get("msg")  # 取得此程式碼的暱稱
        if ojid != None:
            for i in cursor:
                if i["_id"] == ObjectId(ojid):
                    if "Memory_file" in i:
                        FILE_NAME = i["Memory_file"]
                        Name = i["Name"]
                        break
                    elif "Not_perfect_memory_file" in i:
                        FILE_NAME = i["Not_perfect_memory_file"]
                        Name = i["Name"]
                        break
            FILE_NAME = str(FILE_NAME)
            STUDENT_ID = (FILE_NAME.split('_')[0].split('s'))[1]
            # copy_memory_file(FILE_NAME, hwn, STUDENT_ID)  # 生成複製程式碼頁面
            read_python_file(FILE_NAME, STUDENT_ID, hwn, Name, Anonymous_message, collection_comment_memory, "Memory", True)  # 生成複製程式碼頁面
    else:
        FN = request.args.get("msg")  # 取得此程式碼的檔名
        if FN != None:
            FILE_NAME = FN
            FILE_NAME = str(FILE_NAME)
            STUDENT_ID = (FILE_NAME.split('_')[0].split('s'))[1]
            for i in cursor:
                if i["StudentID"] == STUDENT_ID:
                    Name = i["Name"]
            # copy_memory_file(FILE_NAME, hwn, STUDENT_ID)  # 生成複製程式碼頁面
            read_python_file(FILE_NAME, STUDENT_ID, hwn, Name, Anonymous_message, collection_comment_memory, "Memory", True)  # 生成複製程式碼頁面
    if request.method == "GET":
        if "StudentID" in session:
            if Code_review_comment:  # 判斷是否開啟程式碼審查
                read_python_file(FILE_NAME, STUDENT_ID, hwn, Name, Anonymous_message, collection_comment_memory, "Memory")
                return render_template("Memorycodepage.html")
            else:
                return render_template("membererror.html", message="此功能尚未開放!")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")
    else:
        if "StudentID" in session:
            comment = request.form["Comment"]
            comment = comment.replace("\n", "<br>").replace("\r", "<br>")
            DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            for i in cursor:
                if i["StudentID"] == session["StudentID"]:
                    comment_by = i["Name"]
                    smallname = i["Smallname"]
                    break
            cursor = collection_homework.find()  # cursor 一旦使用過必須重新呼叫 ***********************************************
            for i in cursor:
                if i["StudentID"] == STUDENT_ID:
                    if "Time_file" in i and "Memory_file" in i:
                        name = i["Name"]
                        memory_file = i["Memory_file"]
                        time_file = i["Time_file"]
                        memory = i["Memory"]
                        Time = i["Time"]
                        frequency = i["Frequency"]
                        if Anonymous_message:  # 判斷匿名是否開啟
                            get_comment_and_show(name, STUDENT_ID, FILE_NAME, DATE, smallname, comment, hwn, memory, Time, memory_file, time_file, frequency, "Memory")
                        else:
                            get_comment_and_show(name, STUDENT_ID, FILE_NAME, DATE, comment_by, comment, hwn, memory, Time, memory_file, time_file, frequency, "Memory")
                        break
                    else:
                        name = i["Name"]
                        not_perfect_memory_file = i["Not_perfect_memory_file"]
                        not_perfect_time_file = i["Not_perfect_time_file"]
                        frequency = i["Frequency"]
                        if Anonymous_message:  # 判斷匿名是否開啟
                            not_perfect_get_comment_and_show(name, STUDENT_ID, FILE_NAME, DATE, smallname, comment, hwn, not_perfect_memory_file, not_perfect_time_file, frequency, "Memory")
                        else:
                            not_perfect_get_comment_and_show(name, STUDENT_ID, FILE_NAME, DATE, comment_by, comment, hwn, not_perfect_memory_file, not_perfect_time_file, frequency, "Memory")
                        break
            read_python_file(FILE_NAME, STUDENT_ID, hwn, name, Anonymous_message, collection_comment_memory, "Memory")
            return render_template("Memorycodepage.html")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/teachingassistant")
def teachingassistant():  # 助教頁面
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            return render_template("teachingassistant.html")
        else:
            return redirect("/membererror?msg=這裡是助教專區!請止步謝謝~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/studentdata")
def studentdata():  # 顯示學生後台數據
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            create_student_data()  # 創建學生後臺數據
            return render_template("studentdata.html")
        else:
            return redirect("/membererror?msg=這裡是助教專區!請止步謝謝~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/opensmallname")
def opensmallname():  # 開啟匿名留言
    global Anonymous_message
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            Anonymous_message = True  # 開啟匿名留言
            return render_template("teachingassistanterror.html", message="成功開啟匿名留言~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/unopensmallname")
def unopensmallname():  # 關閉匿名留言
    global Anonymous_message
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            Anonymous_message = False  # 關閉匿名留言
            return render_template("teachingassistanterror.html", message="成功關閉匿名留言~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/opencodereviewcomment")
def opencodereviewcomment():  # 打開審查留言
    global Code_review_comment
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            Code_review_comment = True  # 開啟程式碼審查
            return render_template("teachingassistanterror.html", message="成功開啟程式碼審查~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/unopencodereviewcomment")
def unopencodereviewcomment():  # 關閉審查留言
    global Code_review_comment
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            Code_review_comment = False  # 關閉程式碼審查
            return render_template("teachingassistanterror.html", message="成功關閉程式碼審查~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/Timecopyfile")
def Timecopyfile():   # 給學生複製時間程式碼
    return render_template("Copytimecodepage.html")

@app.route("/Memorycopyfile")
def Memorycopyfile():   # 給學生複製記憶體程式碼
    return render_template("Copymemorycodepage.html")

@app.route("/checkmistake")
def checkmistake():   # 給學生確認錯誤題目
    if "StudentID" in session:
        return render_template("checkmistake.html")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/openuploadfile")
def openuploadfile():  # 打開上傳檔案按鈕
    global Upload_file
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            Upload_file = True  # 開啟上傳檔案
            return render_template("teachingassistanterror.html", message="成功開啟上傳檔案~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/unopenuploadfile")
def unopenuploadfile():  # 關閉上傳檔案按鈕
    global Upload_file
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            Upload_file = False  # 關閉上傳檔案
            return render_template("teachingassistanterror.html", message="成功關閉上傳檔案~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/Assignnumber")
def Assignnumber():  # 新增學生編號按鈕
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            randomcodereviewnumber()
            return render_template("teachingassistanterror.html", message="成功生成編號~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/Addmemberinformation")
def Addmemberinformation():
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            addstudentmemberinformation()
            return render_template("teachingassistanterror.html", message="成功新增作業資料庫~")
        else:
            return redirect("/membererror?msg=您不是助教唷,沒有權限~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

#----------------------------------------------------#    路由 route

#----------------------------------------------------#    函式區塊

def createSheet():  # 顯示排名並給獎牌
    sheet_Ori = [[i["StudentID"], i["Name"], i["Time"], i["Memory"]] for i in collection_homework.find() if "Time" in i]
    sheet_StuID = sorted(sheet_Ori, key=lambda x:x[0])
    sheet_Time = sorted(sheet_Ori, key=lambda x:x[2])
    sheet_Memory = sorted(sheet_Ori, key=lambda x:x[3])
    #====================================================================================
    who_get_medal_dict = dict()  # 儲存獎牌人
    medal_dict = {1:"🥇", 2:"🥈", 3:"🥉"}  # 獎牌字典  
    #====================================================================================
    df_Time = pd.DataFrame()
    df_Time["Rank"] = [j[2] for j in sheet_Time]
    df_rank_Time = df_Time.Rank.rank(method='min', ascending=True)
    final_rank_Time = [int(j) for j in df_rank_Time] # 將時間和記憶體做排名

    for i in range(len(sheet_Time)):
        sheet_Time[i] = [final_rank_Time[i]] + sheet_Time[i]
        if 1 <= sheet_Time[i][0] <= 3:
            stu_name = sheet_Time[i][2]
            sheet_Time[i][2] += medal_dict[sheet_Time[i][0]]
            if stu_name not in who_get_medal_dict:
                who_get_medal_dict[stu_name] = [medal_dict[sheet_Time[i][0]]]
            else:
                who_get_medal_dict[stu_name].append(medal_dict[sheet_Time[i][0]])
    #====================================================================================
    df_Memory = pd.DataFrame()
    df_Memory["Rank"] = [j[3] for j in sheet_Memory]
    df_rank_Memory = df_Memory.Rank.rank(method='min', ascending=True)
    final_rank_Memory = [int(j) for j in df_rank_Memory] # 將時間和記憶體做排名

    for i in range(len(sheet_Memory)):
        sheet_Memory[i] = [final_rank_Memory[i]] + sheet_Memory[i]
        if 1 <= sheet_Memory[i][0] <= 3:
            stu_name = sheet_Memory[i][2]
            sheet_Memory[i][2] += medal_dict[sheet_Memory[i][0]]
            if stu_name not in who_get_medal_dict:
                who_get_medal_dict[stu_name] = [medal_dict[sheet_Memory[i][0]]]
            else:
                who_get_medal_dict[stu_name].append(medal_dict[sheet_Memory[i][0]])
    #====================================================================================
    for i in range(len(sheet_StuID)):
        stu_name = sheet_StuID[i][1]
        if stu_name in who_get_medal_dict.keys():
            for medal in who_get_medal_dict[stu_name]:
                sheet_StuID[i][1] += medal
    #====================================================================================
    for i in range(len(sheet_StuID)):
        sheet_StuID[i] = tuple(sheet_StuID[i])
    sheet_StuID = tuple(sheet_StuID)
    for i in range(len(sheet_Time)):
        sheet_Time[i] = tuple(sheet_Time[i])
    sheet_Time = tuple(sheet_Time)
    for i in range(len(sheet_Memory)):
        sheet_Memory[i] = tuple(sheet_Memory[i])
    sheet_Memory = tuple(sheet_Memory)
    #====================================================================================
    return [sheet_StuID, sheet_Time, sheet_Memory]
    
def TimeMemory(id, time, memory, score):  # 寫入時間複雜度和空間複雜度
    if score == 100:
        cursor = collection_homework.find()
        for i in cursor:
            if i["StudentID"] == id:
                if "Frequency" in i:
                    if "Time" in i:
                        if i["Time"] > time:
                            result = collection_homework.update_many({
                                "StudentID":id
                            }, {
                                "$set":{
                                    "Time_file":f"s{id}_{i['Frequency']}",
                                    "Time":time
                                }
                            })
                            print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
                            print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")
                        if i["Memory"] > memory:
                            collection_homework.update_many({
                                "StudentID":id
                            }, {
                                "$set":{
                                    "Memory_file":f"s{id}_{i['Frequency']}",
                                    "Memory":memory
                                }
                            })
                    else:
                        collection_homework.update_many({
                            "StudentID":id
                        }, {
                            "$set":{
                                "Time_file":f"s{id}_{i['Frequency']}",
                                "Memory_file":f"s{id}_{i['Frequency']}",
                                "Time":time,
                                "Memory":memory,
                                "Score":f"{score}"
                            }
                        })
                else:
                    collection_homework.update_many({
                        "StudentID":id
                    }, {
                        "$set":{
                            "Time_file":f"s{id}_0",
                            "Memory_file":f"s{id}_0",
                            "Time":time,
                            "Memory":memory,
                            "Score":f"{score}"
                        }
                    })
    else:
        cursor = collection_homework.find()
        for i in cursor:
            if i["StudentID"] == id:
                if "Time_file" not in i and "Memory_file" not in i:
                    if "Frequency" in i:
                        if int(i["Score"]) < score:
                            collection_homework.update_many({
                                "StudentID":id
                            }, {
                                "$set":{
                                    "Not_perfect_time_file":f"s{id}_{i['Frequency']}",
                                    "Not_perfect_memory_file":f"s{id}_{i['Frequency']}",
                                    "Score":f"{score}"
                                }
                            })
                    else:
                        collection_homework.update_many({
                            "StudentID":id
                        }, {
                            "$set":{
                                "Not_perfect_time_file":f"s{id}_0",
                                "Not_perfect_memory_file":f"s{id}_0",
                                "Score":f"{score}"
                            }
                        })

def uploadCount(id):  # 計算上傳次數
    cursor = collection_homework.find()
    for i in cursor:
        if i["StudentID"] == id:
            if "Frequency" not in i:
                result = collection_homework.update_one({
                    "StudentID":id
                }, {
                    "$set":{
                        "Frequency":1
                    }
                })
                # print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
                # print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")
                break
            else:
                result = collection_homework.update_one({  # 利用 'StudentID':學號 當搜尋目標 ;再用 '$inc' (加 or 減) 想要的資料
                    "StudentID":id
                }, {
                    "$inc":{
                        "Frequency":1  # '1' 代表原本數字加 1
                    }
                })
                # print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
                # print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")
                break

def check_student_dir(student_file):  # 創建學生資料夾 "file/hw/studentid"
    os.chdir(First_Path)
    lst = os.listdir(f"./file/hw{hwn}")
    os.chdir(f"./file/hw{hwn}")
    if student_file not in lst:os.mkdir(student_file)
    os.chdir(First_Path)

def check_student_file_rename(studentid, filename, hw_num, freqency):  # 重新命名學生檔案 "s1104813_0"
    os.chdir(f"./file/hw{hw_num}/{studentid}")
    if os.path.isfile(f"s{studentid}_{freqency}.py"):  # 處理例外事件, 檔案重複
        os.remove(f"s{studentid}_{freqency}.py")
    os.rename(filename, f"s{studentid}_{freqency}.py")
    os.chdir(First_Path)
    return f"s{studentid}_{freqency}.py"

def create_codereview_sheet():  # 創建實名程式碼審查表單
    review_sheet = []
    cursor = collection_homework.find()
    for i in cursor:
        review_sheet.append([i["StudentID"], i["Name"], "未上傳", "未上傳"])

    for rs in range(len(review_sheet)):
        review_sheet[rs] = tuple(review_sheet[rs])
    review_sheet = tuple(review_sheet)

    reviewHtml(review_sheet, collection_homework)

def create_smallname_codereview_sheet():  # 創建匿名程式碼審查表單
    sn_review_sheet = []
    cursor = collection_homework.find()
    count = 0
    for i in cursor:
        count += 1
        sn_review_sheet.append([f"{count}", "未上傳", "未上傳"])

    for srs in range(len(sn_review_sheet)):
        sn_review_sheet[srs] = tuple(sn_review_sheet[srs])
    sn_review_sheet = tuple(sn_review_sheet)
    smallnamereviewHtml(sn_review_sheet, collection_homework)

def create_checkmistake_sheet(checkmistake_sheet):  # 創建學生錯誤題目的表單
    for rs in range(len(checkmistake_sheet)):
        checkmistake_sheet[rs] = tuple(checkmistake_sheet[rs])
    checkmistake_sheet = tuple(checkmistake_sheet)

    checkmistakeHtml(checkmistake_sheet)

def create_student_data():  # 創建後臺學生數據表單
    student_sheet = []
    cursor = collection_homework.find()
    count = 0
    for i in cursor:
        count += 1
        if "Time_file" in i and "Memory_file" in i:
            student_sheet.append([count, i["StudentID"], i["Name"], i["Smallname"], i["Frequency"], i['Score'], i["Time_file"], i["Memory_file"]])
        else:
            if "Frequency" in i:
                if "Not_perfect_time_file" in i and "Not_perfect_memory_file" in i:
                    student_sheet.append([count, i["StudentID"], i["Name"], i["Smallname"], i["Frequency"], i['Score'], i["Not_perfect_time_file"], i["Not_perfect_memory_file"]])
            else:
                student_sheet.append([count, i["StudentID"], i["Name"], i["Smallname"], "0", "目前沒分數", "未上傳檔案", "未上傳檔案"])
    for ss in range(len(student_sheet)):
        student_sheet[ss] = tuple(student_sheet[ss])
    student_sheet = tuple(student_sheet)
    studentHtml(student_sheet)

def changepassword(name, id, smallname, password):  # 更改密碼
    cursor = collection.find()
    for i in cursor:
        if name == i["Name"]:
            # print("1")
            if smallname == i["Smallname"]:
                # print("2")
                if id == i["StudentID"]:
                    # print("3")
                    if password == i["Password"]:
                        return "您輸入了舊的密碼~"
                    else:
                        # print("4")
                        result = collection.update_one({  # 利用 'name':'柏岑' 當搜尋目標 ;再用 '$set' (更新 or 添加) 想要改動的資料
                            "Name":name
                        }, {
                            "$set":{
                                "Password":password
                            }
                        })
                        print(f"符合篩選條件的文件數量:{result.matched_count}")
                        print(f"實際符合更新的文件數量:{result.modified_count}")  # 如果要更改的東西已經相同,則不會進行更改
                        return "更改密碼成功~"
                else:return "學號打錯摟!"
            else:return "暱稱錯誤!"
    return "查無此人!"

def allowed_file(filename):  # 限制檔案 (.py)
    return '.' in filename and \
           filename.split('.', 1)[1] in ALLOWED_EXTENSIONS

def randomcodereviewnumber():  # 新增編號給每位同學
    number = sample(range(1,82), 81)
    cursor = collection_homework.find()
    count = 0
    for i in cursor:
        result = collection_homework.update_one({  # 利用 'name':'柏岑' 當搜尋目標 ;再用 '$set' (更新 or 添加) 想要改動的資料
            "Name":i["Name"]
        }, {
            "$set":{
                "Number":number[count]
            }
        })
        count += 1
    # print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
    # print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")

def addstudentmemberinformation():  # 新增學生會員資訊到新作業資料庫
    cursor = collection.find()
    for i in cursor:
        if i["Name"] == "孟柏岑":continue
        collection_homework.insert_one({
            "Name":i["Name"],
            "StudentID":i["StudentID"],
            "Smallname":i["Smallname"],
        })

#----------------------------------------------------#    函式區塊

if __name__ == '__main__':
    app.run(port=3000, debug=True)
