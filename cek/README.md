# cek.py

CLI kecil berbasis tree-sitter untuk memeriksa file Python dalam sebuah folder:

1. Komentar berisi `TODO` atau `FIXME`
2. Fungsi yang lebih dari 30 baris
3. File yang mengandung error sintaks

## Memasang dependensi

```bash
python -m pip install tree-sitter tree-sitter-python
```

## Menjalankan

```bash
python cek.py <folder>
```

Contoh: `python cek.py uji`

## Contoh output

```
uji/rusak.py:1: ada error sintaks
uji/panjang.py:1: fungsi panjang terlalu panjang (32 baris)
uji/todo.py:1: # TODO: tambahkan validasi input
uji/todo.py:3: # FIXME: nama masih di-hardcode
```

## Catatan

- Jumlah baris fungsi dihitung dari baris `def` sampai baris terakhir fungsi.
- Semua fungsi dihitung, termasuk method di dalam kelas dan fungsi bersarang.
- TODO/FIXME hanya dicari di komentar, bukan di dalam string.
- Folder `venv`, `.venv`, `.git`, `node_modules`, dan `__pycache__` dilewati.

## Uji pada repositori nyata

Repo: https://github.com/josharsh/100LinesOfCode

| Temuan | Jumlah |
|---|---|
| Fungsi lebih dari 30 baris | 25 |
| File dengan error sintaks | 2 |
| Komentar TODO/FIXME | 0 |

Cek manual (file dipilih karena memiliki temuan):

| File | Hitungan manual | Output cek.py | Cocok |
|---|---|---|---|
| CaesarCipher/CaesarCipher.py | caesar_encrypt: 32 baris | 32 baris | Ya |
| Wikipedia-Summary-CLI/Wiki_summary.py | search_and_summarize: 35, main: 35 | 35, 35 | Ya |