from tkinter import *
from tkinter import filedialog
import new

def abrirFileExplorer():
  print("abrir file explorer")
  filename = filedialog.askopenfilename(initialdir = '/',title = "Seleccionar KMZ",filetypes = (("kmz","*.kmz"),))
  
  print(filename)
  ventanaSec = Toplevel()
  ventanaSec.wm_title("Proceso completado!")
  ventanaSec.grab_set()
  
  
  if(ventanaSec):
    final = new.iniciar(filename)

if __name__ == '__main__':    
  window = Tk()
  window.title("UzonEnergy - Subir KMZ")
  window.geometry('600x400')
  btnOpenFileExplorer = Button(window, text="Agregar KMZ's", command=abrirFileExplorer)
  btnOpenFileExplorer.grid(column=1, row=0)
  window.mainloop()


