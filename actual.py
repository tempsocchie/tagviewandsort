import os
import random, string
import tkinter
from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter.ttk import *

root = Tk() ############################################################################################################
root.state('zoomed')
archived = []
rightfiles = []
suffix = ("jpg", "png", "gif", "ppm", "pgm")

def gettestcoords(button_press):
    templist.append(button_press)
    print(button_press)

###############
# tag sorting #
###############

def doublechecktags(thetag, tagssplitfrom):
    if thetag not in tagssplitfrom:
        if thetag != "":
            thetag ="_"+thetag
            tagssplitfrom.append(thetag)

def sort_tags(splitthis):
    global temptaglist
    temptaglist=[]
    splitthis, file_ext = os.path.splitext(splitthis)
    if splitthis.endswith('z'):
        tagssplitfrom, filenumber = splitthis.split("-")
        tagssplitfrom = tagssplitfrom.split("_")
        for tags in tagstoadd:
            doublechecktags(tags, tagssplitfrom)
    else:
        tagssplitfrom = splitthis
        filenumber = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))+"z"
    tagssplitfrom.sort()
    stringedlist = "".join(tagssplitfrom)
    global reformedfilename
    reformedfilename = stringedlist + "-" + filenumber + file_ext

def rename_files_prompt():
    new_folder_path = os.path.join(thisfolder, "Renamed_Files")
    os.makedirs(new_folder_path, exist_ok=True)
    tagassign()
    tags = '_'.join(tagstoadd)
    for file in rightfiles:
        if file.endswith(suffix):
            file_name = tags+file
            new_file_path = os.path.join(new_folder_path, file_name)
            os.rename(os.path.join(thisfolder, file), new_file_path)

filepaths = []

#select folder for finding the right files (unsorted pics)
def dothesearch():
    global thisfolder
    thisfolder = os.path.abspath(filedialog.askdirectory())
    files = os.listdir(thisfolder)
    for file in files: #split the filename apart
        if file.endswith(suffix):
            file_path = os.path.join(thisfolder, file)
            filepaths.append(file_path)
            rightfiles.append(file)
            archived.append(file_path)

def renameselected():
    tagassign()
    new_folder_path = os.path.join(thisfolder, "Renamed_Files")
    os.makedirs(new_folder_path, exist_ok=True)
    #newpage.forget()

    for file in templist:
        sort_tags(file)
        new_file_path = os.path.join(thisfolder, reformedfilename)
        os.rename(os.path.join(thisfolder, file), new_file_path)
    buttonnames.clear()
    #makegridframe()
    #for rowx in range(9):
    #    for coly in range(7):
    #        Button(newpage).grid(row=rowx, column=coly, ipadx=50, ipady=50)
    templist.clear()

def originalrenameselected(): ###perhaps to be unused
    tagassign()
    new_folder_path = os.path.join(thisfolder, "Renamed_Files")
    os.makedirs(new_folder_path, exist_ok=True)
    #newpage.forget()

    for file in templist:
        sort_tags(file)
        file_name, file_ext = os.path.splitext(file)
        # что, если только 3 тега используются с символом «_» между
        new_file_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
        new_file_path = os.path.join(thisfolder, new_file_name)
        os.rename(os.path.join(thisfolder, file), new_file_path)
    buttonnames.clear()
    #makegridframe()
    #for rowx in range(9):
    #    for coly in range(7):
    #        Button(newpage).grid(row=rowx, column=coly, ipadx=50, ipady=50)
    templist.clear()

def makegridframe():
    global newpage
    currentpage = 1
    newpage = "page"+str(currentpage)
    newpage = Frame(nestedgrid)
    newpage.pack()


            
