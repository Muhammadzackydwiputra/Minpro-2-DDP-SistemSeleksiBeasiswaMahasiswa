import pwinput
from prettytable import PrettyTable
import os

os.system("cls" if os.name == "nt" else "clear")

akun = {
    "admin": {"password": "admin059", "role": "admin"},
    "user": {"password": "user059", "role": "user"}
}

data = {}

def login():
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    if username in akun:
        if password == akun[username]["password"]:
            return akun[username]["role"]

    return

def input_ipk():
    ipk = float(input("IPK: "))

    if 0 <= ipk <= 4:
        return ipk

    print("IPK harus 0.0 - 4.0")
    return -1

def tambah():
    nama = input("Nama: ")

    if nama == "":
        print("Nama tidak boleh kosong")
        return

    if nama in data:
        print("Nama sudah terdaftar")
        return

    ipk = input_ipk()

    if ipk >= 0:
        data[nama] = {"ipk": ipk}
        print("Data berhasil ditambahkan")

def lihat():
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "IPK", "Status"]

    for nama in data:
        ipk = data[nama]["ipk"]

        if ipk >= 3.25:
            status = "Diterima"
        else:
            status = "Tidak Diterima"

        tabel.add_row([nama, ipk, status])

    print(tabel)

def ubah():
    nama = input("Nama yang diubah: ")

    if nama not in data:
        print("Data tidak ditemukan")
        return

    nama_baru = input("Nama baru: ")

    if nama_baru == "":
        print("Nama tidak boleh kosong")
        return

    if nama_baru in data:
        print("Nama sudah terdaftar")
        return

    ipk = input_ipk()

    if ipk >= 0:
        data[nama_baru] = {"ipk": ipk}
        del data[nama]
        print("Data berhasil diubah")

def hapus():
    nama = input("Nama yang dihapus: ")

    if nama in data:
        del data[nama]
        print("Data berhasil dihapus")
    else:
        print("Data tidak ditemukan")
    
while True:
    print("\n=== Sistem Seleksi Beasiswa ===")
    role = login()

    if role == "admin":
        while True:
            print("\n=== Menu Admin ===")
            print("1. Tambah")
            print("2. Lihat")
            print("3. Ubah")
            print("4. Hapus")
            print("5. Logout")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                tambah()
            elif pilihan == "2":
                lihat()
            elif pilihan == "3":
                ubah()
            elif pilihan == "4":
                hapus()
            elif pilihan == "5":
                break
            else:
                print("Menu tidak tersedia.")

    elif role == "user":
        while True:
            print("\n=== Menu User ===")
            print("1. Lihat Hasil")
            print("2. Logout")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                lihat()
            elif pilihan == "2":
                break
            else:
                print("Menu tidak tersedia.")

    else:
        print("Username atau password salah")

    ulang = input("Login lagi? (ya/tidak): ")

    if ulang.lower() == "tidak":
        print("Program selesai")
        break