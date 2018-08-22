#run pip install xlrd datetime
import xlrd
import datetime
wb = xlrd.open_workbook("i18n.xls")
sheet = wb.sheet_by_index(0)
file = open("i18n.properties", "w")
date = datetime.datetime.now().strftime("%c")
file.write("# "+date[:-14]+''+date[-5:]+date[:-5][-9:]+" GMT+0530 (India Standard Time)\n")
for row in range(1,sheet.nrows):
    for col in range(0,sheet.ncols):
        if(col == 0):
            file.write(sheet.cell_value(row,col)+"=")
        else:
            file.write(sheet.cell_value(row,col)+"~|~")
    file.write("\n")
file.close()

