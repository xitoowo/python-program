import tkinter
from tkinter import messagebox


def throw_info():
    messagebox.showinfo('Сохранение', 'Данные были сохранены!')


window = tkinter.Tk()
window.title('Введите адрес')
frame = tkinter.Frame()
frame.pack()
lbl_first_name = tkinter.Label(master=frame, text="Имя: ")
ent_first_name = tkinter.Entry(master=frame, width=50)
lbl_first_name.grid(row=0, column=0, sticky=tkinter.E)
ent_first_name.grid(row=0, column=1)
lbl_second_name = tkinter.Label(master=frame, text="Фамилия: ")
ent_second_name = tkinter.Entry(master=frame, width=50)
lbl_second_name.grid(row=1, column=0, sticky=tkinter.E)
ent_second_name.grid(row=1, column=1)
lbl_country = tkinter.Label(master=frame, text="Страна: ")
ent_country = tkinter.Entry(master=frame, width=50)
lbl_country.grid(row=2, column=0, sticky=tkinter.E)
ent_country.grid(row=2, column=1)
lbl_city = tkinter.Label(master=frame, text="Город: ")
ent_city = tkinter.Entry(master=frame, width=50)
lbl_city.grid(row=3, column=0, sticky=tkinter.E)
ent_city.grid(row=3, column=1)
lbl_street = tkinter.Label(master=frame, text="Улица: ")
ent_street = tkinter.Entry(master=frame, width=50)
lbl_street.grid(row=4, column=0, sticky=tkinter.E)
ent_street.grid(row=4, column=1)
lbl_index = tkinter.Label(master=frame, text="Индекс: ")
ent_index = tkinter.Entry(master=frame, width=50)
lbl_index.grid(row=5, column=0, sticky=tkinter.E)
ent_index.grid(row=5, column=1)
btn_submit = tkinter.Button(master=frame, text='Сохранить...',
                            command=throw_info)
btn_submit.grid(row=6, column=1)
window.mainloop()
