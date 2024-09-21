import random as rnd
import sys
import os
import funktionen
import datum

class Lotto:
        __menutext = """
*************************
***  Lotto-Generator  ***
*************************

* Zahlen (A)uslesen
* Zahlen (E)rstellen
* (V)erzeichnis wechseln
* (B)eenden
        """
        
        def __init__(self, filename):
                assert isinstance(filename, object)
                self.path = filename
                if sys.platform == "win32":
                        self.user = os.environ['USERNAME']
                else:
                        self.user = os.environ['USER']

        def lotto_read(self):
                funktionen.clear()
                try:         
                        file = open(self.path, "r")
                        lotto = file.readlines()
                        file.close()
                        for i in range(len(lotto)):
                            lotto[i] = lotto[i].rstrip(lotto[i][-1])

                except:
                        lotto = [f"Datei {self.path} ist nicht im aktuellen Verzeichnis!"]
                return lotto

        def lotto_create(self, row):
                lotto=[]
                lotto.extend(range(1,50))
                date = funktionen.date()
                time_now = funktionen.time_now()
                file = open(self.path, 'w')
                tip = [f"{date}  {time_now}"]
                file.write(date + '  ' + time_now)
                for i in range(row):
                    row=f"{i+1:2d}. "
                    ergebnis = rnd.sample(lotto, 6)
                    ergebnis.sort()
                    file.write("\n{:2d}. ".format(i+1))
                    for j in ergebnis:
                        row = row + f"{j:2d} "
                        file.write("{:2d} ".format(j))
                    tip.append(row)
                file.write("\n")
                file.close()
                return tip

        def changedir(self):
                funktionen.clear()
                files = os.listdir()
                files.sort()
                path = ""
                for entry in files:
                        path += "{entry:<30}{bytes:>10} Byte\n".format(
                                entry=entry,
                                bytes=os.path.getsize(entry))
                print(path)
                newPath = input("Bitte Arbeitsverzeichnis eingeben: ")
                try:
                        os.chdir(newPath)
                except:
                        print("Verzeichnis '{}' ist nicht vorhanden!".format(newPath))
                menu = input("Zum Beenden Return drücken:")

        def run(self):
                choice = "-"
                while choice not in "Bb":
                        funktionen.clear()
                        self.date = datum.datetime()
                        print("{} {}".format(self.date[0], self.user))
                        print("\naktuelles Verzeichnis: ", os.getcwd())
                        print(self.__menutext)
                        choice = input("Ihre Wahl: ")
                        if choice in "Aa": self.lotto_read()
                        elif choice in "Ee": self.lotto_create()
                        elif choice in "Vv": self.changedir()
                print("Danke für die Benutzung des Lotto-Generators!")
                menu = input("Zum Beenden Return drücken")



