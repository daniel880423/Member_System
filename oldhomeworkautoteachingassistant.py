import os
def oldteachingassistanthtml(hw_num): 
    html = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>最高權限</title>
        <style type="text/css">
            table {{border-spacing: 0;width: 100%;}}
            tr {{text-align: center;}}
            th {{padding: 10px;}}
            table tbody tr:nth-child(odd) {{background-color: #eee}}
            table thead {{background-color: blue;color: white;}}
            table thead th:first-child {{border-radius: 5px 0 0 0;border: 1px solid blue;}}
            .but {{text-align: center;width: 300px;min-height: 60px;display: block;background-color: #4a77d4;border: 1px solid #3762bc;color: #fff;padding: 9px 14px;font-size: 15px;line-height: normal;border-radius: 5px;margin: 10px auto;cursor: pointer;}}
        </style>
    </head>

    <body style="background-color: #315e49;">
        <div style="text-align:center;">
            <h1 style="color: rgb(47, 2, 66);">助教專用網站</h1></br>
        </div>
        <table border="3" width="300px" height="100px" style="border-color:#555858;">
            <tr>
                <td bgcolor="#37464a">
                    <form action="/oldhomeworkstudentdata/{hw_num}" style="display:inline-block;"><button class="but" style="font-size: 23px;">學生後臺數據</button></form>
                    <form action="/oldhomeworkmember/{hw_num}" style="display:inline-block;"><button class="but" style="font-size: 23px;">返回會員首頁</button></form>
                    <form action="/signout" style="display:inline-block;"><button class="but" style="font-size: 23px;">登出</button></form>
                </td>
            </tr>
        </table>
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
    with open(f"templates/oldhomework{hw_num}teachingassistant.html", "w", encoding="utf-8") as file:
        file.write(final_html)