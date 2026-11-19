import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

kode = b"""
def tambah(a, b):
    return a + b

tambah(1, 2)

if nilai >= 80:
    print("Lulus")
else:
    print("Tidak Lulus")

class Mahasiswa:
    def salam(self):
        print("Halo, saya seorang mahasiswa.")

"""
tree = parser.parse(kode)
print(tree.root_node)