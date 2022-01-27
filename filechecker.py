import os
import time
from tkinter import messagebox
from tkinter import *
import sys

#read the given dir from a txt
with open('dir.txt','r', encoding='utf-8' ) as f:
    dir  = f.read()

def size_checker():
    for root, dirs, files in os.walk(dir):
        for f in files:
            size = sys.getsizeof(f)
            print(size)
            if size < 22000:
                dir_of_wrong_file = os.path.dirname(os.path.realpath(f))
                with open('hibak.txt', 'r') as file:
                    content = file.read()
                    if dir_of_wrong_file in content == True:
                        pass
                    if dir_of_wrong_file in content == False:
                        with open('hibak.txt','a') as file:
                            file.write(dir_of_wrong_file+'\n')
                            return False      
            else:
                return True
#show if the given file is in the dir
def measure(subject): 
    global last_dir
    # gives the number of maps in a dir 
    num_of_dir = len(os.listdir(dir)) 
    #counting variables
    j = []  
    b = []
    # loops trough the files in the given dir with os.walk
    for root, dirs, file in os.walk(dir):
        # if the file is retic,than it has a different procedure 
        if subject == 'RETIC':
            for directory  in dirs:
                if ('Blank') in directory:
                    b.append('b')
        for files in file:
            if subject in files:
                j.append('j')
            else: pass 

    sum_subject_file = len(j) 
    if subject == 'RETIC':
       sum_subject_file = sum_subject_file + len(b)      
    print(sum_subject_file)
    # substract the number of files from the number of maps --> we can see the differenc and if the file is missing from the dir 
    if num_of_dir - sum_subject_file != 0:
        last_dir = os.listdir(dir)[-1]
        j.append('j')
        with open('hibak.txt', 'r') as f:
            innertext = f.read()
        with open('hibak.txt', 'a') as f:
            # if the dir is already in the txt file than it skips and show no error 
            if last_dir in innertext:
                print(f'{subject} passed')
                return True
            else:
                # writes the last(wrong) dir in a txt file 
                f.write(last_dir+'\n')
                print(f'{subject} failed')
                return False
    else: 
        print(f'{subject} passed')
        return True

# this is the function for the pop up window
def popup():
    
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    # if yes is selected than it brings us to the dir of the wrong map in file explorer 
    if messagebox.askyesno('Warning', 'You have an error at '+last_dir+'. Do you want to go to the folder?') == True:
        os.startfile(dir + '/' + last_dir)
    else: pass

    window.deiconify()
    window.destroy()
    window.quit()
# this is the loop that scans the files in order
while True: 
    if measure('RBC') == False:
        popup()
    if measure('HGB') == False:
        popup()
    if measure('bloodsensor') == False:
        popup()
    if measure('ResultInfo') == False:
        popup()
    if measure('WBC') == False:
        popup() 
    if measure('RETIC') == False:
        popup()        
    if size_checker() == False:
        popup
    # if the loop ended than it waits five second and than check again
    time.sleep(5)



