import time
import os, sys

def clear():
    try:
        s = sys.winver
        os.system('cls') 
    except: 
        os.system('clear')
        
def date():
    lt = time.localtime()
    date = '{:02d}.'.format(lt.tm_mday)
    date += '{:02d}.'.format(lt.tm_mon)
    date += '{:04d}'.format(lt.tm_year)
    return(date)

def time_now():
    lt = time.localtime()
    time_now = '{:02d}:'.format(lt.tm_hour)
    time_now += '{:02d}:'.format(lt.tm_min)
    time_now += '{:02d}'.format(lt.tm_sec)
    return(time_now)

if __name__ == '__main__':
    clear()
    print(date(), end='  ')
    print(time_now())
    
    
