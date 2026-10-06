# Minpro-2-DDP-SistemSeleksiBeasiswaMahasiswa 

# 1. Deskripsi Singkat Program
Program Sistem Seleksi Beasiswa ini menggunakan Python untuk mengelola data mahasiswa berdasarkan nilai IPK. Program memiliki dua role, yaitu admin dan user. Admin dapat melakukan tambah, lihat, ubah, dan hapus data, sedangkan user hanya dapat melihat hasil seleksi.

Data mahasiswa disimpan menggunakan dictionary dan ditampilkan dalam bentuk tabel. Status seleksi ditentukan berdasarkan IPK, yaitu IPK ≥ 3,25 dinyatakan Diterima, sedangkan IPK di bawah 3,25 dinyatakan Tidak Diterima.
# 2. Flowchart

<img width="2092" height="1323" alt="FlowchartZacky2 drawio" src="https://github.com/user-attachments/assets/1a221c2b-c500-4ca7-8496-a4c22c19a40e" />


# 3. Program

# Dictionary Akun
<img width="323" height="67" alt="Screenshot 2026-10-06 145029" src="https://github.com/user-attachments/assets/ccbc7946-5b3f-4c64-8dff-66712896b28e" />

Dictionary akun yang digunakan untuk menyimpan data akun pengguna. Setiap akun memiliki username, password, dan role. Program memiliki dua role, yaitu admin dan user.

# Dictionary Data
<img width="91" height="29" alt="Screenshot 2026-10-06 145036" src="https://github.com/user-attachments/assets/bd6c2fe8-8955-4ce6-a0ff-20794cbf7db7" />

Dictionary data digunakan sebagai tempat untuk menyimpan data mahasiswa yang dimasukkan ke dalam program. Data tersebut nantinya berisi nama mahasiswa dan nilai IPK.

# Function Login
<img width="309" height="139" alt="Screenshot 2026-10-06 145111" src="https://github.com/user-attachments/assets/b304f6f9-b239-40a4-8c5f-8a1dd6b7ff76" />

"login()" digunakan untuk melakukan proses login pengguna. Program meminta username dan password, kemudian mencocokkannya dengan data yang terdapat pada dictionary akun. Jika username dan password benar, program akan masuk ke menu. Jika salah, program akan menampilkan pesan bahwa username atau password salah.

# Function Input IPK
<img width="215" height="125" alt="Screenshot 2026-10-06 145124" src="https://github.com/user-attachments/assets/03c2b932-6eaf-433d-8365-5f3d9a1f57ee" />

"input_ipk()" digunakan untuk menerima nilai IPK dari pengguna sekaligus melakukan validasi. Nilai IPK yang diperbolehkan adalah 0 sampai 4. Jika nilai tidak berada di rentang itu, program akan menampilkan pesan bahwa IPK harus berada pada rentang 0,0–4,0 dan mengembalikan nilai -1 sebagai tanda bahwa input IPK tidak valid.

# Function Tambah
<img width="256" height="236" alt="Screenshot 2026-10-06 150701" src="https://github.com/user-attachments/assets/303fe42c-fe7d-409a-b527-9b0186321f8b" />

"tambah()" digunakan untuk menambahkan data mahasiswa. Program terlebih dahulu meminta nama mahasiswa dan memeriksa apakah nama tersebut kosong atau sudah terdaftar. Setelah nama valid, program meminta IPK menggunakan "input_ipk()". Jika IPK valid, data mahasiswa disimpan ke dalam dictionary data.

# Function Lihat
<img width="288" height="212" alt="Screenshot 2026-10-06 150718" src="https://github.com/user-attachments/assets/45f6e079-5699-4664-aee1-32fc60d2bf71" />

"lihat()" digunakan untuk menampilkan seluruh data mahasiswa dalam bentuk tabel. Program mengambil nama dan IPK dari dictionary data, kemudian menentukan status seleksi berdasarkan nilai IPK.

# Function Ubah
<img width="254" height="340" alt="Screenshot 2026-10-06 150728" src="https://github.com/user-attachments/assets/dfbea3fe-1004-4812-b96c-3294cb9d49e6" />

"ubah()" digunakan untuk mengubah data mahasiswa. Pertama, program memeriksa apakah nama yang ingin diubah terdapat dalam dictionary. Jika ditemukan, pengguna dapat memasukkan nama baru dan IPK baru. Setelah data baru dimasukkan, data lama dihapus menggunakan del, kemudian digantikan dengan data yang baru.

# Function Hapus
<img width="234" height="126" alt="Screenshot 2026-10-06 150743" src="https://github.com/user-attachments/assets/8067ea4a-2f51-4dbd-a9ad-5dc0a4eff463" />

"hapus()" digunakan untuk menghapus data mahasiswa. Program terlebih dahulu memeriksa apakah nama mahasiswa terdapat dalam dictionary.

# Looping
<img width="279" height="49" alt="Screenshot 2026-10-06 151627" src="https://github.com/user-attachments/assets/dd61532a-e2b5-4759-9231-c52ee73b3027" />

"While True" digunakan agar program dapat berjalan terus selama pengguna belum memilih untuk keluar.

# Menu Admin
<img width="276" height="338" alt="Screenshot 2026-10-06 151801" src="https://github.com/user-attachments/assets/02240196-b8cc-41a4-82d8-0dc7240ae202" />

Bagian ini dijalankan apabila pengguna berhasil login sebagai admin. Admin memiliki akses penuh untuk mengelola data mahasiswa(CRUD).

# Menu User
<img width="268" height="209" alt="Screenshot 2026-10-06 151840" src="https://github.com/user-attachments/assets/db7918ae-6c9d-4db6-9a31-71bc34f0d0b8" />

Bagian ini dijalankan jika pengguna login sebagai user. User hanya diberikan akses untuk melihat hasil seleksi.

# Logout
<img width="269" height="80" alt="Screenshot 2026-10-06 151855" src="https://github.com/user-attachments/assets/10b01bb0-ba07-47c9-a435-d8565e33c124" />

Setelah pengguna melakukan logout, program menanyakan apakah ingin login kembali. "lower()" digunakan untuk mengubah input menjadi huruf kecil.

# 4. Output

# Admin
<img width="176" height="330" alt="Screenshot 2026-10-06 154941" src="https://github.com/user-attachments/assets/6261c9a6-3d1b-437e-97b6-681730d945b0" />

<img width="158" height="287" alt="Screenshot 2026-10-06 155017" src="https://github.com/user-attachments/assets/11a2eb22-50d3-439f-aa62-691aa8ee6bc8" />

# User
<img width="242" height="286" alt="Screenshot 2026-10-06 155035" src="https://github.com/user-attachments/assets/5663d46e-d96d-4e3f-9a18-3873d21c0588" />


# 5. Nilai Tambah

# Library
<img width="209" height="49" alt="Screenshot 2026-10-06 153947" src="https://github.com/user-attachments/assets/72bea9f7-7a96-4ed0-ae96-a58580e37a96" />

"pwinput" digunakan untuk menyembunyikan password ketika pengguna melakukan login. "PrettyTable" digunakan untuk menampilkan data mahasiswa dalam bentuk tabel agar lebih rapi. Sedangkan "os" digunakan untuk menjalankan perintah pada sistem operasi.
