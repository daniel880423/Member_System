def homework_4(Str): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    if Str == "": #處理到最後剛剛好變成空字串
        return True
    if len(Str) >= 10:
        if Str[0] == Str[-1]:
            if Str[1] == Str[-2]:
                if Str[2] == Str[-3]:
                    if Str[3] == Str[-4]:
                        if Str[4] == Str[-5]:
                            Str = Str[5:-5]
                            return homework_4(Str)
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif len(Str) < 10:
        if len(Str) < 8:
            if len(Str) < 6:
                if len(Str) < 4:
                    if len(Str) == 1:
                        return True
                    else:
                        if Str[0] == Str[-1]:
                            return True
                        else:
                            return False
                else:
                    if Str[0] == Str[-1]:
                        if Str[1] == Str[-2]:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                if Str[0] == Str[-1]:
                    if Str[1] == Str[-2]:
                        if Str[2] == Str[-3]:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            if Str[0] == Str[-1]:
                if Str[1] == Str[-2]:
                    if Str[2] == Str[-3]:
                        if Str[3] == Str[-4]:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False



if __name__ == '__main__':
    Str = "gT0csstmecHid9alhrwAjcak18lscOwogpwe27eUxxzhuboGr36szjixgUxjt45myquKtsevp54enZpnkrcuwS63jnqrypiSxd72bnzofEbgfr81wosPdqeiwb90tBmjrwmnyEl99zexoxvRjdh108vpmjIyetxa117umQpirrfvbP126sfftbdyEak135mhzomZxplb144azuPkbtask153aGtbhohqaLh162lcxdqoDqha171cpndKnibcm180ldDjjbllseE189jwpdwgpZgj198gdtohGwnhz207atkKpkrtne216iPrxjqnanCc225xdxklpAmmo234quleFuulfi243npCepcnrchG252duhmsezDtv261jmtqpJlswu270rmyOwgwkzt279mUapzmjtwRi288yhgkubTqvo297exxgKpkgro306qzYpgmdctsS315zrzuhbcFrx324ngqubGkcwe333aokUiunrkd342sFhxqbwpxHh351kwcjkfCnai360atizDebten369zoFetzexdwQ378jujszbyMeu387dojxfJvrkz396mkoVujmkch405oLjzynmckQs414tknoivLlil423pjajBicvyw432vdYlqrzughO441kfglqkwAry450axlwaBsdtf459icpEgoqjmn468nIxtqooegEz477iotgsaDemv486rwmfIrvkkk495hmRuxxlttnI504ceyojrrLgv513xwgmtPykzo522hnfPmhgdkg531wAknhelkuGz540nscnwdKjcv549bngwGezwad558bsZmgpkyixD567suffqkzHor576hfewbKgjzi585bbtFnaryhe594zIzagtasnGc603yrjkquOekr612hjbdFnqiov621fcDcgzgfdgN630tukbfddBmx639zcxaqShgxy648iqeIudgkbw657mRmuwvnsyYn666xphbldCfti675pzidWbppxx684dqMdoxvebuP693xkhkepkFsl702tckkoMeeuj711atsAmgyhqh720tSdwagrhoAw729xiyvlqNftj738dpixKahcof747ebBltusozrS756fyajnveQcs765cqyqtQrsdd774yvkFpulgqy783zEeonugvsBe792renhpwLztb801ybuyMelxtk810vvVohrcnnkY819wxphtadZth828cshvnVipwo837dioRqrqcpl846rXfurjazrGh855qkensxFyim864mcidFhjunq873wgWlmcetwvH882kwqjdlrCer891ttzcpSzlau900hitUddfkin909rUikiqglcKv918weamabNalg927dykaAkigre936zgPgtbtequE945fevyimhHjd954ioixbSlvpj963kupXvpqswm972kVscmfzdpOo981jztpfuRaap990jqiuKfaxmz999fsUjjdrpsaH1008ppcxlnyLtu1017kywluRuvln1026bdnThrjepj1035kGjdlzujxKe1044sbkafqFnej1053ksjvOhhcuu1062sxTgiznugxE1071vhlzxpcIjk1080uflhdIyeqs1089vzpYnixsqb1098sAnenbrpcAs1107jsjxfqVyuh1116mrmrMzkmil1125cvMljfumorT1134jdzcbbwDdp1143itnvkEfvkr1152tfbGkxydac1161oQfdrijqmAm1170jmpczaCtab1179erurHbmetw1188ntBsazffwhE1197lvrgalvFue1206jrkilFilhu1215vtiBwmjtvr1224lDvehqmnqQk1233evrgheBgwj1242spdhBapfmn1251hxOcnlwpukU1260nvypdvePtg1269hrjzsLzgpe1278ksvGgroras1287eVcjzonhfGd1296vebseqNpmh1305btwhExxphj1314gxHlbxhvglL1323pfxylkjKmh1332qrabxIslkt1341ykgRxmfpjr1350pAoseysxhRi1359llxzacAcjl1368vuvzZenxls1377cgLpmhhwcnU1386exjnlquYzr1395ungxvLecib1404tkpZvggsku1413eNjshsqabZl1422haqrsxZujb1431nmaaItpkxs1440feWisvcmrmN1449bwizabeGdz1458gjpbaLemhh1467uswUrwbjll1476kKbaulqgyIj1485dsxddnOlqy1494xtwyAudgdb1503diExliopchR1512chcbwnlLci1521uemaaRehfp1530bjyPfnofhj1539mZrkeqeezSb1548vbxcoxVvuq1557rvltXtbtnn1566kbBwkrcquvP1575xncahfbCun1584zompqYrdcp1593xzyVcjgruj1602nWcyhqxllHa1611jnelbfXouy1620eqnzKiwwah1629pjNghteknpJ1638ztxmrzuAvu1647hmdhyKwyne1656uwnLnvqtix1665sChnlgjlfLv1674kaktdpZaad1683wmtqIwgftv1692gxCuqciuwsT1701zqerjrdZdz1710qasjmAdfob1719rfaIzztaul1728fJfhzjqjqMz1737uspxaqJbfx1746yprqJfxtpb1755uvMurqphiqF1764muiloimIbo1773jrhokFmseh1782kxdPvotpry1791bSxdvxfpbZu1800vurzgaKdzr1809glhhNpnfyl1818vpFzmvjmpwU1827wsqsobfFjk1836epiijOftng1845hnnEohblve1854aHevcbvzrWq1863gxcrzeHcbp1872yikaIbwziv1881vuHkwjxwvoJ1890wzpjhnnWgv1899vywwrNakookaNrwwyv9981vgWnnhjpzw0981JovwxjwkHuv1881vizwbIakiy2781pbcHezrcxg3681qWrzvbcveHa4581evlbhoEnnh5481gntfOjiipe6381kjFfbosqsw7281UwpmjvmzFpv8181lyfnpNhhlg9081rzdKagzruv0081uZbpfxvdxSb1971yrptovPdxk2871hesmFkohrj3771obImiolium4671FqihpqruMvu5571bptxfJqrpy6471xfbJqaxpsu7371zMqjqjzhfJf8271luatzzIafr9171bofdAmjsaq0171zdZdrjreqz1071TswuicquCxg2961vtfgwIqtmw3861daaZpdtkak4761vLfljglnhCs5661xitqvnLnwu6561enywKyhdmh7461uvAuzrmxtz8361JpnkethgNjp9261hawwiKznqe0261yuoXfblenj1161aHllxqhycWn2061jurgjcVyzx3951pcdrYqpmoz4851nuCbfhacnx5751PvuqcrkwBbk6651nntbtXtlvr7551quvVxocxbv8451bSzeeqekrZm9351jhfonfPyjb0351pfheRaameu1251icLlnwbchc2151RhcpoilxEid3051bdgduAywtx4941yqlOnddxsd5841jIygqluabKk6741lljbwrUwsu7641hhmeLabpjg8541zdGebaziwb9441NmrmcvsiWef0441sxkptIaamn1341bjuZxsrqah2241lZbaqshsjNe3141uksggvZpkt4041biceLvxgnu5931rzYuqlnjxe6831UncwhhmpLgc7731slxneZzvuv8631ljcAcazxll9531iRhxsyesoAp0531rjpfmxRgky1431tklsIxbarq2331hmKjklyxfp3231LlgvhxblHxg4131jhpxxEhwtb5031hmpNqesbev6921dGfhnozjcVe7821sarorgGvsk8721epgzLszjrh9621gtPevdpyvn0621UkupwlncOxh1521nmfpaBhdps2421jwgBehgrve3321kQqnmqhevDl4221rvtjmwBitv5121uhliFlikrj6021euFvlagrvl7911EhwffzasBtn8811wtembHrure9711batCazcpmj0711mAmqjirdfQo1611cadyxkGbft2511rkvfEkvnti3411pdDwbbczdj4311TromufjlMvc5211limkzMrmrm6111huyVqfxjsj7011sAcprbnenAs8901bqsxinYpzv9801sqeyIdhlfu0801kjIcpxzlhv1701ExgunzigTxs2601uuchhOvjsk3501jenFqfakbs4401eKxjuzldjGk5301jpejrhTndb6201nlvuRulwyk7101utLynlxcpp8001HasprdjjUsf999zmxafKuiqj099paaRufptzj189oOpdzfmcsVk279mwsqpvXpuk369jpvlSbxioi459djHhmiyvef549EuqetbtgPgz639ergikAakyd729glaNbamaew819vKclgqikiUr909nikfddUtih009ualzSpcztt198reCrldjqwk288HvwtecmlWgw378qnujhFdicm468miyFxsnekq558hGrzajrufXr648lpcqrqRoid738owpiVnvhsc828htZdathpxw918YknncrhoVvv018ktxleMyuby108btzLwphner297eBsvgunoeEz387yqglupFkvy477ddsrQtqyqc567scQevnjayf657SrzosutlBbe747fochaKxipd837jtfNqlvyix927wAohrgawdSt027hqhygmAsta117jueeMokkct207lsFkpekhkx396PubevxodMqd486xxppbWdizp576itfCdlbhpx666nYysnvwumRm756wbkgduIeqi846yxghSqaxcz936xmBddfbkut036NgdfgzgcDcf126voiqnFdbjh216rkeOuqkjry306cGnsatgazIz495ehyranFtbb585izjgKbwefh675roHzkqffus765DxiykpgmZsb855dawzeGwgnb945vcjKdwncsn045zGuklehnkAw135gkdghmPfnh225ozkyPtmgwx315vgLrrjoyec405InttlxxuRmh594kkkvrIfmwr684vmeDasgtoi774zEgeooqtxIn864nmjqogEpci954ftdsBawlxa054yrAwkqlgfk144OhguzrqlYdv234wyvciBjajp324lilLvionkt414sQkcmnyzjLo504hckmjuVokm693zkrvJfxjod783ueMybzsjuj873QwdxezteFoz963netbeDzita063ianCfkjcwk153hHxpwbqxhFs243dkrnuiUkoa333ewckGbuqgn423xrFcbhuzrz513SstcdmgpYzq603orgkpKgxxe792ovqTbukghy882iRwtjmzpaUm972tzkwgwOymr072uwslJpqtmj162vtDzesmhud252GhcrncpeCpn342ifluuFeluq432ommAplkxdx522cCnanqjxrPi612entrkpKkta702zhnwGhotdg891jgZpgwdpwj981EesllbjjDdl081mcbinKdnpc171ahqDoqdxcl261hLaqhohbtGa351ksatbkPuza441blpxZmozhm531kaEydbtffs621PbvfrripQmu711axteyIjmpv801hdjRvxoxez99lEynmwrjmBt09bwieqdPsow18rfgbEfoznb27dxSipyrqnj36SwucrknpZne45pvestKuqym54tjxUgxijzs63rGobuhzxxUe72ewpgowOcsl81kacjAwrhla9diHcemtssc0Tg"
    print(homework_4(Str))
    