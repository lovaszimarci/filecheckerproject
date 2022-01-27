from os import system
from subprocess import check_output
import psutil
import time 

signal = True
# EZ NEM MUKSZIK EZT A FUNCTIONT NE NEZD XDDD 
def checkIfProcessRunning(processName):
    global signal
    for proc in psutil.process_iter():
        if processName.lower() in proc.name().lower():
            print(proc)
        else:
            signal = False
# ide kell majd egy cucc ami bele irja hogy ne vesszen el
def txtfile_ereaser():
        with open('hibak.txt', 'r') as content:
            new_content = content.read()
        with open('osszeshibak.txt', 'a') as file:
            file.write(new_content+'\n')
        with open('hibak.txt', 'w') as file:
            file.close()
    
        
while signal == True:
    checkIfProcessRunning('filechecker')
if signal == False:
    txtfile_ereaser()
    print('hahah')
    SystemExit(0)


