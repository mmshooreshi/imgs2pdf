from pickle import NONE
from fpdf import FPDF
import os
import numpy 
from alive_progress import alive_bar
from modules import *


rows = []

def save_loc(pdf):
    global x_var,y_var
    x_var=pdf.get_x()
    y_var=pdf.get_y()

def set_loc(pdf):
    pdf.set_x(x_var)
    pdf.set_y(y_var)

def count_added(l):
    sumv=0
    for val in list(l[:,5]):
        sumv+=int(val)
    return sumv

def mainc(pdf):
    temp=0
    global q_num,added_list
    for question in remaining_rows:
        if(question[3]!="*" and q_num<=100 and question[5]!=0):
            
            imglink=question[2]
            img_local_link=basepath+"/imgs/"+question[4]
            imglink=img_local_link
            
            img_local_link = img_local_link[:img_local_link.rfind("."):1]+'.jpg'
            imglink=img_local_link

            box=imgdimension(imglink)
            box_height=box[1]
            box_width=box[0]
            box_widthpx=box[3]
            
            #edit this if you want:
            global y_var
            save_loc(pdf)


            hh=int(box_height)
            if(hh>260):
                #print("in")
                ww=(250/hh)*box_width
                hh=250
                box_widthpx=ww
                xx=185-ww
            elif(int(box_widthpx)>500):
                ww=180
                hh=(ww/185)*box_height
                xx=5
            else:
                ww=160
                hh=(ww/185)*box_height
                xx=25


            print("\n")
            print(question)
            print("y_var: ",y_var)
            print("height: ",hh)
            print("xx: ",xx)
            print("\n")
            l=numpy.array(remaining_rows)
            if(int(hh)+int(y_var) >270):
                if(int(y_var)>270):
                    pdf.add_page()
                else:
                    temp=count_added(l)
                    continue      
            q_num+=1
            number=".("+str(q_num)+")"

            save_loc(pdf)
            #pdf.dashed_line(x_var,y_var+5,x_var+160,y_var+5, dash_length = 1, space_length = 1)
            #print(y_var)
            #print(box_height)
            
            
            save_loc(pdf)

            remaining_rows[remaining_rows.index(question)][5]=0

            added_list.append([q_num,question[1],question[3]])
            
            #print(added_list)
            l=numpy.array(remaining_rows)

            #print("rem: " ,[l[:,[0,5]]],end="\n")
            #print(number+" started to load")
            #print(question)
            
            pdf.cell(w=196,h=10,txt=number,ln=1,border='T',align='R',fill=False)
            pdf.cell(w=196,h=hh-2.5,ln=1,border='B',align='R',fill=False)
            y_var=y_var+5
            set_loc(pdf)

            pdf.image(imglink,w=ww,x=pdf.get_x()+xx)
            

            #print(number+"loaded")
            #pdf.line(x_var,y_var+5,x_var+185,y_var+5)
            save_loc(pdf)
            y_var=y_var+2.5
            set_loc(pdf)
    
    l=numpy.array(remaining_rows)
    if(temp==count_added(l) and count_added(l)>0):
        pdf.add_page()
        pdf.pages
    if(count_added(l)==0 or pdf.page_no()>20):
        return
    return 



#Defining the basepath
basepath=os.path.dirname(__file__)

# ~1 Opening XLS file
#remaining_rows= read_excel(basepath+"I-O/input_file")

# ~2 Or directly we open images from 'basepath/imgs/...'
remaining_rows=read_dir(basepath+"/imgs")

print(remaining_rows)

numpy.random.shuffle(remaining_rows)
#print(remaining_rows)

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
pdf.accept_page_break()
pdf.add_page()
pdf.set_font('Arial', 'B', 12)



#print(remaining_rows)
q_num=0
added_list=[]
l=numpy.array(remaining_rows)

with alive_bar(20,enrich_print=True) as bar:
    while(count_added(l)>0 and pdf.page_no()<=1000):
        pg=pdf.page_no()
        mainc(pdf)
        l=numpy.array(remaining_rows)
        for co in range(pdf.page_no()-pg):
            bar()
print("FINISHED")
pdf.output(basepath+'/I-O/output_sorted.pdf', 'F')
        
list_output(added_list)




