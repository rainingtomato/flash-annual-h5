import openpyxl
wb = openpyxl.load_workbook('商家拜访时间线.xlsx')
ws = wb.active
lines = []
for row in ws.iter_rows(min_row=2, values_only=True):
    lines.append(','.join([str(v) if v is not None else '' for v in row]))
with open('merchants.csv', 'w', encoding='utf-8') as f:
    f.write('序号,商家名称,日期,城市,备注\n')
    f.write('\n'.join(lines))
print('done')
