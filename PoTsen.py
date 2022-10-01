# 初始化資料庫連線
import os
import time
from werkzeug.utils import secure_filename  # 過濾檔案名稱
import pymongo  # 資料庫
from testing import ans  # 計算成績
from autohtml import Html  # 輸出排名
import pandas as pd
from autocodereview import reviewHtml  # 輸出 review 表單 
from timeoutputpythonfile import time_read_python_file  # 輸出時間程式碼和留言系統
from memeryoutputpythonfile import memery_read_python_file  # 輸出記憶體程式碼和留言系統
from autostudenthtml import studentHtml  # 生成學生後臺數據
from savecomment import get_comment_and_show  # 儲存學生的留言

# import shutil  # 刪除檔案

client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system   # 資料庫
collection = db.member  # 集合
print("資料庫連線建立成功")

# 載入 Flask 所有的相關工具
from flask import *
app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "any string but secret"
#----------------------------------------------------#
app.jinja_env.auto_reload = True  # 更新靜態文件
app.config['TEMPLATES_AUTO_RELOAD'] = True
#----------------------------------------------------#

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/member")
def member():
    cursor = collection.find()  # 取得所有資料的 cursor 物件
    for i in cursor:
        if i["StudentID"] == session["StudentID"]:
            name = i["Name"]
    if "StudentID" in session:
        return render_template("member.html", message = f"{session['StudentID']}{name}")
    else:
        return redirect("/")

@app.route("/forgetpassword")
def forgetpassword():
    return render_template("forgetpassword.html")

@app.route("/reflash", methods=["POST"])
def reflash():
    # 從前端接收資料
    nickname = request.form["nickname"]
    smallname = request.form["smallname"]
    studentid = request.form["studentid"]
    password = request.form["password"]
    string = changepassword(nickname, studentid, smallname, password)
    return render_template("error.html", message=string)  # 彈性帶入資料

# /error?msg=錯誤訊息
@app.route("/error")
def error():
    msg = request.args.get("msg", "發生錯誤,請聯繫客服!")
    return render_template("error.html", message=msg)  # 彈性帶入資料

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/signup", methods=["POST"])
def signup():
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
    else:return redirect("/error?msg=請正確輸入您的學號!")
    return redirect("/error?msg=恭喜~註冊成功!")

@app.route("/signin", methods=["POST"])
def signin():
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
def signout():
    # 移除 Session 中的會員資訊
    del session["StudentID"]
    return redirect("/")
    
@app.route("/rank1")
def rank1():
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank1.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/rank2")
def rank2():
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank2.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/rank3")
def rank3():
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank3.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/goupload")
def goupload():
    # 顯示上傳檔案的頁面
    if "StudentID" in session:
        msg = request.args.get("msg", "尚未上傳檔案!")
        return render_template("goupload.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/codereview")
def codereview():
    if "StudentID" in session:
        create_codereview_sheet()
        return render_template("codereview.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/Timecodepage", methods=["GET", "POST"])
def Timecodepage():
    global File_Name, Student_ID, date
    if request.method == "GET":
        if "StudentID" in session:
            File_Name = request.args.get("msg")
            File_Name = str(File_Name)
            Student_ID = (File_Name.split('_')[0].split('s'))[1]
            # print(File_Name, I_D, hwn, "Time")
            time_read_python_file(File_Name, Student_ID, hwn)
            return render_template("Timecodepage.html")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")
    else:
        if "StudentID" in session:
            comment = request.form["Comment"]
            # print(comment)
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cursor = collection.find()
            for i in cursor:
                if i["StudentID"] == session["StudentID"]:
                    comment_by = i["Name"]
                if i["StudentID"] == Student_ID:
                    name = i["Name"]
                    memery_file = i["Memery_file"]
                    time_file = i["Time_file"]
                    memery = i["Memery"]
                    Time = i["Time"]
                    frequency = i["Frequency"]
            comment = comment.replace("\n", "<br>").replace("\r", "<br>")
            get_comment_and_show(name, Student_ID, File_Name, date, comment_by, comment, hwn, memery, Time, memery_file, time_file, frequency, "Time")
            time_read_python_file(File_Name, Student_ID, hwn)
            # read_python_file(File_Name, Student_ID, hwn, "Time")
            # print(name, File_Name, date, comment_by, comment)
            return render_template("Timecodepage.html")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/Memerycodepage", methods=["GET", "POST"])
