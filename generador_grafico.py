from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',]
voc = ['a', 'e', 'i', 'o', 'u']

class Aplicacion(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.raiz = Tk()

        self.raiz.geometry('300x300')
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('Generador de palabras')

        
         
        self.gen = ttk.Button(self.raiz, text='Generar texto',
                                command=self.generar)
        self.gen.pack(side=LEFT)
        self.bsalir = ttk.Button(self.raiz, text='Salir',
                                 command=self.raiz.destroy)
        self.bsalir.pack(side=RIGHT)

        self.text = tk.StringVar()
        self.text.set("PALABRA")
        self.label = ttk.Label(self.raiz, text=self.text.get())

        self.gen.pack()
        self.label.pack()
        self.raiz.mainloop()

    def generar(self):
        word = ""
        for i in range(random.randrange(2,10)):
            
            randcon = random.randrange(0,20)
            randvoc = random.randrange(0,4)
            car_a = con[randcon]
            car_b = voc[randvoc]
            preword = car_a + car_b
            word += preword

        self.label.destroy()
        self.text.set(word)
        self.label = ttk.Label(self.raiz, text=self.text.get())
        self.label.pack()

        
            

    def changeText(self):
        self.text.set("Text updated")
        
def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()

