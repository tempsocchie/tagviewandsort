import os
import random
import tkinter
from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog

#from PIL import ImageTk, Image

def enstrfolder():
    folder_path_var = tk.StringVar()
    prompt1_var = tk.StringVar()
    prompt2_var = tk.StringVar()
    prompt3_var = tk.StringVar()
    prompt4_var = tk.StringVar()
    prompt5_var = tk.StringVar()
    status_var = tk.StringVar()


def dothesearch():
    browse_folders
    files = os.listdir(os.getcwd)
    #for file in files: #split the filename apart
        #if

root = Tk()
# create mainwin window
#mainwin = ttk.Frame(height=1000, width=1000, bg='purple')
#mainwin.title("DECIDE")
#mainwin.geometry('1000x1000')
#mainwin.state('zoomed')
#, background = 'BLACK'
#searchwin = ttk.Frame(mainwin)
#searchwin.pack()
#searchwin.place(x=20, y=20)

searchbar = ttk.Entry()

nestedgrid = Frame()
for r in range(2):
    for c in range(10):
        Button(nestedgrid, borderwidth=1).grid(row=r, column=c, ipadx=60, ipady=35)

nestedsearch = Frame()
for r in range(5):
    for c in range(1):
        Entry(nestedsearch, borderwidth=1).grid(row=r, column=c, ipadx=60, ipady=35)

for r in range(1):
    for c in range(1):
        #Button(root).grid(row=r, column=c)
        Button(root, padx=100, pady=70, text=str("options1"), borderwidth=3).grid(row=0, column=0)
        nestedgrid.grid(row=0, column=1)
        nestedsearch.grid(row=1, column=0)
        Button(root, padx=700, pady=300, text=str("picgrid"), borderwidth=3).grid(row=1, column=1)
        Button(root, padx=100, pady=30, text=str("err"), borderwidth=3).grid(row=2, column=0)
        Button(root, padx=400, pady=30, text=str("err"), borderwidth=3).grid(row=2, column=1)


#entered_tag = ttk.StringVar()
#gosearch = ttk.Button(searchwin, text="do the search", command = dothesearch)

#searchbar.grid(row = 0, column = 0, sticky=W)
#gosearch.grid(row = 1, column = 0, sticky=W)

#def rescalepic(imgdim):
#    eitherdim = [50]
#    for smallerdim in eitherdim:
#        iheight = float(str(imgdim.height))
#        iwidth = float(str(imgdim.width))
#        if iheight > iwidth:
#            maxsize = (100,100)
#            imgex1.thumbnail(maxsize)
#        else:
#            maxsize = (100,100)
#            imgex1.thumbnail(maxsize)
 
#maingridsection = Frame(mainwin, bg='PURPLE')
#maingridsection.place(x=300, y=10)

def go_left():
    if pagenumref >= 1:
        if pagenumref == curr_max_page:
            right_select.pack(side='right')
        pagenumref = pagenumref - 1
        if pagenumref == 0:
            left_select.forget_pack()
        currentpage.pack_forget()
        currentpage = newpage
        currentpage.pack()

def go_right():
    if pagenumref <= curr_max_page:
        if pagenumref == 0:
            left_select.pack(side='left')
        pagenumref = pagenumref + 1
        if pagenumref == curr_max_page:
            right_select.forget_pack()
        currentpage.pack_forget()
        currentpage = newpage
        currentpage.pack()

def grid_select_buttons(): #the left/right buttons
    leftright_frame = Frame() #maingridsection
    leftright_frame.pack(side='bottom')
    left_select = Button(leftright_frame, bg='grey', text = "left", command=go_left)
    right_select = Button(leftright_frame, bg='grey', text = "right", command=go_right)
    #if currentpage == 0: #un-pack current grid page, pack new grid page
    left_select.pack(side='left')
    right_select.pack(side='right')
    pagenums = 0

