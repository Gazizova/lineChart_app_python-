from tkinter import *
import math

root = Tk()
root.title("Построение графика функций y = sin(x)")
root.geometry('1020x620')

canvas = Canvas(root, width=1200, height=620, bg='#002')

# линии сетки по вертикали
for y in range(21):
    k = 50*y
    canvas.create_line(10+k, 610, 10+k, 10, width=1, fill='#191936')

# линии сетки по вертикали
for x in range(13):
    k = 50*x
    canvas.create_line(10, 10+k, 1010, 10+k, width=1, fill='#191936')

# линии координат x & y
canvas.create_line(10, 10, 10, 610, width=1, arrow=FIRST, fill='white') # Y
canvas.create_line(0, 310, 1010, 310, width=1, arrow=LAST, fill='white') # X

w = 0.0209
phi = 10
A = 200
dy = 310

xy = []
for x in range(1000):
    y = math.sin(x * w)
    xy.append(x + phi)
    xy.append(y * A + dy)
sin_line = canvas.create_line(xy, fill='blue')
canvas.pack()


def button_clicked():
    print ("Клик!")
root1=Tk()
# кнопка по умолчанию
button1 = Button()
button1.pack()
# кнопка с указанием родительского виджета и несколькими аргументами
button2 = Button(root1, bg="red", text=u"Кликни меня!", command=button_clicked)
button2.pack()

root2 = Tk()
text = Text(root2, height=20, width=20, font='Arial 10', wrap=WORD)
text.pack()

root.mainloop()

root=Tk()
var1=IntVar()
var2=IntVar()
check1=Checkbutton(root,text=u'1 пункт',variable=var1,onvalue=1,offvalue=0)
check2=Checkbutton(root,text=u'2 пункт',variable=var2,onvalue=1,offvalue=0)
check1.pack()
check2.pack()
root.mainloop()