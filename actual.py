import os
import random, string
import tkinter
from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
#from PIL import ImageTk, Image

root = Tk() ############################################################################################################

rightfiles = []
archived = []

def addtoarchive():
    storedfilepath = str(gridpage)+"-"+str(rowx, coly)
    allpagenums[storedfilepath] = file

def browse_folders():
    os.chdir(filedialog.askdirectory())

#select folder for finding the right files (unsorted pics)
def dothesearch():
    suffix = ("jpg", "png", "gif")
    thisfolder = os.path.abspath(filedialog.askdirectory())
    files = os.listdir(thisfolder)
    for file in files: #split the filename apart
        file_path = os.path.join(thisfolder, file)
        if file.endswith(suffix):
            rightfiles.append(file)
            print(file)
            print(file_path)
            archived.append(file_path)

#for adding pics to the grid
def addtogrid():
    while len(rightfiles) > 0:
        rowx = 0
        coly = 0
        for file in rightfiles:
            while rowx < 5:
                while coly < 8:
                    #print(rightfiles.pop())
                    filana = str(file) #should do that at least reference
                    filep1 = Image.open(str(rightfiles.pop()))
                    rightfiles.remove(file)
                    filep2 = filep1.thumbnail(maxsize)
                    filep3 = ImageTk.PhotoImage(filep1)
                    #filep4 to be 1st, 2nd, etc'rd from list
                    filep4 = Label(maingridsection, image=filep3)
                    filep4.image = filep3
                    filep4.grid(row=rowx, column=coly)
                    filep4.frame(nestedgrid)
                    key = str(gridpage+"-"+rowx+coly)
                    archivedfilepaths[key] = filana
                    coly += 1
                rowx += 1
                coly = 0
            if rowx == 6:
                key = "page" + str(curr_max_page)
                allpagenums[key] = filep4
                curr_max_page += 1
    #когда будет достигнуто 40, перейдите к совершенно новому виджету

#test grid making/swapping
testarchived={}
buttonnames=[]

def makegridbutton():
    buttonnames.append(str("o")+str(tr)+str(tc))
    thispage = str(tr)+str(tc)
    testarchived[thispage] = buttonnames[0]
def gettestcoords():
    print("uh")

def makeagrid():
    testgridpage=0
    testfilana=0
    for tr in range(4):
        for tc in range(4):
            class makebuttons:
                def __init__(self, parent, name):
                    identify = str(tr)+str(tc)
                    print(identify)
                    self.parent = parent
                    self.name = name
                    self.identify = identify
                    Button(nestedgrid, command=gettestcoords, text=name).grid(row=tr, column=tc, ipadx=50, ipady=50)
            currentbutton = (str("o")+str(tr)+str(tc))
            makebuttons(nestedgrid, currentbutton)
            #buttonnames[0] = Button(nestedgrid, command=gettestcoords, text=(buttonnames[0]))
            #buttonnames[0].grid(row=tr, column=tc, ipadx=50, ipady=50)
            #buttonnames.pop(0)

def thenclosegrid():
    for r in range(5):
        for c in range(8):
            Button(nestedgrid, text=str("2")).grid(row=r, column=c, ipadx=50, ipady=50)
def testgrid():
    print(rightfiles)
    print(archived)

def settags(): #this works, don't remove, is test
    tag1, tag2, tag3, tag4, tag5 = etag1.get(), etag2.get(), etag3.get(), etag4.get(), etag5.get()
    print(tag1)

nestedgrid = Frame(width=800, height=500)
nestedgrid.pack(side=RIGHT)
searchbar = Frame(root)
searchbar.pack(side=LEFT)

##### entry widgets/ #####
etag1 = tk.Entry(searchbar, width=30)
etag2 = tk.Entry(searchbar, width=30)
etag3 = tk.Entry(searchbar, width=30)
etag4 = tk.Entry(searchbar, width=30)
etag5 = tk.Entry(searchbar, width=30)
for c in sorted(searchbar.children):
    searchbar.children[c].pack()
buttonoptions = Frame(searchbar)
buttonoptions.pack()
##### /entry widgets #####

for r in range(5):
    for c in range(2):
        tk.Button(buttonoptions, text="make an grid", command=makeagrid).grid(row=0, column=0, sticky='we')
        tk.Button(buttonoptions, text="close er grid").grid(row=0, column=1, sticky='we')
        tk.Button(buttonoptions, text="Do the search").grid(row=1, column=0, sticky='we')
        tk.Button(buttonoptions, text="set tags").grid(row=1, column=1, sticky='we')
        tk.Button(buttonoptions).grid(row=r, column=c, sticky='we')


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

def on_click(p,i,j,arched): #linking clicks specific gridpos to archived filepath. Example ref = 1-32
    for coord in coordslist:
        p, i, j = coord[0], coord[2], coord[3]
        str(p+"-"+i+j)

def testgrid():
    entries = [[None for col in range(8)] for row in range(5)]
    for row in range(5):
        for col in range(8): #maingridsection
            thegrid = ttk.Frame(mainwin)
            thegrid.grid(row=row, column=col, ipady=50)
            entries[row][col] = thegrid
            #thegrid.bind('<Button-1>': on_click(row,col))

###############
# tag sorting #
###############

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
            new_file_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
            new_file_name = f"{prompt1}{prompt2}{prompt3}{prompt4}{prompt5}{new_file_name}{file_ext}"
            new_file_path = os.path.join(new_folder_path, new_file_name)
            os.rename(os.path.join(folder_path, file), new_file_path)

def checkfiletype(fname):
    suffix = ("jpg", "png", "gif")
    rightfiles = []
    if fname.endswith(suffix):
        rightfiles.append()
    print(rightfiles)

##############
# grid stuff #
##############

#certainwidget.bind('<Button-1>', clicktoselect)
    
def unselectgrid(x, y, selected, specgrid):
    if clickcount == 0:
        backcolour = "gray"
        clickcount = 1
    else:
        backcolour = "dark slate gray"
        clickcount = 0
    selected.widget.config(bg = backcolour) #need to make thumbnail 90x90
    specgrid[x][y] = backcolour
    #filena = #get string from clicking widget, but has to be specific grid box
pagenums = 0
allpagenums = []


root.mainloop()
