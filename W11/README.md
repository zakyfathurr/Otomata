- Penjelasan mengenai CYK algorithm dan cara kerjanya
1. load_grammar(json_path)
    Membaca file JSON berisi grammar, lalu membalik produksinya agar bisa dicari dari kanan ke kiri (untuk kebutuhan algoritma CYK).

2. cyk_parse(grammar, input_string)
    Menerapkan algoritma CYK:
    - Memecah input (dengan spasi) menjadi token.
    - Mengisi tabel segitiga CYK dari bawah ke atas berdasarkan aturan grammar.
    - Mengecek apakah simbol S ada di posisi [0][n-1] (artinya string diterima grammar).

3. display_table(table, tokens)
    Menampilkan isi tabel CYK ke terminal agar bisa dilihat proses parsing-nya.

4. main()
    - Memuat grammar dari grammar.json.
    - Menerima input string dari pengguna.
    - Menjalankan CYK dan menampilkan apakah string diterima, serta menampilkan tabelnya.
    - Berulang hingga pengguna mengetik exit

- Cara menggunakan program kalian
    masukkan input string yang memiliki spasi diantaranya

- Sample input dan Sample output
![image](https://github.com/user-attachments/assets/eacf3e90-cf80-4466-831e-3d1aff616046)
