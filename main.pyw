#! /usr/bin/python3
import subprocess
import platform
import os
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from lotto import Lotto
from center.center import center_window
from aboutTK import About
script_dir = os.path.dirname(os.path.abspath(__file__))

class LottoGUI:
    def __init__(self, filename):
        self.l = Lotto(file)
        self.dir = os.getcwd()
        self.Labeltxt = []
        self.LottoLabel = []
        self.main = Tk()
        self.icon = os.path.join(script_dir, 'lotto.png')
        self.image = PhotoImage(file=self.icon)
        self.main.iconphoto(False, self.image)
        self.main.title(f"Lotto Generator: {self.dir}")
        self.geometry = center_window(800, 600, self.main)
        self.main.geometry(self.geometry)
        self.main.resizable(False, False)
        self.row_value = StringVar()
        index = 0
        for _row in range(14):
            if index == 0:
                self.Labeltxt.append(StringVar(value=""))
                self.LottoLabel.append(Label(self.main, textvariable=self.Labeltxt[index], anchor="w", justify="left", font=("Arial", 15)))
                self.LottoLabel[index].grid(row=0, column=0, columnspan=7, padx=10, pady=10)
                index += 1
            else:
                for _column in range(7):
                    self.Labeltxt.append(StringVar(value=""))
                    self.LottoLabel.append(Label(self.main, textvariable=self.Labeltxt[index], anchor="w", justify="left", font=("Arial", 15)))
                    self.LottoLabel[index].grid(row=_row, column=_column, padx=10, pady=5)
                    index += 1
        self.lotto = Lotto.lotto_read(self.l)
        self.lotto_output(self.lotto)
        self.__addMenu()
        self.__addFileMenu()
        self.__addAboutMenue()
        self.main.wm_protocol("WM_DELETE_WINDOW", self.quit)
        self.main.mainloop()
        
    def __addMenu(self):
        self.menu = Menu(self.main)
        self.main.configure(menu=self.menu)

    def __addFileMenu(self):
        self.filemenu = Menu(master=self.menu)
        self.file = StringVar()
        self.menu.add_cascade(label="Datei", menu=self.filemenu)
        self.filemenu.add_command(label="Verzeichnis wechseln", command=self.changedir, accelerator="Strg+V")
        self.filemenu.add_command(label='Neuen Tip erstellen', command=self.lotto_create, accelerator="Strg+E")
        self.filemenu.add_command(label="Datei anzeigen", command=self.show_txt, accelerator="Strg+T")
        self.filemenu.add_command(label='Ende', command=self.quit, accelerator="Strg+B")

        self.main.bind("<Control-v>", lambda event: self.changedir())
        self.main.bind("<Control-e>", lambda event: self.lotto_create())
        self.main.bind("<Control-t>", self.show_txt)
        self.main.bind("<Control-b>", lambda event: self.quit())

    def __addAboutMenue(self):
        self.aboutmenu = Menu(master=self.menu)
        self.menu.add_cascade(label="Über", menu=self.aboutmenu)
        self.aboutmenu.add_command(label="Version", command=self.about)

    def lotto_output(self, tip):
        date, lotto = tip
        self.main.title(f"Lotto Generator: {self.dir}")
        if self.Labeltxt[0] != "":
            for Labeltxt in self.Labeltxt:
                Labeltxt.set("")
        self.Labeltxt[0].set(date)
        index = 0
        for _row, lottoRow in enumerate(lotto):
            for _col, lottoCol in enumerate(lottoRow):
                index += 1
                self.Labeltxt[index].set(lottoCol)
            print()
    def changedir(self):
        self.newPath = filedialog.askdirectory()
        returnValue, newPath = Lotto.changedir(self.l, self.newPath)
        if returnValue == 0:
            self.dir = os.getcwd()
            self.lotto = Lotto.lotto_read(self.l)
            self.lotto_output(self.lotto)

    def lotto_create(self):
        row_str = simpledialog.askstring("Neuen Tip erzeugen", "Wieviele Zeilen sind erwünscht?")
        print(row_str)
        if row_str is not None:
            if row_str.isdigit():
                row = int(row_str)
                if row < 1 or row > 12:
                    messagebox.showerror("Falscher Zahlenbereich", "Die erlaubte Anzahl Zeilen ist von einer bis zu 12 Zeilen definiert!")
                    return
                else:
                    tip = Lotto.lotto_create(self.l, row)
                    self.lotto_output(tip)
            else:
                messagebox.showerror("Eingabe nicht erwünscht", "Bitte nur Zahlen eingeben!")
                return 

    def show_txt(self, event=None):
        # Nutzt self.dir für den Pfad auf deinem USB-Stick 
        file_path = os.path.join(self.dir, "lotto.txt")

        if os.path.exists(file_path):
            system = platform.system()
            if system == 'Windows':
                os.startfile(file_path)
            else:
                opener = 'open' if system == 'Darwin' else 'xdg-open'
                subprocess.call([opener, file_path])
        else:
            messagebox.showwarning("Datei fehlt", f"Keine lotto.txt in {self.dir} gefunden.")     

    def quit(self):
        if messagebox.askyesno('Beenden',  'Wollen Sie wirklich das Programm beenden?'):
            self.main.quit()
            self.main.destroy()

    def about(self):
        About(self.main, "Lotto - 6 aus 49", "Lotto-Generator", 1.1)
          
file = ("lotto.txt")
l = LottoGUI(file)
