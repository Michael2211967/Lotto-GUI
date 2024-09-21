 # Datum.py
 # Datum gibt das aktuelle Datum und die Zeit
 # in deutschem Format aus

import time

def datetime():
    month = ["Januar", "Februar", "März", "April", "Mai", "Juni",\
          "Juli", "August", "September", "Oktober", "November", "Dezember"]
    wtage = ["Montag", "Dienstag", "Mittwoch",\
          "Donnerstag", "Freitag", "Samstag", "Sonntag"]


    lt = time.localtime()                                #   Variablenstruktur für
                                                         #         die Zeit
                                                         #          Zeit
                                                         #     wird geholt
    week = lt.tm_wday                                    #  Wochentag als Zahl
    day = lt.tm_mday                                     #        Datum
    month_int = lt.tm_mon                                #   Monat als Zahl
    year = lt.tm_year                                    #        Jahr
    hour = lt.tm_hour                                    #   aktuelle Stunde
    minute = lt.tm_min                                   #   aktuelle Minute
    second = lt.tm_sec                                   #   aktuelle Sekunde

    #month_int =12
    # day = 31

    #              Zeit wird ausgewertet und die Begrüßung gesetzt:
    if hour>=0 and hour<=3:
        Begr = "Hi, so spät noch aktiv ???"
    if hour>3  and hour<=6:
        Begr = "So früh am Computer? Geh' lieber ins Bett"
    if hour>6  and hour<=8:
        Begr = "Guten Morgen! Schon so früh auf?"
    if hour>8  and hour<=12:
        Begr = "Guten Morgen"
    if hour>12 and hour<=18:
        Begr = "Guten Tag"
    if hour>18 and hour<=23:
        Begr = "Guten Abend"
    if month_int == 12 and day == 24:
        Begr += "\nFrohe Weihnachten User!"
    if month_int == 12 and day == 31:
        Begr += "\nIch wünsche eine feuchtfröhliche Silvester-Party!"
    return ([Begr, wtage[week], day, month[month_int-1], year, hour, minute, second])
#      Begrüßung, Datum und Uhrzeit werden auf Standardgerät ausgegeben:

if __name__ == "__main__":
    date = datetime()
    print(f"\n{date[0]}")
    print(f"\nHeute ist {date[1]}, der {date[2]}. {date[3]} {date[4]}. Es ist {date[5]:02d}:{date[6]:02d}:{date[7]:02d} Uhr\n")

