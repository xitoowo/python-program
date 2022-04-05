from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mbox


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Всплывающие окна с уведомлениями")
        self.pack()

        error = Button(self, text="Ошибка", command=self.onError)
        error.grid(padx=5, pady=5)
        warning = Button(self, text="Предупреждение", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Вопрос", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Информация", command=self.onInfo)
        inform.grid(row=1, column=1)

    def onError(self):
        mbox.showerror("Ошибка", "Не могу открыть файл")

    def onWarn(self):
        mbox.showwarning("Предупреждение", "Вызов устаревшей функции")

    def onQuest(self):
        mbox.askquestion("Вопрос", "Вы уверены, что хотите выйти?")

    def onInfo(self):
        mbox.showinfo("Информация", "Скачивание завершено")


def main():
    root = Tk()
    ex = Example()
    root.geometry("300x150+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()