from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Huffman import HuffmanCoding
from PIL import Image, ImageTk
import wave
import cv2
import numpy as np
import os
from bitarray import bitarray

# pip install wave
# pip install opency-python
# pip install bitarray

# En este commit he intentado abrir los archivos separandolos frame a frame y también he creado una función
# que permit (en teoría) llamara a la instamcia de despompresión de huffman para descomprimir archivos de texto
# veré como implementarla para archivos de audio y tienes que instalar los pip que te dejé erriba, ya que he utilizado
# otras librerías especiales para abrir videos, fotos y audio


# Funciones
class Hman:
    def __init__(self, root):
        self.Huffman = HuffmanCoding()
        self.root = root

    # Seleccion, Archivos
    def SeleccionarArchivoTexto(self):
        # Abre un cuadro de diálogo para que el usuario seleccione un archivo
        archivo = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt;*huff"),
                ("Todos los archivos", "*.*"),
            ],
        )

        # Verifica si el usuario ha seleccionado un archivo
        if archivo:
            with open(archivo, "rb") as file:
                text = file.read()
                print(text)

            messagebox.showinfo(
                "Archivo de texto",
                message="El archivo de texto fue seleccionado conrrectamente ",
            )
            self.Huffman.set_original_text(text)

    # GMR implementé las funciones para abrir como texto archivos de audio y archivos de imagen y video
    #####################################################################
    # Seleccion Audio
    def SeleccionarArchivoAudio():
        audio = filedialog.askopenfilename(
            defaultextension=".mp3",
            filetypes=[
                ("Archivos de audio", "*.mp3;*.wav"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if audio:
            huffman_coder = HuffmanCoding()
            with wave.open(audio, "rb") as audio_file:
                audio_data = audio_file.getparams()
                frames = audio_file.readframes(audio_data.nframes)
                samplw_width = audio_file.getsampwidth()
                framerate = audio_file.getframerate()
                channels = audio_file.getnchannels()

            messagebox.showinfo(
                "Archivo de audio",
                message="El archivo de audio fue seleccionado conrrectamente ",
            )

            huffman_coder.set_original_text(frames)

    def SeleccionarArchivoImage():
        image = filedialog.askopenfilename(
            defaultextension=".png",
            filetypes=[
                ("Archivos de imagen", "*.png*"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if image:
            huffman_coder = HuffmanCoding()
            image_data = cv2.imread(image)
            data = np.array(image_data)

            messagebox.showinfo(
                "Archivo de imagen",
                message="El archivo de imagen fue seleccionado conrrectamente ",
            )

            huffman_coder.set_original_text(data)

    def SeleccionarArchivoVideo():
        video = filedialog.askopenfilename(
            defaultextension=".mp4",
            filetypes=[
                ("Archivos de video", "*.mp4"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if video:
            huffman_coder = HuffmanCoding()
            cap = cv2.VideoCapture(video)
            if not cap.isOpened():
                print("Error al abrir el archivo de video.")
                return
            else:
                messagebox.showinfo(
                    "Archivo de video",
                    message="El archivo de video fue seleccionado conrrectamente ",
                )

            frames = []
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frames.append(gray_frame)

            video_data = np.array(frames)
            huffman_coder.set_original_text(video_data)

    #########################################################################

    # Compresor de archivos

    def Comprimir(self):
        # Verifica si hay texto original seleccionado
        if not self.Huffman.original_text:
            messagebox.showwarning(
                "Advertencia", "No hay archivo seleccionado, por favor ingrese uno."
            )
            return

        # Calcula la tabla de frecuencias y crea el arbol de Huffman
        self.Huffman.calculate_frequency_table()
        self.Huffman.create_huffman_tree()
        self.Huffman.calculate_table_conversion()

        # Obtien el texto comprimido en forma de cadena binaria
        BitsComprimidos = self.Huffman.get_compressed_text()

        # Obtiene el resultado en formato bitarray
        Resultado = self.Huffman.BinarioBitarray()

        # Abre un cuadro de dialogo para argumentar el archivo comprimido
        ArchivoComprimido = filedialog.asksaveasfilename(
            defaultextension=".huff", filetypes=[("Archivos comprimidos", "*.huff")]
        )
        if ArchivoComprimido:
            # Guarda el resultado en el arcchivo comprimido
            with open(ArchivoComprimido, "wb") as Compressed_file:
                Resultado.tofile(Compressed_file)

            # Calcula el tamaño original y el tamaño comprimido
            original_size = len(self.Huffman.original_text)
            TamanioComprimido = len(BitsComprimidos.encode("utf-8"))
            Ratio = (
                1 - original_size / TamanioComprimido
            ) * 100  # Calcula el ratio de compresion

            # Muestra un resumen con la información
            messagebox.showinfo(
                "Resumen",
                f"Tamaño original: {original_size} bits\n Tamaño comprimido: {TamanioComprimido} bits\n Ratio de compresión: {Ratio}",
            )

    ############################################################################
    # intento de descompresor de archivos
    # GMR

    # Descompresor de archivos
    def DescomprimirArchivo(self):
        archivo = filedialog.askopenfilename(
            defaultextension=".huff",
            filetypes=[
                ("Archivos de texto", "*.huff*"),
                ("Todos los archivos", "*.*"),
            ],
        )
        if archivo == "" or archivo is None:
            messagebox.showerror(
                "Error", "No se ha elegido ningun archivo a descomprimir"
            )
            return
        try:
            with open(archivo, "rb") as f:
                bits = BitArray(f.read())

        except Exception as e:
            print(e)
            messagebox.showerror("Error", "El archivo no es valido")
            return
        # Crea una instancia del Huffman
        self.Descompressor = self.Huffman.descomprimir(bits)
        # Obtiene el resultado en formato string

        # Mostrará el resultado en un cuadro de diálogo
        messagebox.showinfo(
            "Resultados",
            "Se han descomprimido {} bytes".format(len(self.Descompressor)),
        )
        # Guardar el resultado en un archivo
        ArchivoDescomprimido = filedialog.asksaveasfilename(
            initialdir=".",
            title=archivo,
            filetype=(("Text files", ".txt"),),
            defaultextension=".txt",
        )
        if not ArchivoDescomprimido:
            return
        else:
            with open(ArchivoDescomprimido, "wb") as f:
                f.write(bytes(self.Des, encoding="utf-8"))

    ######################################################################################################

    # Otros comandos
    def Ayuda(self):
        messagebox.showinfo(
            "¿Cómo usar el programa?",
            message="Hola profesor Manuel. El programa funciona de la sigiente manera:\nUsted debe de darle click en cualquier opción de la barra para poder abrir cualquier tipo de archivo.\nUna vez hecho eso da clik en el botón comprimir y guarda el archivo.\nEl mismo proceso para descomprimir. ",
        )


# Características de la ventana
root = Tk()
root.title("Proyecto de Estructuras de Datos")
root.iconbitmap(
    "C:/Users/angel/OneDrive/Documentos/Universidad/Segundo año de universidad/Tercer Semestre/Estructuras de datos II/Parcial 3/ProyectoEstructurasDatosIICompresorArchivos/LogoUP.ico"
)
root.geometry("800x500")
root.resizable(0, 0)
MenuBar = Menu(root)
canvas = Canvas(root, width=800, height=500)
canvas.place(x=180, y=0)
root.config(menu=MenuBar, bg="brown")
app = Hman(root)


# Este es el titulo de la pagina
Titulo = Label(root, text="COMPRESOR DE ARCHIVOS", font=("arial 20"), fg="black")
Titulo.place(x=250, y=0)

Presentacion = Label(
    root,
    text="-- Integrantes -- \n ID: 0258859 \n Ángel Alberto Bolaños Dávila.\n ID: \n Gerardo Macias Romo. \n -- Materia -- \n Estructura de Datos II \n -- Profesor -- \n Manuel Alejandro Rodríguez Rivera",
    bg="brown",
    font=("times 8"),
)
Presentacion.place(x=0, y=120)

Ayuda = Label(
    root,
    text="Para saber como funciona el programa.\n Da CLICK \n En  el botón de ayuda de la barra superior :)",
    bg="brown",
    font=("times 7"),
)
Ayuda.place(x=0, y=400)


Imagen = Image.open(
    "C:/Users/angel/OneDrive/Documentos/Universidad/Segundo año de universidad/Tercer Semestre/Estructuras de datos II/Parcial 3/ProyectoEstructurasDatosIICompresorArchivos/images.png"
)
Ancho = 100
Alto = 80
ImagenNueva = Imagen.resize((Ancho, Alto))
ImagenSalida = ImageTk.PhotoImage(ImagenNueva)


Picture = Label(root, image=ImagenSalida)
Picture.place(x=40, y=20)
# Aqui mostramos el archivo de texto, imagen y audio

# Archivo de texto
EtiquetaArchivoTexto = Label(
    root, text=" Archivo de texto ", font=("arial 12"), fg="Black"
)
EtiquetaArchivoTexto.place(x=380, y=50)


# Imagen
EtiquetaImagen = Label(
    root,
    text="Comprimir Imagen ",
    font=("arial 12"),
    fg="black",
)
EtiquetaImagen.place(x=380, y=150)
# Audio

EtiquetaAudio = Label(root, text=" Comprimir Audio ", font=("arial 12"), fg="Black")
EtiquetaAudio.place(x=380, y=250)


# Todo lo de la barra
ArchivoMenu = Menu(MenuBar, tearoff=0)
ArchivoMenu.add_command(
    label="Abrir Archivo de Texto", command=app.SeleccionarArchivoTexto
)
ArchivoMenu.add_command(label="Cerrar")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label="Salir", command=root.quit)

ImagenMenu = Menu(MenuBar, tearoff=0)
ImagenMenu.add_command(
    label="Abrir Imagen",
)
# Faltan las opiones de vieo
# Se tienen que crear otras funciones especiales para descomprimir archivos de video, audio e imagen
AyudaMenu = Menu(MenuBar, tearoff=0)
AyudaMenu.add_command(label="Ayuda", command=app.Ayuda)
AyudaMenu.add_separator()

AudioMenu = Menu(MenuBar, tearoff=0)
AudioMenu.add_command(
    label="Abrir Audio",
)

MenuBar.add_cascade(label="Archivo", menu=ArchivoMenu)
MenuBar.add_cascade(label="Imagen", menu=ImagenMenu)
MenuBar.add_cascade(label="Audio", menu=AudioMenu)
MenuBar.add_cascade(label="Ayuda", menu=AyudaMenu)

# Botones para comprimir y descomprimir los archivos

btnCompresioArchivosTexto = Button(
    root, text="Comprimir Archivo", bd=5, font=("arial 10"), command=app.Comprimir
)
btnCompresioArchivosTexto.place(x=200, y=90)

btnDescomprimirArchivosTexto = Button(
    root,
    text="Descomprimir Archivo",
    bd=5,
    font=("arial 10"),
    command=app.DescomprimirArchivo,
)
btnDescomprimirArchivosTexto.place(x=550, y=90)

btnCompresioImagen = Button(
    root, text="Comprimir Imagen", bd=5, font=("arial 10"), command=app.Comprimir
)
btnCompresioImagen.place(x=200, y=200)

btnDescomprimirImagen = Button(
    root,
    text="Descomprimir Imagen",
    bd=5,
    font=("arial 10"),
    command=app.DescomprimirArchivo,
)
btnDescomprimirImagen.place(x=550, y=200)


btnCompresioAudio = Button(
    root, text="Comprimir Audio", bd=5, font=("arial 10"), command=app.Comprimir
)
btnCompresioAudio.place(x=200, y=300)

btnDescomprimirAudio = Button(
    root,
    text="Descomprimir Audio",
    bd=5,
    font=("arial 10"),
    command=app.DescomprimirArchivo,
)
btnDescomprimirAudio.place(x=550, y=300)


root.mainloop()
