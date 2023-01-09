import tkinter
import tkinter.filedialog
import tkinter.font
import webbrowser
from tkinter import *
from tkinter.font import Font

def ouvrir():
    ouvrir_fichier = tkinter.filedialog.askopenfilename(title='Open a existing file',defaultextension='.txt',filetypes=[("Text file",".txt")])
    name = ouvrir_fichier
    if ouvrir_fichier:
        affichertexte = open(ouvrir_fichier, 'r')
        lecture = affichertexte.readlines()
        blocnote.title(f'{name} - Eon notes')
        for ligne in lecture:
            affichetxt.insert("end", ligne)
    else:
        blocnote.title("Please select a file in order to open one :)")

def saveFile():
    file = tkinter.filedialog.asksaveasfile(title='Save',initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(affichetxt.get(1.0,END))
    file.write(filetext)
    file.close()





blocnote = tkinter.Tk()
blocnote.title("Welcome! Select a text file or start writing one to get started !")
blocnote.geometry('850x500')
blocnote.minsize(400, 350)
blocnote.iconbitmap('logo.ico')
labelopen = tkinter.Label(relief=FLAT) # KAT KHDM FIHA SAVE
affichetxt = tkinter.Text(font=('',9),relief=FLAT,undo=TRUE) # KAT OPENI FIHA FILES
affichetxt.pack(fill=BOTH)

# menus
menubar = tkinter.Menu(blocnote)
menu_fichier = tkinter.Menu(menubar, tearoff=0)
menu_edition = tkinter.Menu(menubar, tearoff=0)
menu_options = tkinter.Menu(menubar, tearoff=0)

# racine menu
menubar.add_cascade(label='File', menu=menu_fichier)
menubar.add_cascade(label='Edition', menu=menu_edition)
menubar.add_cascade(label='Options', menu=menu_options)
blocnote.config(menu=menubar)

def newfile():
    affichetxt.delete(1.0, END)
    blocnote.title("New .txt file - Eon blocnote")

#cascade ficher
menu_fichier.add_command(label='Open',command=ouvrir)
menu_fichier.add_command(label='New',command=newfile)
menu_fichier.add_command(label='Save',command=saveFile)
menu_fichier.add_separator()
menu_fichier.add_command(label='Exit',command=lambda: blocnote.destroy())

def redo():
    affichetxt.edit_redo

def undo():
    affichetxt.edit_undo

def crtlz():
    blocnote.bind("<Control-z>",command=undo)

def ctrls():
    blocnote.bind('<Control-s>',command=saveFile)


#cascade edition
menu_edition.add_command(label='Undo',command=undo)
menu_edition.add_command(label='Redo',command=affichetxt.edit_redo)

#cascade options
def darkmod():
    blocnote.config(background='#2a2a31')
    affichetxt.config(bg='#2a2a31',fg='White')
    menu_edition.config(bg='#2a2a31',fg='White')
    menu_fichier.config(bg='#2a2a31',fg='White')
    menu_options.config(bg='#2a2a31',fg='White')
    menubar.config(bg='#2a2a31')
def whitemode():
    blocnote.config(background='White')
    affichetxt.config(bg='White',fg='Black')
    menu_edition.config(bg='White',fg='Black')
    menu_fichier.config(bg='White',fg='Black')
    menu_options.config(bg='White',fg='Black')
    menubar.config(bg='White')

def docs():
    webbrowser.open_new_tab('https://github.com/Cloakedshiny/Cloakedshiny')
menu_options.add_command(label='Dark Mode',command=darkmod)
menu_options.add_command(label='White mode',command=whitemode)
menu_options.add_separator()
menu_options.add_command(label='Documentation',command=docs)

blocnote.mainloop()