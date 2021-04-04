from tkinter import *
import webbrowser

root = Tk()
root.title("Link Runner")

def search():
    url = enter.get()
    webbrowser.open(url)


enter = Entry(root)
enter.pack()

button = Button(root, text="Search", command=search)
button.pack()




root.mainloop()
