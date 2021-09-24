import xlrd
from os import walk

def read_excel(addr):
    rows=[]
    loc = (addr)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0) 
    # for row in range(sheet.nrows)[::-1]:
    for row in range(sheet.nrows):
        number=int(row+1)
        name=sheet.cell_value(row, 0)
        link=sheet.cell_value(row, 1)
        link_name=link[link.rfind("/")+1::1]
        answer=sheet.cell_value(row, 2)
        if(answer!="*"):
            rows.append([number,name,link,answer,link_name,1])
    
    return rows

    # numpy.random.shuffle(remaining_rows), print(remaining_rows)
    # Extracting number of rows --> print(sheet.nrows)


def read_dir(addr):
    
    rows=[]
    filenames = list(next(walk(addr), (None, None, []))[2]) # [] if no file
    filenames.sort()
    
    for row in filenames:
        number=int(filenames.index(row)+1)
        #name=sheet.cell_value(row, 0)
        #link=sheet.cell_value(row, 1)
        file_extension=str(row)[-3::]
        if(file_extension=="png" or file_extension=="jpg"):
            link_name=row
            rows.append([number,"name","link","answer",link_name,1])
        #answer=sheet.cell_value(row, 2)
        # if(answer!="*"):
        #     rows.append([number,name,link,answer,link_name,1])
    return rows


