import xlrd
import xlwt
from xlutils import copy
import settings

book: xlrd.book.Book = None


"""获取excel文件预备存储的id信息
    @:param None
"""
def getId():
    global book
    book = xlrd.open_workbook(settings.FILE_NAME)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    for row in range(settings.START_INDEX,nrows):
        yield (row,sheet.cell(row,settings.SUBMIT_INDEX).value)



"""将爬到的信息写回
    @:param tagetBook:写入非默认的excel文件
"""

def modifyContents(targetBook=None):
    if targetBook is None:
        global book
        new_book = copy.copy(book)
    else:
        new_book = copy.copy(targetBook)
    sheet = new_book.get_sheet(0)

    while True:
        try:
            row,col,content = yield
            sheet.write(row,col,content)
            new_book.save("db.xls")
        except Exception:
            new_book.save("db.xls")