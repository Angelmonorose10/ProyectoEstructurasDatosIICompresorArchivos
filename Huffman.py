import heapq
from bitarray import bitarray


# Definición de la clase para los nodos del árbol de Huffman
class HuffmanNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        return self.key < other.key


# Definición de la clase principal para la codificación de Huffman
class HuffmanCoding:
    def __init__(self):
        # Inicialización de variables
        self.original_text = ""  # Texto original a comprimir
        self.freq_table = {}  # Tabla de frecuencias de los caracteres
        self.heap = []  # Lista utilizada como heap
        self.huffman_tree = None  # Árbol de Huffman
        self.table_conversion = {}  # Tabla de conversión de caracteres

    def set_original_text(self, text):
        # Método para establecer el texto original
        self.original_text = text

    def calculate_frequency_table(self):
        # Método para calcular la tabla de frecuencias
        self.freq_table = {}
        for c in self.original_text:
            if c in self.freq_table:
                self.freq_table[c] += 1
            else:
                self.freq_table[c] = 1

    def create_huffman_tree(self):
        # Método para crear el árbol de Huffman
        elements = [
            HuffmanNode(key=freq, value=letter)
            for letter, freq in self.freq_table.items()
        ]
        
        if not elements:
            return
        
        heapq.heapify(elements)

        # Proceso para armar el árbol de Huffman
        while len(elements) > 1:
            left_child = heapq.heappop(elements)
            right_child = heapq.heappop(elements)

            new_node = HuffmanNode(key=left_child.key + right_child.key)
            new_node.left_child = left_child
            new_node.right_child = right_child

            heapq.heappush(elements, new_node)

        self.huffman_tree = elements[0]

    def calculate_table_conversion(self):
        # Método para calcular la tabla de conversión de caracteres
        self.table_conversion = {}
        self._dfs(self.huffman_tree, "")

    def _dfs(self, curr_node, curr_code):
        # Método auxiliar para realizar un recorrido en profundidad en el árbol
        if curr_node.value is not None:
            self.table_conversion[curr_node.value] = curr_code
        if curr_node.left_child is not None:
            self._dfs(curr_node.left_child, curr_code + "0")
        if curr_node.right_child is not None:
            self._dfs(curr_node.right_child, curr_code + "1")

    def get_compressed_text(self):
        # Método para obtener el texto comprimido
        compressed_text = ""
        for char in self.original_text:
            compressed_text += self.table_conversion[char]
        return compressed_text

    def BinarioBitarray(self):
        Resultado = self.get_compressed_text()
        ResultadoBitArray = bitarray()
        Rsult = int(Resultado, 2).to_bytes((len(Resultado) + 7) // 8, "big")
        ResultadoBitArray.frombytes(Rsult)
        return ResultadoBitArray

    def descomprimir(self, compressed_text):
        if not compressed_text:
            return ""
        
        actual = self.huffman_tree
        TextoDescomprimido = ""

        for bit in compressed_text:
            if bit == "0":
                if actual and actual.left_child:
                    actual = actual.left_child
            elif bit == "1":
                if actual and actual.right_child:
                        actual = actual.right_child
          
                if actual and actual.value is not None:
                    TextoDescomprimido += actual.value
                    actual = self.huffman_tree
                    
        return TextoDescomprimido
                
      
    

          

    # GMR 23:20
    ###################################################################################
    # Esta función desencripta el árbol de huffman oculto en un archivo
    # Pero para eso tenemos que antes encriptarlo por lo que al inicio de un archivo .huff
    # primero se va aguardar la tabla de frecuencias de la forma frequencia seguida de la
    # letra a la que pertenece

    # Ocurre un error cuándo los siguientes dígitos después de la ecriptación son dígitos
    # y no letras, para eso no sé que hacer pero ya pensaré en algo
    # Actualización, ya está solucionado
    def get_compressed_huffman_tree(self, compressed_text):
        resultado = {}
        digitos_temporales = []
        eliminados = []
        eliminados_parciales = []
        for character in compressed_text:
            if character.isdigit():
                digitos_temporales.append(character)
                eliminados_parciales.append(character)
            elif character.isalpha():
                letra = character
                if letra in resultado:
                    compressed_text = compressed_text[
                        len(eliminados) - len(eliminados_parciales) :
                    ]
                    eliminados = []
                    digitos_temporales = []
                    return resultado, compressed_text

                if digitos_temporales:
                    resultado[letra] = int("".join(digitos_temporales))
                    digitos_temporales = []
                eliminados_parciales = []
            eliminados.append(character)

        return

    # Después de que quitamos la tabla de frecuencias que estaba encriptada, entonces lo que resta
    # es el texto que está comprimido en caractéres ASCII, así que lo pasamos a bianrio con la siguiente
    # función

    def al_binario(self, input):
        with open(input, "r") as file:
            text = file.read()

        texto_binario = "".join(format(ord(char), "08b") for char in text)

        return texto_binario

    # Una vez hecho este proceso, nos queda solo el texto en binario crudo, por lo que para comenzar a
    # descomprimir el archivo primero debemos de crear el árbol de huffam con la tabla de frecuencias que
    # acabamos de desencriptar y ahora si podemos usar

    # La siguiente función nos va a ser deayda para asignar como frequency table los resultados que obtuvimos
    # en la desencriptación inicial, básicamente nos sirve para asignarla como variable global y poder trabajar
    # con esa tabla de frecuencia directamente con la función de create_huffman_tree()

    def frequency_table_descompression(self, resultados):
        self.freq_table = resultados

    # la siguiente función nos permite guardar el diccionario al inicio del archivo esta función nos va a ser
    # de utilidad al momento de encriptar el diccionario en el archivo

    def guardar_diccionario(self, diccionario, archivo):
        with open(archivo, "w") as fichero:
            for letra, valor in diccionario.items():
                fichero.write(f"{valor}{letra}")

    # la funcion de abajo nos permite abrir el archivo para descomprimirlo

    def abrir_para_descomprimir(self, archivo):
        mi_archivo_abierto = ""
        with open(archivo, "rb") as fichero:
            mi_archivo_abierto = fichero
        return mi_archivo_abierto

    # Ahora que tenemos estas funciones, la secuencia para desencriptar sería
    # Paso 1: paso_1 = self.Huffman.abrir_para_descomprimir("archivo.huff")
    # paso 2 y 3: paso_2, paso_3 = get_compressed_huffman_tree(paso_1)
    # paso 4: frequency_table_descompression(paso_2)
    # paso 5: paso_5 = al_binario(paso_3)
    # paso 6: crate_huffman_tree()
    # paso 7: paso_7 = descomprimir(paso_5)

    # Ahora solo nos falta meter el resultado del paso 7 en un archivo de texto

    # Para eso creamos una función en la que dado un texto y un archivo, se escriba
    # el texto en el archivo, para eso ya debemos sabe cuál es nuestro archivo al
    # que le vamos a escribir el texto descomprimido

    def meter_a_archivo(self, texto, archivo):
        with open(archivo, "w+") as fichero:
            fichero.write(str(texto))

    # paso 8: meter_a_archivo(paso_7,"archivo.txt")


##########################################################################