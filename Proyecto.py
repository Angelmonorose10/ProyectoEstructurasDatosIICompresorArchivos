from tkinter import *
from tkinter import messagebox #Esta funcion aun no se usa
from tkinter import filedialog

# Características de la ventana
root = Tk() 
root.title("Proyecto de Estructuras de Datos")
root.iconbitmap("C:/Users/angel/OneDrive/Documentos/Universidad/Segundo año de universidad/Tercer Semestre/Estructuras de datos II/Parcial 3/ProyectoEstructurasDatosIICompresorArchivos/LogoUP.ico")
root.geometry("800x500")
root.resizable(0,0)
MenuBar = Menu(root)
root.config(menu = MenuBar, bg = "blue")

# Funciones del programa

# Funciones de seleccion:

# 1.- Archivos de texto.
def SeleccionarArchivoTexto():
     # Abre un cuadro de diálogo para que el usuario seleccione un archivo
    archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    # Verifica si el usuario ha seleccionado un archivo
    if archivo:
        # Borra cualquier contenido existente en el Entry
        MostrarArchivoTextoSeleccionado.delete(0, "end")
        # Inserta el nuevo contenido en el Entry
        MostrarArchivoTextoSeleccionado.insert(0, archivo)

# 2.- Imagenes.
def SeleccionarImagen():
    imagen = filedialog.askopenfilename(defaultextension=".png", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif"), ("Todos los archivos", "*.*")])
    if imagen:
       MostrarImageSeleccionada.delete(0, "end")
       MostrarImageSeleccionada.insert(0,  imagen)
       
# 3.- Audio. 

def SeleccionarArchivoAudio():
    audio = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Archivos de audio", "*.mp3;*.wav"), ("Todos los archivos", "*.*")])
    if audio:
        MostrarAudioSeleccionado.delete(0, "end")
        MostrarAudioSeleccionado.insert(0, audio)
        
# Funciones de compresion de Archivos

       
#Funciones de descompresion de archivos.


#Este es el titulo de la pagina
Titulo = Label(root, text = "COMPRESOR DE ARCHIVOS", font = ("arial 20"), bg = "blue", fg = "White")
Titulo.place(x = 200, y = 0)


#Aqui mostramos el archivo de texto, imagen y audio

#Archivo de texto
EtiquetaArchivoTexto = Label(root, text="Archivo seleccionado: ", font = ("arial 12"), fg = "White", bg = "blue" )
EtiquetaArchivoTexto.place (x = 0 , y = 50 )
MostrarArchivoTextoSeleccionado = Entry(root, bd = 2, width = 102)
MostrarArchivoTextoSeleccionado.place(x = 160, y = 50)

# Imagen
EtiquetaImagen = Label(root, text = "Imagen seleccionada: ", font = ("arial 12"), fg = "white", bg = "blue" )
EtiquetaImagen.place(x = 0, y = 150 )
MostrarImageSeleccionada = Entry(root, bd = 2, width = 102)
MostrarImageSeleccionada.place(x = 160, y = 150)
# Audio

EtiquetaAudio = Label(root, text = "Audio seleccionado: ", font = ("arial 12"), fg = "white", bg = "blue" )
EtiquetaAudio.place(x = 0, y = 250 )
MostrarAudioSeleccionado = Entry(root, bd = 2, width = 102)
MostrarAudioSeleccionado.place(x = 160, y = 250)

# Todo lo de la barra
ArchivoMenu = Menu(MenuBar, tearoff= 0 )
ArchivoMenu.add_command(label = "Abrir Archivo de Texto", command = SeleccionarArchivoTexto)
ArchivoMenu.add_command(label = "Cerrar")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label = "Salir", command = root.quit)

ImagenMenu = Menu(MenuBar, tearoff = 0)
ImagenMenu.add_command(label = "Abrir Imagen", command = SeleccionarImagen)

AyudaMenu = Menu(MenuBar, tearoff = 0)
AyudaMenu.add_command(label = "Ayuda")
AyudaMenu.add_separator() 

AudioMenu = Menu(MenuBar, tearoff = 0)
AudioMenu.add_command( label = "Abrir Audio")

MenuBar.add_cascade( label = "Archivo", menu = ArchivoMenu)
MenuBar.add_cascade( label = "Imagen", menu = ImagenMenu)
MenuBar.add_cascade( label = "Audio", menu = AudioMenu)
MenuBar.add_cascade( label = "Ayuda", menu = AyudaMenu)

# Botones para comprimir y descomprimir los archivos
 
btnCompresioArchivosTexto = Button(root, text = "Comprimir Archivo", bd = 5, font = ("arial 10"))
btnCompresioArchivosTexto.place( x = 50, y = 90 )

btnDescomprimirArchivosTexto = Button(root, text = "Descomprimir Archivo", bd = 5, font = ("arial 10"))
btnDescomprimirArchivosTexto.place(x = 620 , y = 90) 

btnCompresioImagen = Button(root, text = "Comprimir Imagen", bd = 5, font = ("arial 10"))
btnCompresioImagen.place( x = 50, y = 200)

btnDescomprimirImagen = Button(root, text = "Descomprimir Imagen", bd = 5, font = ("arial 10"))
btnDescomprimirImagen.place(x = 620 , y = 200) 

btnCompresioAudio = Button(root, text = "Comprimir Audio", bd = 5, font = ("arial 10"))
btnCompresioAudio.place( x = 50, y = 300 )

btnDescomprimirAudio = Button(root, text = "Descomprimir Audio", bd = 5, font = ("arial 10"))
btnDescomprimirAudio.place(x = 620 , y = 300) 







root.mainloop()