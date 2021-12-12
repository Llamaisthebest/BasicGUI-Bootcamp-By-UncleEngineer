# BasicGUI By Uncle Engineer

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import csv
############################
def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543)
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return stamp

def writetext(quantity,total):
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'Date&Time: {} Food: {} kg. Pay {:,.2f} Bath'.format(stamp,quantity,total))

def writecsv(data):

	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data)
	print('Success')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		data = list(fr)
	return data

def sumdata():
	result = readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return(sumquan,sumtotal)
############################
GUI = Tk()
GUI.geometry('1000x700')
GUI.title('Program For Counting Food v.0.0.1')

file = PhotoImage(file='FoodCalculater.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='Program Counting Quantity Of Food(Must Use Full Screen)',font=('Angsana New',30,'bold'),fg='green')
L1.pack()

L2 = Label(GUI,text='Please Put In How Much Quantity Of Food(kg.)',font=('Angsana New',20))
L2.pack()

v_quantity = StringVar()

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()

def Calculate(event=None):
	quantity = v_quantity.get()
	price = 100
	print('Count:', float(quantity) * price)
	cal = float(quantity) * price

	data = [timestamp(thai=False), quantity, cal]
	writecsv(data)

	sm = sumdata()
	title ='Pay'
	text = 'Food Count {} kg 1 kg = 100 bath Pay All: {:,.2f} Bath'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('')

B1 = ttk.Button(GUI,text='Calculate',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>', Calculate)

def SummaryData(event):
	sm = sumdata()
	title ='AllTogether'
	text = 'Counts: {} kg. Selling: {:,.2f} Bath'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

GUI.bind('<F1>',SummaryData)
GUI.bind('<F2>',SummaryData)

E1.focus()
GUI.mainloop()