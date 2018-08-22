#run pip install xlwt
import xlwt
from xlwt import Workbook
i18nFile= open("i18n.properties")
row = 1
wb = Workbook()
sheet = wb.add_sheet('Sheet1')
style = xlwt.easyxf('font: bold 1')
for _ in i18nFile:
    arr = _.strip()
    if(arr[0]=="#"):
        continue
    length = 0
    key_value = [arr[:arr.find("=")].rstrip()] + arr[arr.find("=")+1:].lstrip().split("~|~")
    value = key_value[:len(key_value)-1]
    if(key_value[0]=="Key"):
        for i in range(len(value)):
            sheet.write(0,i,value[i],style)
    for i in range(len(value)):
        sheet.write(row,i,value[i])
    row = row+1
wb.save("i18n.xls")
i18nFile.close()