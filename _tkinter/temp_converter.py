import tkinter


class Converter(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title = 'Конвертер температур'
        self.geometry("200x50")
        self.resizable(width=False, height=False)

        self.frame = tkinter.Frame(self)
        self.frame.grid(row=0, column=0, padx=10)
        self.ent_temp = tkinter.Entry(self.frame, width=10)
        self.lbl_temp = tkinter.Label(self.frame, text="\N{DEGREE FAHRENHEIT}")
        self.ent_temp.grid(row=0, column=0, sticky='E')
        self.lbl_temp.grid(row=0, column=1, sticky='W')

        self.btn_convert = tkinter.Button(self, text="\N{RIGHTWARDS BLACK ARROW}", command=self.convert)
        self.btn_convert.grid(row=0, column=1, pady=10)
        self.lbl_result = tkinter.Label(self, text="\N{DEGREE CELSIUS}")
        self.lbl_result.grid(row=0, column=2, padx=10)

    def convert(self):
        fahrenheit = self.ent_temp.get()
        if not fahrenheit:
            self.ent_temp.insert(0, 'Введите значение')
            return
        celsius = ((5 / 9) * float(fahrenheit)) - 32
        self.lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


if __name__ == '__main__':
    app = Converter()
    app.mainloop()
