import requests
from excel import *
import settings

def main():
    try:
        """
            浏览器获取的cookies信息
        """

        cookies = {
            "IS_LOGIN":"true",
            "JSESSIONID":"9WvyL2oJdqRdGcpgenW0yjHlhXatvfP7WB0TvwO5qkb8fOgydJMk!-2107473049!-1769973447",
            "WEE_SID":"9WvyL2oJdqRdGcpgenW0yjHlhXatvfP7WB0TvwO5qkb8fOgydJMk!-2107473049!-1769973447!1550251420169",
            "avoid_declare":"declare_pass"
        }


        ids = getId()
        saves = modifyContents(xlrd.open_workbook(settings.TARGET_FILENAME))
        next(ids)
        next(saves)


        for row,id in ids:
            parms = {
                "searchCondition.searchExp": "CN200710133738.5",
                "search_scope": '',
                "searchCondition.dbId": "VDB",
                "resultPagination.limit": "12",
                "searchCondition.searchType": 'Sino_foreign',
                "wee.bizlog.modulelevel": "0200101"
            }
            parms["searchCondition.searchExp"] = id
            print(id,row)
            url = "http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/executeSmartSearch1207-executeSmartSearch.shtml"

            response = requests.post(url, parms, cookies=cookies)
            print(response.status_code)
            data = response.json()


            fnum = data["searchResultDTO"]["searchResultRecord"][0]["fieldMap"]["FNUM"] # "同族"
            pnum = data["searchResultDTO"]["searchResultRecord"][0]["fieldMap"]["PNUM"] #"引证"
            cpnum = data["searchResultDTO"]["searchResultRecord"][0]["fieldMap"]["CPNUM"] # "被引"
            saves.send((row,settings.TYPE2INDEX["同族"],fnum))
            saves.send((row, settings.TYPE2INDEX["引证"], pnum))
            saves.send((row, settings.TYPE2INDEX["被引"], cpnum))
            print("写入的行数是:",row)
            print("正在写入的id:",id,"写入(同族，引证，被引)成功!")



            #法律相关
            Pn = data["searchResultDTO"]["searchResultRecord"][0]["fieldMap"]["PN"] # 公开号Pn
            vid = data["searchResultDTO"]["searchResultRecord"][0]["fieldMap"]["VID"] #申请号
            parms2 = {
                "lawState.nrdAn": "", #id An
                "lawState.nrdPn": "", #公开号Pn
                "pagination.start":"0",
                "wee.bizlog.modulelevel": "0202201"
            }
            parms2["lawState.nrdAn"] = vid
            parms2["lawState.nrdPn"] = Pn
            url2 = "http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/ui_searchLawState-showPage.shtml"
            response2 = requests.post(url2, parms2, cookies=cookies)
            print(61,response2.status_code)
            data2 = response2.json()
            lawStateList = data2["lawStateList"]

            for law_state in lawStateList:
                if law_state["lawStateCNMeaning"] and law_state["lawStateCNMeaning"].strip() in settings.TYPE2INDEX:
                    saves.send((row,settings.TYPE2INDEX[law_state["lawStateCNMeaning"]],law_state["prsDate"]))
            print("写入法律相关成功!")
            print("\n*************************************************************************************\n")

    except Exception:
        settings.START_INDEX = row-3
        main()


main()