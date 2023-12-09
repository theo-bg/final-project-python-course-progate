import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    
    id = int(input("Masukkan PIN anda: "))
    trial = 0

    while (id != int (atm.checkPin()) and trial < 3):
        id = int(input("PIN anda salah. Silakan masukkan lagi: "))
        trial +=1

        if trial == 3:
            print ("Error. Silakan ambil kartu dan coba lagi..")
            exit()
    
    while True:
        print("\nSelamat datang di ATM Bubadibako..")
        print("\n1 - Cek Saldo \t 2 - Tarik Tunai \t 3 - Setor Tunai \t 4 - Ganti PIN \t 5 - Keluar")
        selectmenu = int(input("\nSilakan pilih menu: "))

        if selectmenu == 1:
            print("Saldo anda sekarang: Rp " + str(atm.checkBalance()) + "")

        elif selectmenu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input ("Konfirmasi: Anda akan melakukan tarik tunai dengan nominal Rp " + str(nominal) + "? (y/n) ")

            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp " + str(atm.checkBalance()) + "")
            else:
                break
            if nominal <= atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi tarik tunai berhasil!")
                print("Saldo anda sekarang adalah: Rp " + str(atm.checkBalance()) + "")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan tarik tunai!")
                print("Silakan lakukan penambahan nominal saldo")

        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan setor tunai dengan nominal Rp " + str(nominal) + "? (y/n) ")

            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print ("Saldo anda sekarang adalah: Rp " + str(atm.checkBalance()) + "\n")
            else:
                break

        elif selectmenu == 4:
            verify_pin = int(input("Masukkan PIN anda: "))

            while verify_pin != int(atm.checkPin()):
                verify_pin = int(input("PIN anda salah. Silakan masukkan PIN: "))

            updated_pin = int(input("Silakan masukkan PIN baru: "))
            print("PIN anda berhasil diganti!")

            verify_newpin = int(input("Coba masukkan PIN baru: "))
            
            if verify_newpin == updated_pin:
                print("PIN baru anda sukses")
            else:
                print("Maaf, PIN anda salah!")

        elif selectmenu == 5:
            print("Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini sebagai bukti transaksi anda.")
            print("No. Record: ", random.randint(100000,1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Bubadibako!")
            exit()

        else:
            print("Error. Maaf, menu tidak tersedia")
        