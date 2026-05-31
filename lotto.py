import random as rnd
import sys
import os
import funktionen

class Lotto:    
        def __init__(self, filename):
                assert isinstance(filename, object)
                self.path = filename
                if sys.platform == "win32":
                        self.user = os.environ['USERNAME']
                else:
                        self.user = os.environ['USER']

        def lotto_read(self):
                try:         
                        file = open(self.path, "r")
                        lotto = file.readlines()
                        file.close()
                        for i in range(len(lotto)):
                            lotto[i] = lotto[i].rstrip(lotto[i][-1])
                        date, *lotto_data = lotto
                        for item, lottoRow in enumerate(lotto_data):
                                lottoRow = list(lottoRow.split(sep=" "))
                                lottoRow = list(filter(None,map(str.strip, lottoRow)))
                                lotto_data[item] = lottoRow
                        return date, lotto_data
      
                except:
                        lotto = f"Datei {self.path} ist nicht im aktuellen Verzeichnis!"
                        return lotto, list()

        def lotto_create(self, row):
                lotto=[]
                lotto.extend(range(1,50))
                date = funktionen.date()
                time_now = funktionen.time_now()
                file = open(self.path, 'w')
                date = f"{date}  {time_now}"
                tip = []
                file.write(date)
                for i in range(row):
                    row=[f"{i+1:2d}."]
                    ergebnis = rnd.sample(lotto, 6)
                    ergebnis.sort()
                    file.write("\n{:2d}. ".format(i+1))
                    for j in ergebnis:
                        row.append(str(j))
                        file.write("{:2d} ".format(j))
                    tip.append(row)
                file.write("\n")
                file.close()
                return date, tip

        def changedir(self, newPath):
                try:
                        os.chdir(newPath)
                        return 0, newPath
                except:
                        return 1, f"in Verzeichnis '{newPath}' kann nicht gewechselt werden!"