#class make_new_grid(): #need to add left/right buttons too
def testgrid():
    entries = [[None for col in range(8)] for row in range(5)]
    for row in range(5):
        for col in range(8): #maingridsection
            thegrid = ttk.Frame(mainwin)
            thegrid.grid(row=row, column=col, ipady=50)
            entries[row][col] = thegrid
            thegrid.bind('<Button-1>', lambda e, row=row, col=col: on_click(row,col,e))

###############
# tag sorting #
###############
def browse_folders():
    os.chdir(filedialog.askdirectory())

def sort_tags(splitthis):
    splitthis, file_ext = os.path.splitext(splitthis)
    splitted, filenumber = splitthis.split("-")
    sortedfile = sorted(splitted.split("_"))
    splitted = '_'.join(sortedfile) + "-" + filenumber + file_ext

def splitfiletags(splitthis):
    splitthis, file_ext = os.path.splitext(splitthis)
    splitted, filenumber = splitthis.split("-")
    enlist = splitted.split("_")
    
def rename_files_prompt(): #needs to be the 5 boxes
    folder_path = tk.StringVar()
    prompt1, prompt2, prompt3, prompt4, prompt5 = tk.StringVar()

    # Create a new folder inside the current folder
    new_folder_path = os.path.join(folder_path, "Renamed_Files")
    os.makedirs(new_folder_path, exist_ok=True)

    files = os.listdir(folder_path)
    for file in files:
        suffix = ("jpg", "png", "gif")
        if file.endswith(suffix):
        #if os.path.isfile(os.path.join(folder_path, file)):
            file_name, file_ext = os.path.splitext(file)
            # что, если только 3 тега используются с символом «_» между
            new_file_name = f"{prompt1}{prompt2}{prompt3}{prompt4}{prompt5}{random.randint(0000, 9999)}{file_ext}"
            new_file_path = os.path.join(new_folder_path, new_file_name)
            os.rename(os.path.join(folder_path, file), new_file_path)

def checkfiletype(fname):
    #suffix = ("jpg", "png", "gif")
    rightfiles = []
    if fname.endswith("jpg", "png", "gif"):
        rightfiles.append()

##############
# grid stuff #
##############

#thiswidget.bind('<Button-1>', clicktoselect)

def clickgrid(x, y, selected, specgrid):
    backcolour = "dark slate gray"
    selected.widget.config(bg = backcolour) #need to make thumbnail 90x90
    specgrid[x][y] = backcolour
    #filena = #get string from clicking widget, but has to be specific grid box
    
def unselectgrid(x, y, selected, specgrid):
    backcolour = "gray"
    selected.widget.config(bg = backcolour) #need to make thumbnail 90x90
    specgrid[x][y] = backcolour
    #filena = #get string from clicking widget, but has to be specific grid box
pagenums = 0
allpagenums = []

def addtogrid(rightfiles): #for adding pics to the grid
    while len(rightfiles) > 0:
        rowx = 0
        coly = 0
        for file in rightfiles:
            while rowx < 5:
                while coly < 8:
                    #print(rightfiles.pop())
                    filena = Image.open(str()) #should do that at least reference
                    filep1 = Image.open(str(rightfiles.pop()))
                    filep2 = filep1.thumbnail(maxsize)
                    filep3 = ImageTk.PhotoImage(filep1)
                    #filep4 to be 1st, 2nd, etc'rd from list
                    filep4 = Label(maingridsection, image=filep3)
                    filep4.image = filep3
                    filep4.grid(row=rowx, column=coly) #this makes the grid
                    filep4.frame(maingridsection)
                    coly += 1
                rowx += 1
                coly = 0
            if rowx == 6:
                key = "page" + str(curr_max_page)
                allpagenums[key] = filep4
                curr_max_page += 1
    #когда будет достигнуто 40, перейдите к совершенно новому виджету

#for file in os.listdir(r"C:\Users\succy\Documents\TKinter"):
#    if file.endswith(r".txt"):
#        print(file)
        
# Tkinter event loop
root.mainloop()