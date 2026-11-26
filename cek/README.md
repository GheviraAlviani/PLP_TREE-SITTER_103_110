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

### Cara hitung manual

- Panjang fungsi = baris terakhir fungsi - baris `def` + 1.
- TODO/FIXME dicari dengan `Ctrl+F` di VS Code.
- Hasilnya dibandingkan dengan `hasil_repo.txt`.

### Cek manual 2 file acak

File dipilih dengan `find ~/repo-uji -name "*.py" | shuf -n 2`.

| File | Hitungan manual | Output cek.py | Cocok |
|---|---|---|---|
| Hash/hashing.py | calculate_hash: 14-5+1 = 10, print_usage: 19-16+1 = 4, tanpa TODO/error | tidak ada temuan | Ya |
| morse_translator/morse_translator.py | encrypt: 26-19+1 = 8, decrypt: 47-29+1 = 19, tanpa TODO/error | tidak ada temuan | Ya |

### Cek tambahan pada file yang memiliki temuan

| File | Hitungan manual | Output cek.py | Cocok |
|---|---|---|---|
| CaesarCipher/CaesarCipher.py | caesar_encrypt: 40-9+1 = 32 | 32 baris | Ya |
| Wikipedia-Summary-CLI/Wiki_summary.py | search_and_summarize: 57-23+1 = 35, main: 93-59+1 = 35 | 35 dan 35 baris | Ya |