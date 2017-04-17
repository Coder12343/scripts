import xlrd

data = xlrd.open_workbook('test.xls')
wprksheets = data.sheet_names()
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
	if i == 0:
		continue
	print(table.row_values(i)[:13])



import xlwt

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
sheet1.write(0,0,'asdf')
sheet1.write(0,1,'wer')
workbook.save('C:\\asdf.xls')



import xlutils.copy

rb = xlrd.open_workbook("...")
wb = xlutils.copy.copy(rb)
#获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
ws = wb.get_sheet(0)
ws.write(1,1,'asdf')
wb.add_sheet('sheet2',cell_overwrite_ok=True)
#利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
wb.save('...')




# 读取excel
def read_excel(path):
	data = xlrd.open_workbook(path)
	worksheets = data.sheet_names()
	for sheet_name in worksheets:
		sheet = data.sheet_by_name(sheet_name)
		nrows = sheet.nrows
		for i in range(nrows):
			print(sheet.row_values(i))




