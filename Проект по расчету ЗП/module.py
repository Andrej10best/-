from tkinter import *


# Заготовленные функции
def click():
    common = float(money.get()) * 1.12 * 1.35 * float(var.get()) * 0.87
    result = (common / 20) * int(day.get())
    rounded_result = round(result, 1)
    lbl8.configure(text=rounded_result, fg='green')
    lbl8.place(x=45, y=270)


def clear_text():
    money.delete(0, 'end')
    day.delete(0, 'end')
    lbl8.configure(text='')


# Создание окна
root = Tk()
root.title('Расчет зар. платы.')
root.geometry('450x350')
root.resizable(False, False)

# Создание рамок
lbl_frame = LabelFrame(root, text='Входные данные', font=('Times New Roman', 12))
lbl_frame.place(x=20, y=15, width=200, height=150)

lbl_frame2 = LabelFrame(root, text='Надбавки и вычеты', font=('Times New Roman', 12))
lbl_frame2.place(x=230, y=15, width=200, height=150)

lbl_frame3 = LabelFrame(root, text='Расчетная часть', font=('Times New Roman', 12))
lbl_frame3.place(x=20, y=170, width=200, height=150)

# Создание текстовых полей
lbl = Label(root, text='Оклад:', font=('Times New Roman', 11))
lbl.place(x=45, y=40)

lbl2 = Label(root, text='Кол-во отраб. дней:', font=('Times New Roman', 11))
lbl2.place(x=45, y=100)

lbl3 = Label(root, text='+12%', font=('Times New Roman', 11))
lbl3.place(x=250, y=40)

lbl4 = Label(root, text='+35%', font=('Times New Roman', 11))
lbl4.place(x=250, y=60)

lbl5 = Label(root, text='Премия:', font=('Times New Roman', 11))
lbl5.place(x=250, y=80)

lbl6 = Label(root, text='Вычет: -13%', font=('Times New Roman', 11))
lbl6.place(x=320, y=120)

lbl7 = Label(root, text='Итог:', font=('Times New Roman', 11))
lbl7.place(x=45, y=240)

# Создание радиокнопок с вариантами премирования
var = DoubleVar()
var.set(1.45)

rb1 = Radiobutton(root, text='35%', font=('Times New Roman', 11), variable=var, value=1.35)
rb2 = Radiobutton(root, text='45%', font=('Times New Roman', 11), variable=var, value=1.45)

rb1.place(x=250, y=100)
rb2.place(x=250, y=120)

# Создание полей для ввода данных
money = Entry(root, width=14, font=('Times New Roman', 11))
money.place(x=45, y=65)

day = Entry(root, width=14, font=('Times New Roman', 11))
day.place(x=45, y=125)

# Создание кнопок
btn = Button(root, text='Расчитать', width=8, height=1, command=click)
btn.place(x=45, y=200)

btn2 = Button(root, text='Очистить', width=8, height=1, command=clear_text)
btn2.place(x=250, y=200)

# Текстовое поле для вывода результата
lbl8 = Label(root, text='', font=('Times New Roman', 14))

root.bind('<Return>', click)

root.mainloop()
