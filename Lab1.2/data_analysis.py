from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']


def getvalue(x):
    return x.value

list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['C'][1:]))
list_z = list(map(getvalue, sheet['D'][1:]))


pyplot.plot(list_x, list_y, label='Метка1')
pyplot.plot(list_x, list_z, label='Метка2')
pyplot.legend()
pyplot.show()
