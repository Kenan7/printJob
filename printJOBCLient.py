from tkinter import *
from tkinter.filedialog import askopenfilename
from functionsFile import *
listofShop = ListActiveShops(1)
master = Tk()
master.title("printJOB (Alpha) Executor")
C = Canvas(master, bg="white", height=70, width=400)
C.pack()
variable = StringVar(master)
variable.set('Mağazanı seçin')
w= OptionMenu(master, variable, *listofShop)
w.pack(side='right')
def OpenFile():
    name = askopenfilename(filetypes =(("PDF", "*.pdf"),("Word file","*.doc*")),title = "Fayl seçin")
    print(name)
    name=os.path._getfullpathname(name)
    print(name)
    insertJob(variable.get(),name)
    return print(name)
button1= Button(master, text="Print et", command=OpenFile)
button1.pack(side='left')
def shut():
    master.destroy()
    return
button2=Button(master,text='Bağla',command=shut)
button2.pack()
mainloop()
