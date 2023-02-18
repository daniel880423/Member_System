import os
def oldhomeworkautomemberhtml(hw_num):
    html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" >
                <title>舊作業{hw_num}專區</title>
                <style type="text/css">
                    html{{ width: 100%; height: 100%; overflow: hidden; font-style: sans-serif;   }}   
                    body{{ width: 100%;   height: 100%;   font-family: 'Open Sans',sans-serif;   margin: 0;   background-color: #37464a;}}
                    #login{{ position: absolute;   top: 50%;   left:50%;   margin: -150px 0 0 -150px;   width: 300px;   height: 300px;   }}   
                    #login h1{{ color: #fff;   text-shadow:0 0 10px;   letter-spacing: 5px;   text-align: center;white-space:nowrap;}}   
                    .but{{ width: 300px;   min-height: 20px;   display: block;   background-color: #4a77d4;   border: 1px solid #3762bc;   color: #fff;   padding: 9px 14px;   font-size: 15px;   line-height: normal;   border-radius: 5px;   margin: 0;   }}
                </style>
            </head>
            <body>
                <div id="login">
                    <h1>作業{hw_num}</h1>
                    <h1>{{{{ message }}}}</h1>
                    <h1>{{{{ msg }}}}</h1>
                    <form action="/oldhomeworkrank1/{hw_num}">
                        <button class="but">🏆 排行榜 🏆</button><br/>
                    </form>
                    <form action="/oldhomeworkcodereview/{hw_num}">
                        <button class="but">📄 程式碼審查 📄</button><br/>
                    </form>
                    <form action="/signout">
                        <button class="but">👋 登出 👋</button><br/>
                    </form>
                    <form action="/oldhomeworkteachingassistant/{hw_num}">
                        <button class="but">⛔ 助教專區 ⛔</button>
                    </form>
                </div>
            </body>
        </html>  
    """
    # final_html = f"<!DOCTYPE html><head><meta charset='UTF-8'><link href='RANK.css' rel='stylesheet' type='text/css' /><title>排名</title></head><body style='background-color: #37464a;'><form action='/rank1'><button class='but'>總表</button></form><form action='/rank2'><button class='but'>時間排名</button></form><form action='/rank3'><button class='but'>記憶體排名</button></form><form action='/member'><button class='but'>返回會員首頁</button></form><div class='main'>{html}</div></body></html>"
    final_html = html.replace("'", "\"")
    # print("--------------------------------")
    path = "C:\\Users\\lab70829\\Desktop\\Membership system"
    os.chdir(path)
    # print(os.getcwd())
    # print("--------------------------------")
    with open(f"templates/oldhomework{hw_num}member.html", "w", encoding="utf-8") as file:
        file.write(final_html)