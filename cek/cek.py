import sys
from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNGSI = Query(PY, "(function_definition name: (identifier) @nama) @fungsi")
BATAS = 30
ABAIKAN = {"venv", ".venv", ".git", "node_modules", "__pycache__"}


def cari_error(node):
    """Cari node pertama yang is_error atau is_missing (rekursif)."""
    if node.is_error or node.is_missing:
        return node
    for child in node.children:
        hasil = cari_error(child)
        if hasil is not None:
            return hasil
    return None


def cek_file(path):
    tree = parser.parse(path.read_bytes())

    # Fitur 1: komentar TODO/FIXME
    for node in QueryCursor(Q_TODO).captures(tree.root_node).get("c", []):
        teks = node.text.decode(errors="replace").strip()
        print(f"{path}:{node.start_point[0] + 1}: {teks}")

    # Fitur 2: fungsi lebih dari 30 baris
    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        fungsi = cap["fungsi"][0]
        nama = cap["nama"][0].text.decode(errors="replace")
        jumlah = fungsi.end_point[0] - fungsi.start_point[0] + 1
        if jumlah > BATAS:
            print(f"{path}:{fungsi.start_point[0] + 1}: "
                  f"fungsi {nama} terlalu panjang ({jumlah} baris)")

    # Fitur 3: file dengan error sintaks
    if tree.root_node.has_error:
        bermasalah = cari_error(tree.root_node)
        baris = bermasalah.start_point[0] + 1 if bermasalah else 1
        print(f"{path}:{baris}: ada error sintaks")


for path in Path(sys.argv[1]).rglob("*.py"):
    if ABAIKAN & set(path.parts):
        continue
    cek_file(path)