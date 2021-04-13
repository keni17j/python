import sys
import os
import openpyxl
import numpy as np


def main():

    # open
    wb = openpyxl.Workbook() # create a new workbook
    #file_path = input("--> ")
    #wb = openpyxl.load_workbook(file_path, data_only=True) # load the workbook

    # select the worksheet
    ws = wb.active # active sheet
    #ws_name = wb.sheetnames[0] # get the sheet name
    #ws = wb[ws_name] # select by the sheet name

    write(ws)
    read(ws)
    edit(wb, ws)
    graph(wb, ws)

    # save
    wb.save("test.xlsx")

    # close
    wb.close()
    sys.exit()


def write(ws):

    # write a data
    # method 1
    ws["A1"].value = 1
    # method 2
    ws.cell(row=1, column=2, value=2)

    # write a list
    list_1d = [3, 4, 5, 6, 7]
    ws.append(list_1d)
    list_2d = [[8, 9, 10, 11, 12], [13, 14, 15, 16, 17]]
    for i in list_2d: ws.append(i)


def read(ws):

    # read from the cell
    # method 1
    val = ws["A1"].value
    print(val)
    # method 2
    val = ws.cell(row=1, column=2).value
    print(val)
    # read from in the range
    val = ws["A1:D4"]
    val = [[j.value for j in i] for i in val] # convert to the value
    for i in val: print(i)


def edit(wb, ws):

    # cell style
    # fill
    ws["A1"].fill = openpyxl.styles.PatternFill(patternType="solid", fgColor="ffaaaa")
    # format
    ws["A1"].number_format = "0.00"
    # font
    ws["B1"].font = openpyxl.styles.Font(size=20, bold=True, italic=True, color="0000ff")

    # sheets
    # title
    ws.title = "test_sheet"
    # add a new sheet
    ws_add = wb.create_sheet(title="new_sheet", index=0)
    # copy the sheet
    ws_copy = wb.copy_worksheet(ws_add)
    # delete the sheet
    wb.remove(ws_add)
    wb.remove(ws_copy)


def graph(wb, ws):

    # create a new sheet
    ws = wb.create_sheet(title="graph")
    # write x,y datas
    n = 10 # number of datas = n-1
    x = np.arange(1,n)
    y1 = np.random.randint(1,10,(n-1))
    y2 = np.random.randint(10,20,(n-1))
    data = np.vstack((x, y1, y2))
    data = data.transpose()
    data = np.vstack((np.array(["x", "y1", "y2"]), data))
    for i in data.tolist(): ws.append(i)

    # draw a scatter graph
    chart = openpyxl.chart.ScatterChart()
    # titles
    chart.title = "scatter graph"
    chart.x_axis.title = "x_axis"
    chart.y_axis.title = "y_axis"
    # select values
    xval = openpyxl.chart.Reference(ws, min_col=1, min_row=2, max_row=10)
    yval = openpyxl.chart.Reference(ws, min_col=2, min_row=2, max_row=10)
    series = openpyxl.chart.Series(yval, xval, title="sample1")
    # setting
    #series.marker.symbol = "circle"
    #series.marker.size = 10
    #series.marker.spPr.fill = "0000ff"
    chart.series.append(series)

    # add datas
    yval = openpyxl.chart.Reference(ws, min_col=3, min_row=2, max_row=10)
    series = openpyxl.chart.Series(yval, xval)
    chart.series.append(series)

    # create the graph
    ws.add_chart(chart, "D1")


if __name__ == "__main__": main()
