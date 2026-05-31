import random as rnd
import os
from datetime import datetime

class Lotto:
    def __init__(self, filename):
        self.path = filename

    def lotto_read(self):
        try:
            if not os.path.exists(self.path):
                return [f"Datei {self.path} ist nicht im aktuellen Verzeichnis!"]
            
            with open(self.path, "r", encoding="utf-8") as file:
                lines = file.readlines()
            
            # Bereinige die Zeilen von Newlines und gib sie zurück
            return [line.strip() for line in lines if line.strip()]
        except Exception:
            return [f"Fehler beim Lesen von {self.path}"]

    def lotto_create(self, row):
        lotto_zahlen = list(range(1, 50))
        now = datetime.now()
        date_str = now.strftime("%d.%m.%Y  %H:%M:%S")
        
        output = [date_str]
        
        # Generiere die gewünschte Anzahl an Tippzeilen
        for i in range(row):
            tipp = sorted(rnd.sample(lotto_zahlen, 6))
            tipp_str = " ".join(f"{z:2d}" for z in tipp)
            output.append(f"{i+1:2d}. {tipp_str}")
            
        # Schreibe alles in die Datei
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                for line in output:
                    file.write(line + "\n")
        except Exception:
            pass
            
        return output

    def changedir(self, new_path):
        try:
            if new_path:
                os.chdir(new_path)
                return 0, new_path
            return 1, os.getcwd()
        except Exception:
            return 1, os.getcwd()
