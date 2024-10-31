saldo = 1000000

def tampilkan_menu():
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Tunai💵")
    print("2. Keluar🔙")

while True:
    tampilkan_menu()

    pilihan = input("Plih menu (1/2): ")

    if pilihan == '1':
        try:
            jumlah = int(input("Masukkan jumlah penarikan: "))

            if jumlah > saldo:
                print("Saldo tidak cukup!💢")
            elif jumlah <= 0:
                print("Jumlah penarikan tidak valid!💢")
            else:
                saldo -= jumlah
                print("Penarikan berhasil!✅")
        except ValueError:
            print("Input tidak valid! masukkan angka.")

    elif pilihan == '2':
        print("Terima kasih telah menggunakan ATM!😇")
        break

    else:
        print("Pilihan tidak valid! silahkan coba lagi.")