#for adding pics to the grid
def taddtogrid():
    tk.Button(buttonoptions, text="set tags", command=tagassign).grid(row=0, column=1, sticky='we')
    newtestbutton = Button(buttonoptions, text="spec tagging", command=renameselected)
    newtestbutton.grid(row=3, column=0, sticky='we')
    #makegridframe()
    rowx = 0
    coly = 0
    if len(rightfiles) > 0:
        for rowx in range(3):
            for coly in range(3):
                if len(rightfiles) != 0:
                    n=0
                    print(filepaths[0])
                    n+=1
                    resize1 = Image.open(filepaths[0])
                    resize_image = resize1.resize((100,100))
                    currentimage = ImageTk.PhotoImage(resize_image)
                    #currentimage = currentimage+str(n+1)
                    filepaths.pop(0)
                    label = Label(image=currentimage)
                    label.image = currentimage # keep a reference!
                    label.pack()
                    thetext = rightfiles[0]
                    thetext = Button(nestedgrid, command=lambda m=thetext: gettestcoords(m), image=currentimage).grid(row=rowx, column=coly,sticky='nsew')
                    rightfiles.pop(0)
                else: Button(nestedgrid).grid(row=rowx,column=coly,ipadx=50,ipady=50)
                coly += 1
        rowx += 1
        coly = 0
        if rowx == 10:
            if len(rightfiles) != 0:
                rowx = 0
                currentpage += 1

def addtogrid(): #original
    #while len(rightfiles) > 0:
    rowx = 0
    coly = 0
    for file in rightfiles:
        while rowx < 9:
            while coly < 7:
                filana = str(file) #should do that at least reference
                filep1 = Image.open(str(rightfiles.pop()))
                rightfiles.remove(file)
                filep2 = filep1.thumbnail(maxsize)
                filep3 = ImageTk.PhotoImage(Image.open(filep1))
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

def makeagrid():
    testlist = []
    for tr in range(9):
        for tc in range(7):
            currentbutton = ("p1"+str(tr)+str(tc))
            testlist.append(currentbutton)
            currentbutton = Button(newpage, command=lambda m=currentbutton: gettestcoords(m), text=currentbutton)
            currentbutton.grid(row=tr, column=tc, ipadx=50, ipady=50)

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

def clearpreviousname():
    new_folder_path = os.path.join(thisfolder, "Renamed_Files")
    os.makedirs(new_folder_path, exist_ok=True)
    for file in rightfiles:
        filename, file_ext = os.path.splitext(file)
        if (len(filename)!=6 or filename[-6] != '-' or filename[-1] != 'z'):
            filename = '-'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))+'z'
            filename = filename+file_ext
            new_file_path = os.path.join(new_folder_path, filename)
            os.rename(os.path.join(thisfolder, file), new_file_path)
    rightfiles.clear()

def tagassign():
    global tagstoadd
    tagstoadd = []
    global tag1, tag2, tag3, tag4, tag5
    tag1, tag2, tag3, tag4, tag5 = etag1.get(), etag2.get(), etag3.get(), etag4.get(), etag5.get()
    tagstoadd.extend([tag1, tag2, tag3, tag4, tag5])


### the actual buttons ###
for r in range(5):
    for c in range(2):
        tk.Button(buttonoptions, text="gen folder to grid", command=lambda:[dothesearch(),taddtogrid()]).grid(row=0, column=0, sticky='we')
        #tk.Button(buttonoptions, text="set tags", command=tagassign).grid(row=0, column=1, sticky='we')
        tk.Button(buttonoptions, text="make plain grid", command=makeagrid).grid(row=1, column=0, sticky='we')
        tk.Button(buttonoptions, text="tag all files", command=lambda:[dothesearch(),rename_files_prompt()]).grid(row=1, column=1, sticky='we')
        tk.Button(buttonoptions, text="clear name", command=lambda:[dothesearch(),clearpreviousname()]).grid(row=2, column=0, sticky='we')
        tk.Button(buttonoptions, text="unused", command=lambda:[print(rightfiles)]).grid(row=2, column=1, sticky='we')
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


root.mainloop()
