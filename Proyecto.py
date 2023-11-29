from tkinter import *
from tkinter import messagebox #Esta funcion aun no se usa
from tkinter import filedialog
from Huffman import HuffmanCoding

# Funciones
class Hman:
    def __init__(self, root ): 
        self.Huffman = HuffmanCoding()
        self.root = root

#Seleccion, Archivos
    def SeleccionarArchivoTexto(self):
     # Abre un cuadro de diálogo para que el usuario seleccione un archivo
     archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

    # Verifica si el usuario ha seleccionado un archivo
     if archivo:
        with open(archivo, 'r') as file:
            text = file.read()
        # Borra cualquier contenido existente en el Entry
        self.MostrarArchivoTextoSeleccionado.delete(0, "end")
        # Inserta el nuevo contenido en el Entry
        self.MostrarArchivoTextoSeleccionado.insert(0, text)
        
        self.Huffman.set_original_text(text) 
        
#  Seleccion Imagen       
    def SeleccionarImagen():
        imagen = filedialog.askopenfilename(defaultextension=".png", filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif"), ("Todos los archivos", "*.*")])
        if imagen:
            MostrarImageSeleccionada.delete(0, "end")
            MostrarImageSeleccionada.insert(0,  imagen)
            
#Seleccion Audio         
    def SeleccionarArchivoAudio():
        audio = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Archivos de audio", "*.mp3;*.wav"), ("Todos los archivos", "*.*")])
        if audio:
            MostrarAudioSeleccionado.delete(0, "end")
            MostrarAudioSeleccionado.insert(0, audio)
                      
 # Compresor de archivos           
    def Comprimir(self):
        if not self.Huffman.original_text:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo antes de comprimir.")
            return
    
        self.Huffman.calculate_frequency_table()
        self.Huffman.create_huffman_tree()
        self.Huffman.calculate_table_conversion()
     
        BitsComprimidos = self.Huffman.get_compressed_text()
        
        
        compressed_file_path = filedialog.asksaveasfilename(defaultextension=".huff", filetypes=[("Archivos Huffman", "*.huff")])
        if compressed_file_path:
            
            with open(compressed_file_path, 'wb') as compressed_file:
                compressed_file.write(BitsComprimidos.encode('utf-8'))
                
                
                
            original_size = len(self.Huffman.original_text)
            compressed_size = len(BitsComprimidos.encode('utf-8'))  
            return
        original_size/compressed_size
        
           
        
                
                
                
                
                
                
                
        
# Características de la ventana
root = Tk() 
root.title("Proyecto de Estructuras de Datos")
root.iconbitmap("C:/Users/angel/OneDrive/Documentos/Universidad/Segundo año de universidad/Tercer Semestre/Estructuras de datos II/Parcial 3/ProyectoEstructurasDatosIICompresorArchivos/LogoUP.ico")
root.geometry("800x500")
root.resizable(0,0)
MenuBar = Menu(root)
root.config(menu = MenuBar, bg = "blue")
app = Hman(root)


#Este es el titulo de la pagina
Titulo = Label(root, text = "COMPRESOR DE ARCHIVOS", font = ("arial 20"), bg = "blue", fg = "White")
Titulo.place(x = 200, y = 0)


#Aqui mostramos el archivo de texto, imagen y audio

#Archivo de texto
EtiquetaArchivoTexto = Label(root, text="Archivo seleccionado: ", font = ("arial 12"), fg = "White", bg = "blue" )
EtiquetaArchivoTexto.place (x = 0 , y = 50 )
app.MostrarArchivoTextoSeleccionado = Entry(root, bd = 2, width = 102)
app.MostrarArchivoTextoSeleccionado.place(x = 160, y = 50)

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
ArchivoMenu.add_command(label = "Abrir Archivo de Texto", command = app.SeleccionarArchivoTexto)
ArchivoMenu.add_command(label = "Cerrar")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label = "Salir", command = root.quit)

ImagenMenu = Menu(MenuBar, tearoff = 0)
ImagenMenu.add_command(label = "Abrir Imagen", command = app.SeleccionarImagen)

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
 
btnCompresioArchivosTexto = Button(root, text = "Comprimir Archivo", bd = 5, font = ("arial 10"), command = app.Comprimir)
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