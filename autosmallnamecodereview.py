from HTMLTable import HTMLTable
# 載入 pymongo 套件
# import pymongo
import os
# 連線到 MongoDB 雲端資料庫
# client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")

def smallnamereviewHtml(rows, collection):
    # 標題
    table = HTMLTable()
    # 表頭行
    table.append_header_rows((
        ('編號', '程式碼' , ''),
        (    '', '時間', '記憶體'),
    ))
    # 合併單元格
    table[0][0].attr.rowspan = 2
    table[0][1].attr.colspan = 2

    # 資料行

    exec(f"table.append_data_rows({rows})")

    # 標題樣式  
    table.caption.set_style({
        'color': '#fff',
        'font-size': '30px',
    })
    # 表格樣式，即</table><table>標籤樣式
    table.set_style({
        'border-collapse': 'collapse',
        'word-break': 'keep-all',
        'white-space': 'nowrap',
        'font-size': '22px',
    })
    # 統一設定所有單元格樣式，<tbody><tr><td>或</td><th>
    table.set_cell_style({
        'border-color': '#000',
        'border-width': '1px',
        'border-style': 'solid',
        'padding': '5px',
    })
    # 表頭樣式
    table.set_header_row_style({
        'color': '#fff',
        'background-color': '#48a6fb',
        'font-size': '22px',
    })

    # 覆蓋表頭單元格字型樣式
    table.set_header_cell_style({
        'padding': '15px',
    })
    # 調小次表頭字型大小
    table[1].set_cell_style({
        'padding': '8px',
        'font-size': '20px',
    })
    # ---------------------------------------------------------------- # 

    html = table.to_html()  # 字串
    html = list(html)
    # print(html[html.index("未")+87:html.index("未")+87+3])
    
    # print(html[html.index("未")+91:html.index("未")+3+91])
    cursor = collection.find()
    cursor_list = sorted(list(cursor), key=lambda x:x["Number"])
    for dic in cursor_list:
        idx = html.index("未")

        if "Time_file" in dic:
            html[idx:idx+3] = [f"<a href='/codepage/Time/{str(dic['_id'])}'>程式碼</a>"]
        else:
            if "Not_perfect_time_file" in dic:
                html[idx:idx+3] = [f"<a href='/codepage/Time/{str(dic['_id'])}'>程式碼</a>"]
            else:
                html[idx:idx+3] = ["沒有完成"]

        if "Memory_file" in dic:
            html[idx+87-2:idx+87+3-2] = [f"<a href='/codepage/Memory/{str(dic['_id'])}'>程式碼</a>"]
        else:
            if "Not_perfect_memory_file" in dic:
                html[idx+87-2:idx+87+3-2] = [f"<a href='/codepage/Memory/{str(dic['_id'])}'>程式碼</a>"]
            else:
                html[idx+87-2:idx+87+3-2] = ["沒有完成"]
    
    html = ''.join(html)

    final_html = """
    <!DOCTYPE html>

    <head>
        <meta charset='UTF-8'>
        <title>程式碼審查</title>
        <style type="text/css">
            .main {
                width: 80%;
                margin: 20px auto;
                background-color: #ffffff
            }
            table {border-spacing: 0;width: 100%;}
            tr {text-align: center;}
            th {padding: 10px;}
            table tbody tr:nth-child(odd){background-color: #eee}
            table thead {background-color: blue;color: white;}
            table thead th:first-child {border-radius: 5px 0 0 0;border: 1px solid blue;}
            .but{text-align: center;width: 300px;min-height: 60px;display: block;background-color: #4a77d4;border: 1px solid #3762bc;color: #fff;padding: 9px 14px;font-size: 15px;line-height: normal;border-radius: 5px;margin: 10px auto;}
        </style>
    </head>

    <body style='background-color: #37464a;'>
        <table border="3" width="300px" height="100px" style="border-color:#555858;">
            <tr>
                <td bgcolor="#37464a">
                    <form action="/codereviewsheet" style="display:inline-block;"><button class="but"style="font-size: 23px;">查看審查名單</button></form>
                    <form action="/member" style="display:inline-block;"><button class="but"style="font-size: 23px;">返回會員首頁</button></form>
                </td>
            </tr>
        </table>
        <div class='main'>
        """ + html + """
        </div>
    </body>

    </html>
    """
    # final_html = f"<!DOCTYPE html><head><meta charset='UTF-8'><link href='RANK.css' rel='stylesheet' type='text/css' /><title>排名</title></head><body style='background-color: #37464a;'><form action='/rank1'><button class='but'>總表</button></form><form action='/rank2'><button class='but'>時間排名</button></form><form action='/rank3'><button class='but'>記憶體排名</button></form><form action='/member'><button class='but'>返回會員首頁</button></form><div class='main'>{html}</div></body></html>"
    final_html = final_html.replace("'", "\"")
    # print(final_html)
    # print("--------------------------------")
    path = "C:\\Users\\lab70829\\Desktop\\Membership system"
    os.chdir(path)
    # print(os.getcwd())
    # # print("--------------------------------")
    with open(f"templates/codereview.html", "w", encoding="utf-8") as file:
        file.write(final_html)

