import os
import random, string
import tkinter
from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
#from PIL import ImageTk, Image
from tkinter.ttk import *

root = Tk() ############################################################################################################
root.state('zoomed')

rightfiles = []
archived = []
suffix = ("jpg", "png", "gif")

###############
# tag sorting #
###############

def sort_tags(splitthis):
    splitthis, file_ext = os.path.splitext(splitthis)
    splitted, filenumber = splitthis.split("-")
    sortedfile = sorted(splitted.split("_"))
    splitted = '_'.join(sortedfile) + "-" + filenumber + file_ext

def rename_files_prompt(): #needs to be the 5 boxes
    folder_path = filedialog.askdirectory()
    files = os.listdir(folder_path)
    filecount = 0
    new_folder_path = os.path.join(folder_path, "Renamed_Files")
    os.makedirs(new_folder_path, exist_ok=True)
    for file in files:
        if file.endswith(suffix):
        #if os.path.isfile(os.path.join(folder_path, file)):
            file_name, file_ext = os.path.splitext(file)
            # что, если только 3 тега используются с символом «_» между
            new_file_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
            new_file_name = f"{tag1}_{tag2}_{tag3}_{tag4}_{tag5}-{new_file_name}{file_ext}"
            new_file_path = os.path.join(new_folder_path, new_file_name)
            os.rename(os.path.join(folder_path, file), new_file_path)
            filecount += 1
    print(filecount)

def checkfiletype(fname):
    suffix = ("jpg", "png", "gif")
    rightfiles = []
    if fname.endswith(suffix):
        rightfiles.append()
    print(rightfiles)
#select folder for finding the right files (unsorted pics)
def dothesearch():
    filecount=0
    global thisfolder
    thisfolder = os.path.abspath(filedialog.askdirectory())
    files = os.listdir(thisfolder)
    for file in files: #split the filename apart
        file_path = os.path.join(thisfolder, file)
        if file.endswith(suffix):
            rightfiles.append(file)
            archived.append(file_path)
            filecount+=1

def renameselected():
    new_folder_path = os.path.join(thisfolder, "Renamed_Files")
    os.makedirs(new_folder_path, exist_ok=True)
    print(templist)
    for file in templist:
        file_name, file_ext = os.path.splitext(file)
        # что, если только 3 тега используются с символом «_» между
        new_file_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        new_file_name = f"{tag1}_{tag2}_{tag3}_{tag4}_{tag5}-{new_file_name}{file_ext}"
        new_file_path = os.path.join(new_folder_path, new_file_name)
        os.rename(os.path.join(thisfolder, file), new_file_path)

#for adding pics to the grid
def taddtogrid():
    dothesearch()
    rowx = 0
    coly = 0
    for rowx in range(9):
        for coly in range(9):
            if len(rightfiles) != 0:
                #thatphoto=rightfiles[0],thephoto=Image.open(thatphoto),thisphoto = PhotoImage(thephoto)
                rightfiles[0]=Button(nestedgrid, command=lambda m=rightfiles[0]: gettestcoords(m), text=rightfiles[0]).grid(row=rowx, column=coly,sticky='nsew')
                rightfiles.pop(0)
            else:
                Button(nestedgrid).grid(row=rowx,column=coly,ipadx=50,ipady=50)
            #key = str(gridpage+"-"+rowx+coly)
            #archivedfilepaths[key] = filana
            coly += 1
        rowx += 1
        coly = 0
    newtestbutton = Button(buttonoptions, text="woo", command=renameselected)
    newtestbutton.grid(row=3, column=0, sticky='we')
    global newtesttbutton

def addtogrid(): #original
    #while len(rightfiles) > 0:
    rowx = 0
    coly = 0
    for file in rightfiles:
        while rowx < 5:
            while coly < 8:
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
templist = []

def gettestcoords(button_press):
    templist.append(button_press)
    print(templist)

class makebuttons:
    def __init__(self, parent, name, brow, bcol): #filename, pathway
        self.parent = parent
        self.name = name
        #self.filename = filename
        #self.pathway = pathway
        Button(nestedgrid, command=lambda m=name: gettestcoords(m), text=name).grid(row=brow, column=bcol, ipadx=50, ipady=50)

def makeagrid():
    testlist = []
    for tr in range(8):
        for tc in range(10):
            currentbutton = ("p1"+str(tr)+str(tc))
            testlist.append(currentbutton)
            currentbutton = Button(nestedgrid, command=lambda m=currentbutton: gettestcoords(m), text=currentbutton)
            currentbutton.grid(row=tr, column=tc, ipadx=50, ipady=50)

def thenclosegrid():
    for tr in range(8):
        for tc in range(9):
            currentbutton = ("p2"+str(tr)+str(tc))
            makebuttons(nestedgrid, currentbutton, tr, tc)

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

def tagassign():
    global tag1, tag2, tag3, tag4, tag5
    tag1, tag2, tag3, tag4, tag5 = etag1.get(), etag2.get(), etag3.get(), etag4.get(), etag5.get()

### the actual buttons ###
for r in range(5):
    for c in range(2):
        tk.Button(buttonoptions, text="Do the search", command=dothesearch).grid(row=0, column=0, sticky='we')
        tk.Button(buttonoptions, text="set tags", command=tagassign).grid(row=0, column=1, sticky='we')
        tk.Button(buttonoptions, text="make an grid", command=makeagrid).grid(row=1, column=0, sticky='we')
        tk.Button(buttonoptions, text="set folder", command=lambda: print(rightfiles)).grid(row=1, column=1, sticky='we')
        tk.Button(buttonoptions, text="add to grid", command=taddtogrid).grid(row=2, column=0, sticky='we')
        tk.Button(buttonoptions, text="assign", command=rename_files_prompt).grid(row=2, column=1, sticky='we')
        tk.Button(buttonoptions).grid(row=r, column=c, sticky='we')
### empty image base grid ###
#for r in range(8):
#    for c in range(10):
#        Button(nestedgrid, text="000", fg='white').grid(row=r, column=c, ipadx=50, ipady=50)
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


root.mainloop()
