#! /usr/bin/python3
from tkinter import *
from tkinter import messagebox
from lotto import Lotto


class LottoGUI:
    def __init__(self, filename):
        self.l = Lotto(file)
        self.lotto = Lotto.lotto_read(self.l)
        self.Labeltxt = []
        self.LottoLabel = []
        self.main = Tk()
        self.main.title("Lotto Generator")
        self.main.geometry("800x600")
        self.main.resizable(False, False)
        self.row_value = StringVar()
        for i in range(14):
            if i < len(self.lotto):
                self.Labeltxt.append(StringVar(value=self.lotto[i]))
                self.LottoLabel.append(Label(self.main, textvariable=self.Labeltxt[i], anchor="w", justify="left", font=("Mono", 15)))
                self.LottoLabel[i].pack(fill="x")
            else:
                self.Labeltxt.append(StringVar(value=""))
                self.LottoLabel.append(Label(self.main, textvariable=self.Labeltxt[i], anchor="w", justify="left", font=("Mono", 15)))
                self.LottoLabel[i].pack(fill="x")
                self.__addMenu()
                self.__addFileMenu()

        self.new_tip = Frame(self.main, relief="ridge")
        self.frame_title = Label(self.new_tip, text="Neuen Tip erzeugen", font=("Mono", 12))
        self.question = Frame(self.new_tip)
        self.questionLabel = Label(self.question, text="Wieviele Zeilen sind erwünscht?", font=("Mono", 15))
        self.questionEntry = Entry(self.question, textvariable=self.row_value, width=2, font=("Mono", 15))
        self.questionButton = Button(self.question, text="Ok", font=("Mono", 15), command=self.overtaking)
        self.questionLabel.pack(side="left")
        self.questionEntry.pack(side="left")
        self.questionButton.pack(side="right")
        self.frame_title.pack()
        self.question.pack()
        self.new_tip.pack(side="bottom")        
        self.main.mainloop()
        
    def __addMenu(self):
        self.menu = Menu(self.main)
        self.main.configure(menu=self.menu)

    def __addFileMenu(self):
        self.filemenu = Menu(master=self.menu)
        self.file = StringVar()
        self.menu.add_cascade(label="Datei", menu=self.filemenu)
        self.filemenu.add_command(label='Ende', command=self.quit)

    def overtaking(self):
        row = int(self.row_value.get())
        if row < 1 or row > 12:
            messagebox.showerror("Falscher Zahlenbereich", "Die erlaubte Anzahl Zeilen ist von einer bis zu 12 Zeilen definiert!")
            return
        tip = Lotto.lotto_create(self.l, row)
        for i in range(14):
            if i < len(tip):
                self.Labeltxt[i].set(tip[i])
            else:
                self.Labeltxt[i].set("")

    #def lotto_create(self):
        #self.create = Tk()
        #self.create.title("Neuen Tip erzeugen")
        #self.questionlabel = Label(self.create, text="Wieviele Zeilen sind erwünscht?")
        #self.questionlabel.pack()
        #self.questionEntry = Entry(self.create, textvariable=self.row_value)
        #self.questionEntry.pack()
        #self.questionButton = Button(self.create, text="Ok", command=self.overtaking)
        #self.questionButton.pack()

    def quit(self):
        if messagebox.askyesno('Beenden',  'Wollen Sie wirklich das Programm beenden?'):
            self.main.destroy()
                
          
file = ("lotto.txt")
l = LottoGUI(file)