def Memerycodepage():
    global FILE_NAME, STUDENT_ID, DATE
    if request.method == "GET":
        if "StudentID" in session:
            FILE_NAME = request.args.get("msg")
            FILE_NAME = str(FILE_NAME)
            STUDENT_ID = (FILE_NAME.split('_')[0].split('s'))[1]
            # print(FILE_NAME, STUDENT_ID, hwn)
            memery_read_python_file(FILE_NAME, STUDENT_ID, hwn)
            return render_template("Memerycodepage.html")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")
    else:
        if "StudentID" in session:
            comment = request.form["Comment"]
            DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cursor = collection.find()
            for i in cursor:
                if i["StudentID"] == session["StudentID"]:
                    comment_by = i["Name"]
                if i["StudentID"] == STUDENT_ID:
                    name = i["Name"]
                    memery_file = i["Memery_file"]
                    time_file = i["Time_file"]
                    memery = i["Memery"]
                    Time = i["Time"]
                    frequency = i["Frequency"]
            comment = comment.replace("\n", "<br>").replace("\r", "<br>")
            get_comment_and_show(name, STUDENT_ID, FILE_NAME, DATE, comment_by, comment, hwn, memery, Time, memery_file, time_file, frequency, "Memery")
            memery_read_python_file(FILE_NAME, STUDENT_ID, hwn)
            # read_python_file(File_Name, Student_ID, hwn, "Time")
            # print(name, File_Name, date, comment_by, comment)
            return render_template("Memerycodepage.html")
        else:
            return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/teachingassistant")
def teachingassistant():
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            return render_template("teachingassistant.html")
        else:
            return redirect("/membererror?msg=這裡是助教專區!請止步謝謝~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/studentdata")
def studentdata():
    if "StudentID" in session:
        if session["StudentID"] == "1104813":
            create_student_data()  # 創建學生後臺數據
            return render_template("studentdata.html")
        else:
            return redirect("/membererror?msg=這裡是助教專區!請止步謝謝~")
    else:
        return redirect("/membererror?msg=尚未登入!請先登入謝謝~")

@app.route("/opensmallname")
def opensmallname():
    pass

@app.route("/unopensmallname")
def unopensmallname():
    pass

#--------------------------------------------------------------------------------#    函式區塊

def createSheet():
    sheet_Ori = [[i["StudentID"], i["Name"], i["Time"], i["Memery"]] for i in collection.find() if "Time" in i]
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
    

def TimeMemery(id, time, memery, score):  # 寫入時間複雜度和空間複雜度
    if score == 100:
        cursor = collection.find()
        # print(id, time, memery, score)
        for i in cursor:
            if "Frequency" in i:
                if i["StudentID"] == id:
                    try:
                        if i["Time"] < time:
                            time = i["Time"]
                        else:
                            collection.update_one({
                                "StudentID":id
                            }, {
                                "$set":{
                                    "Time_file":f"s{id}_{i['Frequency']}"
                                }
                            })
                    except KeyError:pass
                    try:
                        if i["Memery"] < memery:
                            memery = i["Memery"]
                        else:
                            collection.update_one({
                                "StudentID":id
                            }, {
                                "$set":{
                                    "Memery_file":f"s{id}_{i['Frequency']}"
                                }
                            })
                    except KeyError:pass
            else:
                collection.update_many({
                    "StudentID":id
                }, {
                    "$set":{
                        "Time_file":f"s{id}_0",
                        "Memery_file":f"s{id}_0"
                    }
                })
        result = collection.update_many({
            "StudentID":id
        }, {
            "$set":{
                "Time":time,
                "Memery":memery
            }
        })
        print(f"符合篩選條件的文件數量(TimeMemery):{result.matched_count}")
        print(f"實際符合更新的文件數量(TimeMemery):{result.modified_count}")


