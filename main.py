from tkinter import *
from PIL import ImageTk,Image
import google
import bbc
import ny
import cnn
import guardian

master = Tk() 
master.title("Trending News")
master.iconbitmap('assets\\icon.ico')
master.geometry('970x610')
master.configure(bg='#314057')
#master.resizable(0,0)
label_spaceTop=Label(master,text=" ",bg='#314057',width=970)
label_spaceTop.pack()
photo = PhotoImage(file ="assets\\logo.png")
label_image=Label(master,image=photo)
#label_image.grid(row=1,column=1)
label_image.pack()
label_space=Label(master,text=" ",bg='#314057',width=970)
label_space.pack()
label_line=Label(master,text=" ",bg='#314057',width=970)
label_line.pack()
f1 = Frame(master)
f1.configure(bg='#314057')
def getGoogle():
 g_news=google.getFromGoogle()
 display(g_news)

def getBbc():
 b_news=bbc.getFromBbc()
 display(b_news)


def getNy():
 ny_news=ny.getFromNy()
 display(ny_news)


def getCnn():
 cnn_news=cnn.getFromCnn()
 display(cnn_news)

def getGuardian():
 guardian_news=guardian.getFromGuardian()
 display(guardian_news)

def display(news):
 print('Displaying...')
 clearDisplay()
 for item in news:
  #if item.pubDate in news:
  listbox.insert(END, "Posted: "+item.pubDate.text+"")
  listbox.insert(END, " ")
  listbox.insert(END, "Title: "+item.title.text)
  listbox.insert(END, " ")
  listbox.insert(END, "Link: "+item.link.text)
  listbox.insert(END, " ")
  listbox.insert(END,"-"*400)


def clearDisplay():
 print('Clearing list...')
 listbox.delete(0, END)


b1 = Button(f1, text="Google Trending News",font=("Helvetica", 11),command=getGoogle)
b2 = Button(f1, text="BBC",font=("Helvetica", 11),command=getBbc)
b3 = Button(f1, text="CNN",font=("Helvetica", 11),command=getCnn)
b4 = Button(f1, text="The Guardian",font=("Helvetica", 11),command=getGuardian)
b5 = Button(f1, text="The New York Times",font=("Helvetica", 11),command=getNy)
f1.pack()


b1.grid(row=0, column=0,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6)
b2.grid(row=0, column=5,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6)
b3.grid(row=0, column=10,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6)
b4.grid(row=0, column=15,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6)
b5.grid(row=0, column=20,columnspan=4, rowspan=4,
               sticky=W+E+N+S, padx=6, pady=6)
f2 = Frame(master)
f2.configure(bg='#827857')
f2.pack()
scrollbar = Scrollbar(f2)
scrollbar.pack( side = RIGHT, fill = Y )
listbox = Listbox(f2,width=200,bg="light blue",foreground="#000000",height=100, font=("Helvetica", 12),yscrollcommand = scrollbar.set)
listbox.pack()
listbox.pack( side = LEFT, fill = BOTH)
scrollbar.config( command = listbox.yview)


if __name__ == '__main__':
 print("Starting...")
 master.mainloop()