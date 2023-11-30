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
        self.original_text = ""         # Texto original a comprimir
        self.freq_table = {}            # Tabla de frecuencias de los caracteres
        self.heap = []                  # Lista utilizada como heap
        self.huffman_tree = None        # Árbol de Huffman
        self.table_conversion = {}      # Tabla de conversión de caracteres

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
        elements = [HuffmanNode(key=freq, value=letter) for letter, freq in self.freq_table.items()]
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
        Rsult = int (Resultado, 2).to_bytes((len(Resultado) + 7 ) //8, 'big')
        ResultadoBitArray.frombytes(Rsult)
        return ResultadoBitArray
    
    def descomprimir(self, compressed_text):
        actual = self.huffman_tree
        TextoDescomprimido = ""
        
        for bit in compressed_text:
            if bit == "0":
                actual = actual.left_child
            elif bit == "1":
                actual = actual.right_child
            
            if actual.value is not None:
                TextoDescomprimido += actual.value
                actual = self.huffman_tree
                
        return TextoDescomprimido