def uploadCount(id, score):  # 計算上傳次數
    if score == 100:
        cursor = collection.find()
        for i in cursor:
            if i["StudentID"] == id:
                if "Frequency" not in i:
                    result = collection.update_one({
                        "StudentID":id
                    }, {
                        "$set":{
                            "Frequency":1
                        }
                    })
                    print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
                    print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")
                    break
                else:
                    result = collection.update_one({  # 利用 'StudentID':學號 當搜尋目標 ;再用 '$inc' (加 or 減) 想要的資料
                        "StudentID":id
                    }, {
                        "$inc":{
                            "Frequency":1  # '1' 代表原本數字加 1
                        }
                    })
                    print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
                    print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")
                    break

def check_student_dir(student_file, hw_num):
    first = os.getcwd()
    lst = os.listdir(f"file/hw{hw_num}")
    last = os.chdir(f"./file/hw{hw_num}")
    if student_file not in lst:os.mkdir(student_file)
    os.chdir(first)

def check_student_file_rename(studentid, filename, hw_num, freqency):
    first = os.getcwd()
    os.chdir(f"./file/hw{hw_num}/{studentid}")
    os.rename(filename, f"s{studentid}_{freqency}.py")
    os.chdir(first)
    return f"s{studentid}_{freqency}.py"

def create_codereview_sheet():  # 創建程式碼審查表單
    review_sheet = []
    cursor = collection.find()
    for i in cursor:
        # print(i)
        review_sheet.append([i["StudentID"], i["Name"], "未上傳", "未上傳"])

    for rs in range(len(review_sheet)):
        review_sheet[rs] = tuple(review_sheet[rs])
    review_sheet = tuple(review_sheet)

    reviewHtml(review_sheet)

def create_student_data():
    student_sheet = []
    cursor = collection.find()
    for i in cursor:
        print(i)
        if "Time_file" in i and "Memery_file" in i:
            student_sheet.append([i["StudentID"], i["Name"], "暱稱", i["Frequency"], i["Time_file"], i["Memery_file"]])
        else:
            if "Frequency" in i:
                student_sheet.append([i["StudentID"], i["Name"], "暱稱", i["Frequency"], "未上傳檔案", "未上傳檔案"])
            else:
                student_sheet.append([i["StudentID"], i["Name"], "暱稱", "0", "未上傳檔案", "未上傳檔案"])
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

ALLOWED_EXTENSIONS = set(['py'])  # 限制檔案格式
def allowed_file(filename):
    return '.' in filename and \
           filename.split('.', 1)[1] in ALLOWED_EXTENSIONS

#--------------------------------------------------------------------------#

hwn = "4"
@app.route("/upload", methods=["POST"])
def upload():
    check_student_dir(session["StudentID"], hwn)
    UPLOAD_FOLDER = f'C:/Users/user/Desktop/論文/Membership system/file/hw{hwn}/{session["StudentID"]}'
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  # 存放的資料夾
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制檔案大小 "16MB"
    file = request.files["file"]
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    else:return redirect("/membererror?msg=檔案錯誤,請重新上傳!")
    cursor = collection.find()
    for i in cursor:
        if i["StudentID"] == session["StudentID"]:
            # try:
            if "Frequency" in i:
                filename = check_student_file_rename(session["StudentID"], filename, hwn, str(i["Frequency"]))
                break
            else:
                filename = check_student_file_rename(session["StudentID"], filename, hwn, "0")
                break
            # except UnboundLocalError:return redirect("/membererror?msg=未選擇檔案,請重新上傳!")
    # print(filename)
    Score, Time, Memery = ans(session["StudentID"], filename, hwn)
    TimeMemery(session["StudentID"], Time, Memery, Score)  # Time and Memery 寫入資料庫
    # print(session["StudentID"])
    uploadCount(session["StudentID"], Score)  # 計算上傳次數
    return render_template("membererror.html", message="成功上傳!", Score=f"分數:{Score}", Time=f"時間:{Time}ms", Memery=f"記憶體:{Memery}KB")
    # return render_template("membererror.html")

@app.route("/membererror")
def membererror():
    msg = request.args.get("msg", "發生錯誤,請聯繫助教!")
    return render_template("membererror.html", message=msg)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
