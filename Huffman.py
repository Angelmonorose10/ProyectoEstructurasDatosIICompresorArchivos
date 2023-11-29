import heapq
from bitarray import bitarray
class HuffmanNode(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

class HuffmanCoding:
    def __init__(self):     
        self.original_text = ""
        self.freq_table = {} # Usar una lista como heap
        self.huffman_tree = None
        self.table_conversion = {}

    def set_original_text(self, text):
        self.original_text = text

    def calculate_frequency_table(self): 
        self.freq_table = {}
        for c in self.original_text:
            if c in self.freq_table:
                self.freq_table[c] += 1
        else:
            self.freq_table[c] = 1 

    def create_huffman_tree(self):
        elements = [HuffmanNode(key = freq, value = letter) for letter, freq in self.freq_table.items()]
        self.heaify(elements)
        # Proceso para armar el árbol de Huffman
        while len(elements) > 1:
            left_child = heapq.heappop(elements)
            right_child = heapq.heappop(elements)

            new_node = HuffmanNode(key = left_child.key + right_child.key)
            new_node.left_child = left_child
            new_node.right_child = right_child

            heapq.heappush(elements, new_node)

        self.huffman_tree = elements[0]
        
    def calculate_table_conversion(self):
        self.table_conversion = {}
        self._dfs(self.huffman_tree)

    def _dfs(self, curr_node, curr_code):
        if curr_node.value is not None:
            self.table_conversion[curr_node.value] = curr_code
        if curr_node.left_child is not None:
            self._dfs(curr_node.left_child, curr_code + "0")
        if curr_node.right_child is not None:
            self._dfs(curr_node.right_child, curr_code + "1")

    def get_compressed_text(self):
        compressed_bits = bitarray()
        for char in self.original_text:
            compressed_bits.extend(self.table_conversion[char])

        return compressed_bits
