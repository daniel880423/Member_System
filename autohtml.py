from HTMLTable import HTMLTable

def Html(student):
    for i in range(len(student)):
        # 標題
        table = HTMLTable()
        # 表頭行
        if i != 0:
            table.append_header_rows((
                ('排名', '學號', '姓名', '複雜度' , ''),
                (    '',   '',     '', '花費時間(s)', '記憶體使用量(MB)'),
            ))
            # 合併單元格
            table[0][0].attr.rowspan = 2
            table[0][1].attr.rowspan = 2
            table[0][2].attr.rowspan = 2
            table[0][3].attr.colspan = 2
        else:
            table.append_header_rows((
                ('學號', '姓名', '複雜度' , ''),
                (   '',     '', '花費時間(s)', '記憶體使用量(MB)'),
            ))
            # 合併單元格
            table[0][0].attr.rowspan = 2
            table[0][1].attr.rowspan = 2
            table[0][2].attr.colspan = 2

        # 資料行

        exec(f"table.append_data_rows({student[i]})")

        # table.append_data_rows((
        #     ('1','孟柏岑', '1104813', 10, 0.5),
        #     ('2','張培元', '1104807', 15, 0.1),
        #     ('3','詹育森', '1094815', 20, 0.08)
        # ))

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
            'font-size': '30px',
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
            'font-size': '18px',
        })

        # 覆蓋表頭單元格字型樣式
        table.set_header_cell_style({
            'padding': '15px',
        })
        # 調小次表頭字型大小
        table[1].set_cell_style({
            'padding': '8px',
            'font-size': '15px',
        })
        # ---------------------------------------------------------------- # 

        html = table.to_html()  # 字串
        final_html = "<!DOCTYPE html><head><meta charset='UTF-8'><link href='RANK.css' rel='stylesheet' type='text/css' /><title>排名</title><style typer='text/css'>nav{display:flex;text-align:center;position: fixed;}nav>.l{flex:auto}</style></head><body style='background-color: #37464a;'><nav><div class='l'><form action='/rank1'><button class='but'>總表</button></form><form action='/rank2'><button class='but'>時間排名</button></form><form action='/rank3'><button class='but'>記憶體排名</button></form><form action='/member'><button class='but'>返回會員首頁</button></form></div></nav><div class='main'>"+html+"</div></body></html>"
        final_html = final_html.replace("'", "\"")
        with open(f"templates/rank{i+1}.html", "w", encoding="utf-8") as file:
            file.write(final_html)