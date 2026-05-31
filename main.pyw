#! /usr/bin/python3
import os
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from lotto import Lotto


class LottoGUI:
     def __init__(self, filename):
          self.l = Lotto(file)
          self.dir = os.getcwd()
          self.lotto = Lotto.lotto_read(self.l)
          self.Labeltxt = []
          self.LottoLabel = []
          self.main = Tk()
          self.main.title(f"Lotto Generator: {self.dir}")
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
          self.filemenu.add_command(label="Verzeichnis wechseln", command=self.changedir)
          self.filemenu.add_command(label='Neuen Tip erstellen', command=self.lotto_create)
          self.filemenu.add_command(label='Ende', command=self.quit)

     def __addAboutMenue(self):
          self.aboutmenu = Menu(master=self.menu)
          self.menu.add_cascade(label="Über", menu=self.aboutmenu)
          self.aboutmenu.add_command(label="Version", command=self.about)

     def lotto_output(self, tip):
          self.main.title(f"Lotto Generator: {self.dir}")
          for i in range(14):
               if i < len(tip):
                    self.Labeltxt[i].set(tip[i])
               else:
                    self.Labeltxt[i].set("")

     def changedir(self):
          self.newPath = filedialog.askdirectory()
          returnValue, newPath = Lotto.changedir(self.l, self.newPath)
          if returnValue == 0:
               self.dir = os.getcwd()
               self.lotto = Lotto.lotto_read(self.l)
               self.lotto_output(self.lotto)

     def lotto_create(self):
          row_str = simpledialog.askstring("Neuen Tip erzeugen", "Wieviele Zeilen sind erwünscht?")
          if row_str is not None:
               if row_str.isdigit():
                    row = int(row_str)
                    if 1 <= row <= 12:
                         tip = Lotto.lotto_create(self.l, row)
                         self.lotto_output(tip)
                    else:
                         messagebox.showerror("Falscher Zahlenbereich", "Die erlaubte Anzahl Zeilen ist von einer bis zu 12 Zeilen definiert!")
                         return
               else:
                    messagebox.showerror("Eingabe nicht erwünscht", "Bitte nur Zahlen eingeben!")
                    return


     def quit(self):
          if messagebox.askyesno('Beenden',  'Wollen Sie wirklich das Programm beenden?'):
               self.main.quit()
               self.main.destroy()

     def about(self):
          version_window = Toplevel(self.main)
          version_window.title("Über")
          version_window.geometry("250x100")
          version_label = Label(version_window, text="Lotto-Generator 1.0")
          version_label.pack(padx=20, pady=20)
          version_button = Button(version_window, text="ok", command=version_window.destroy)
          version_button.pack(side="bottom", padx=20, pady=10)

file = ("lotto.txt")
l = LottoGUI(file)
