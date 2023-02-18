def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if len(Str) < 100:
        if len(Str)<2:  #若字串長度小於2(即字串中只有一個字或沒有字)則符合迴文條件
            return True
        if Str[0]!=Str[-1]: #檢查字串頭尾是否相同
            return False
        else: 
            return homework_4(Str[1:-1])    #若字串頭尾相同，則刪除頭尾再執行一次function
    else:
        compare = ''.join(reversed(Str[-100:]))
        if Str[0:100] != compare:
            return False
        else:
            return homework_4(Str[100:-100])
s
if __name__ == '__main__':
    Str =   "zY0uvtxsegVfr9trasaOexrq18hjkZhzjbgg27jWeqxfhjjAg36pfhwbdUebz45wtviZlwxpe54rzTyqlrijzK63yeyidjmJyh72fjdvkPebpq81hevXzjcvag90rDfmwksmcVe99capxvjLwrm108zdglFwtirm117asJqqgwtmvJ126oochcduVbk135juwtzDmfxu144ofeKwxpjjz153wKwsncbhzTh162ukbsqrUwsi171ynssSvyloh180tpCnywbmsnN189rvubomiFlc198hdfbaPlhnf207crdCyupsru216fSwaqnwmlHx225suksjoIdpn234kfjhLpgtoh243yhQhryislyV252jymbesiAuc261izrykJwpih270kfsJwvqtpp279xKasipifrVf288thkpycGyal297yoeyKoohew306quPwhsoztbJ315sroxwkpCwl324hnjbyHrgyl333hquWqiwsop342sHfazyrgqNh351vqotclSagp360fdipUxxznt369wgNhcomndtD378ppbdjyhBej387joowhOzygv396sipIdmestn405hUgsxhgzlEn414qnclcqMsem423ldcqRtwpsf432jbNdeyrzocH441twjejunAek450ypzqdNdluy459lpuZxbmbtb468nJrdmdrqqCv477kuixnxKher486yirjMqsvtn495pwKftcjluiT504hgalnbnQsm513tvtpgCyjos522gsnTdfxatp531jSzlifhleJs540pcflupUpxw549dqbpXcrhwq558shIvhpyfthX567cfiXaXifc765XhtfyphvIhs855qwhrcXpbqd945wxpUpulfcp045sJelhfilzSj135ptaxfdTnsg225sojyCgptvt315msQnbnlagh405TiuljctfKwp594ntvsqMjriy684rehKxnxiuk774vCqqrdmdrJn864btbmbxZupl954yuldNdqzpy054keAnujejwt144HcozryedNbj234fspwtRqcdl324mesMqclcnq414nElzghxsgUh504ntsemdIpis693vgyzOhwooj783jeBhyjdbpp873DtdnmochNgw963tnzxxUpidf063pgaSlctoqv153hNqgryzafHs243poswiqWuqh333lygrHybjnh423lwCpkwxors513JbtzoshwPuq603wehooKyeoy792layGcypkht882fVrfipisaKx972pptqvwJsfk072hipwJkyrzi162cuAisebmyj252VylsiyrhQhy342hotgpLhjfk432npdIojskus522xHlmwnqawSf612urspuyCdrc702fnhlPabfdh891clFimobuvr981NnsmbwynCpt081holyvSssny171iswUrqsbku261hTzhbcnswKw351zjjpxwKefo441uxfmDztwuj531kbVudchcoo621JvmtwgqqJsa711mritwFlgdz801mrwLjvxpac99eVcmskwmfDr09gavcjzXveh18qpbePkvdjf27hyJmjdiyey36KzjirlqyTzr45epxwlZivtw54zbeUdbwhfp63gAjjhfxqeWj72ggbjzhZkjh81qrxeOasart9rfVgesxtvu0Yz"
    print(homework_4(Str))
    