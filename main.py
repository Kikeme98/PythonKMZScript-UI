from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter
import new

kmzAgregado = 0

def abrirFileExplorer():
  if(kmzAgregado!=0):
    print("abrir file explorer")
    filename = filedialog.askopenfilename(initialdir = '/',title = "Seleccionar KMZ",filetypes = (("kmz","*.kmz"),))
    
    print(filename)
    
    final = new.iniciar(filename)

window = Tk()
txtInputKMZNumero = Entry()
comboboxTipoKMZ = ttk.Combobox(window,state="readonly" )
comboboxTipoKMZ.set("Seleccione el tipo")
comboboxTipoKMZ["values"] = ["LED", "Haluro", "Vapor", "Prueba"]

def registrarKMZ():
  print("Registrando KMZ")
  print(txtInputKMZNumero.get())
  kmzAgregado = new.registrarKMZEnBD(txtInputKMZNumero.get(), comboboxTipoKMZ.get())
  print(kmzAgregado)



titulo = Label(text="Subir KMZ - Uzon Energy", )
btnOpenFileExplorer = Button(window, text="Agregar KMZ's", command=abrirFileExplorer)
btnAgregarKMZ = Button(window, text="Registrar KMZ", command=registrarKMZ)




if __name__ == '__main__':    
  window.title("UzonEnergy - Subir KMZ")
  window.geometry('400x400')
  titulo.grid(column=1, row=0)
  txtInputKMZNumero.grid(column=1, row=1)
  btnAgregarKMZ.grid(column=3, row=1)
  comboboxTipoKMZ.grid(column=2, row=1)
  btnOpenFileExplorer.grid(column=1, row=3)
  window.mainloop()

