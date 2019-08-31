from tkinter import *
window = Tk()
window.title("Merhaba Vektörel")
window.geometry('350x200')
lbl = Label(window, text="Merhaba")
lbl.grid(column=0, row=0)
def tiklandi():
    lbl.configure(text="Tıklandı")
def git():
    import webbrowser as web
    web.open_new("www.ibrahimediz.com")
btn = Button(window, text="Düğmeye Bas",command=tiklandi)
btn.grid(column=1, row=0)
btn2 = Button(window, text="Beni Gör",command=git)
btn2.grid(column=2, row=0)
window.mainloop()