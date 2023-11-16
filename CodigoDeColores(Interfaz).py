from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.title('\tCódigo De Resistencias - Cuatro Franjas')
root.configure(background='#DDD') 
root.geometry('700x350')

def comercial(r):
	global l5
	l5.destroy()
	lista = (0.1, 0.12, 0.13, 0.2, 0.24, 0.27, 0.33, 0.39, 0.43, 0.51, 0.68, 0.75, 0.82, 0.91, 1, 1.2, 1.5, 1.8, 2.2, 2.7,
		3.3, 3.9, 4.7, 5.1, 5.6, 6.8, 8.2, 10, 12, 15, 18, 22, 27, 33, 39, 47, 51, 56, 68, 82, 100, 120, 150, 180, 220,
		270, 330, 390, 470, 510, 560, 680, 820, 1000, 1200, 1500, 1800, 2200, 2700, 3300, 3900, 4700, 5100, 5600, 6800,
		8200, 10000, 12000, 15000, 18000, 22000, 27000, 33000, 39000, 47000, 51000, 56000, 68000, 82000, 100000, 120000,
		150000, 180000, 220000, 270000, 330000, 390000, 470000, 51000, 560000, 680000, 820000, 1E6, 1.2E6, 1.5E6, 1.8E6, 
		2.2E6, 2,7E6, 3.3E6, 3.9E6, 4.7E6, 5.1E6, 5.6E6, 6.8E6, 8.2E6, 10E6
	)
	if r in lista:
		l5 = Label(root,text="La resistencia es comercial.",fg='#039C06',font=('Helvetica', 10, 'bold'))
		l5.place(x=5,y=275)
	else:
		l5 = Label(root,text="La resistencia NO es comercial.",fg='#F00',font=('Helvetica', 10, 'bold'))
		l5.place(x=5,y=275)


def codcol(x):
	global l4
	l4.destroy()
	codigo = {
	    0:"negro",
	    1:"cafe",
	    2:"rojo",
	    3:"naranja",
	    4:"amarillo",
	    5:"verde",
	    6:"azul",
	    7:"violeta",
	    8:"gris",
	    9:"blanco",
	    0.1:"dorado",
	    0.01:"plata"
	}

	codigoc = {
	    0:"#000",
	    1:"#6E5808",
	    2:"#F00",
	    3:"#FFB300",
	    4:"#FFF700",
	    5:"#0F0",
	    6:"#00F",
	    7:"#E600FF",
	    8:"#514F52",
	    9:"#FFF",
	    0.1:"#FCE983",
	    0.01:"#D1D1D1"
	}

	x = round(x,2)

	if x >= 10:

		y = len(str(x)) - 2
		f1 = x // (10**(y-1))
		f2 = x // (10**(y-2)) - (f1*10)
		f3 = y - 2

	elif x >= 1 and x < 10:

		y = x * 10
		f1 = y // 10
		f2 = y - (f1*10)
		f3 = 0.1

	elif x == 0 :
		f1=0
		f2=0
		f3=0

	elif x < 1 and x>0:
		y = x
		y=y*100
		f1 = y // (10)
		f2 = y - (f1*10)
		f3 = 0.01

	l4 = Label(root,text=f"{codigo[f1].upper()}, {codigo[f2].upper()}, {codigo[f3].upper()}, DORADO.",fg='#000',bg='#DDD',font=('Helvetica', 10, 'bold'))
	l4.place(x=145,y=210)
	canvasr = Canvas(root,width=300,height=100)
	canvasr.place(x=100,y=95)
	canvasr.create_rectangle(3,10,300,100,fill="#D7F1F7")#izq,sup,der,inf
	canvasr.create_rectangle(40,10,70,100,fill=codigoc[f1])#izq,sup,der,inf
	canvasr.create_rectangle(100,10,130,100,fill=codigoc[f2])#izq,sup,der,inf
	canvasr.create_rectangle(190,10,160,100,fill=codigoc[f3])#izq,sup,der,inf
	canvasr.create_rectangle(220,10,250,100,fill=codigoc[0.1])#izq,sup,der,inf

def calcul(*args):
	global l2,l3,l4
	l2.destroy()
	l3.destroy()
	try:
		patron = r'[+-]?\d*\.?\d+'
		num = str(inp.get())	
		if 'K' in num or 'k' in num:	
			num = re.findall(patron, num)
			num = float(num[0])*1E3
		elif 'M' in num:
			num = re.findall(patron, num)
			num = float(num[0])*1E6
		elif 'G' in num:
			num = re.findall(patron, num)	
			num = float(num[0])*1E9
		elif 'm' in num:	
			num = re.findall(patron, num)	
			num = float(num[0])*1E-3
		else:
			num = float(inp.get())
		
		if num > 9.9E+10:
			messagebox.showwarning(message="¡Valor Muy Grande!\nPor favor ingrese un número menor o igual a 99 G Ω.",title="Advertencia")
		elif num < 0.1 and num != 0:
			messagebox.showwarning(message="¡Valor Muy Pequeño!\nPor favor ingrese un número mayor o igual a 0.1 Ω.",title="Advertencia")
		else:
			l2 = Label(root,text=notacion(round(num,2)),fg='#000',font=('Helvetica', 10, 'bold'))
			l2.place(x=225,y=75)
			l3 = Label(root,text=f"Considere la última franja como dorado (± 5%). Valor oscila entre {round(num*0.95,2)} Ω y {round(num*1.05,2)} Ω",fg='#000',font=('Helvetica', 10, 'bold'))
			l3.place(x=5,y=245)
			codcol(num)
	except ValueError:
		messagebox.showerror(message="¡Error De Entrada!\nPor favor ingrese un número válido.",title="Error")
		pass

def notacion(res):
	comercial(res)
	if res >= 1000:
		if res >= 1000 and res < 1000000:
			res = res/1000	
			if (res % 10) == 0 or res == 1:
				enot = str("  " + str(int(res)))
				enot += " k Ω "
			else:	
				enot = str("  " + str(res))
				enot += " k Ω "
		elif res >= 100000 and res < 1000000000:
			res = res/1000000
			if (res % 10) == 0 or res == 1:
				enot = str("  " + str(int(res)))
				enot += " M Ω "
			else:
				enot = str("  " + str(res))
				enot += " M Ω "
		elif res >= 1E9 and res < 1E12:
			res = res/1E9
			if (res % 10) == 0 or res == 1:
				enot = str("  " + str(int(res)))
				enot += " G Ω "
			else:
				enot = str("  " + str(res))
				enot += " G Ω "
	else:
		if (res % 10) == 0 or res == 1:
			enot = "   " + str(int(res)) + " Ω   "
		else:
			enot = "   " + str(res) + " Ω   "
	
	return enot

l2 = Label(root)
l3 = Label(root)
l4 = Label(root)
l5 = Label(root)
l = Label(root,text='Escribe el valor en Ohms:\n',fg='#000',bg='#DDD',font=('Helvetica', 10, 'bold'))
l.place(x=25,y=25)
inp = StringVar()
inpt = Entry(textvar=inp)
inpt.place(x=225,y=25)
btn = Button(root,text='Enviar',fg='#000',bg='#439C0C',font=('Helvetica', 10, 'bold'),command=calcul)
btn.place(x=360,y=22)
l = Label(root,text="Ernesto Romero Rios ®",fg='#000',bg='#DDD',font=('Helvetica', 10, 'bold'))
l.place(x=5,y=320)
inpt.focus()
root.bind("<Return>",calcul)
root.mainloop()