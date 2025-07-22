# CAPSTONE MODUL 1: PYTHON
# KARINA FIDELIA RAMADHANI

# Aplikasi ini bertujuan untuk mempermudah peternak mendata hasil produksi ayamnya

farmList = {
        "1" : {"Nama Kandang" : "A1", "Manager" : "Budhi", "Populasi" : 45000, "Usia" : 25},
        "2" : {"Nama Kandang" : "A2", "Manager" : "Stefan", "Populasi" : 50000, "Usia" : 25},
        "3" : {"Nama Kandang" : "B", "Manager" : "William", "Populasi" : 80000, "Usia" : 16},
        "4" : {"Nama Kandang" : "C", "Manager" : "Ria", "Populasi" : 45000, "Usia" : 10}
    }


def showMainMenu():
    print("""
"Selamat datang di 'Chicky Apps'!🐔"
Silahkan pilih menu
    1. Daftar kandang ayam
    2. Update data kandang      
    3. Tambah data kandang
    4. Hapus data kandang
    5. Penjualan ayam (livebird)
    6. Log Out
""")    


def showFarmList():
    print("Ini daftar kandang kamu:")
    print("No | Nama Kandang | Manager | Populasi | Usia")
    for No, data in farmList.items():
        print(f"{No:<2} | {data["Nama Kandang"]:<12} | {data["Manager"]:<7} | {data["Populasi"]:<8} | {data["Usia"]:<2}")


def showUpdateMenu():
    showFarmList()
    No = input("Masukkan nomor kandang yang ingin kamu update: ")
    if No in farmList:
        print(f"\nData kandang no {No} saat ini: ")
        print(f"1. Nama kandang : {farmList[No]["Nama Kandang"]}")
        print(f"2. Nama Manager Kandang : {farmList[No]["Manager"]}")
        print(f"3. Populasi ayam : {farmList[No]["Populasi"]}")
        print(f"4. Usia ayam: {farmList[No]["Usia"]}")

        choose = input("Masukkan nomor kandang yang ingin kamu ubah datanya: ")
        while True:
            if choose == "1":
                newValue = input("Masukkan nama kandang yang baru: ")
                farmList[No]["Nama Kandang"] = newValue
            elif choose == "2":
                newValue = input("Masukkan nama manager kandang yang baru: ")
                farmList[No]["Manager"] = newValue
            elif choose == "3":
                newValue = int(input("Masukkan jumlah populasi ayam yang baru: "))
                farmList[No]["Populasi"] = newValue
            elif choose == "4":
                newValue = int(input("Masukkan usia ayam yang baru: "))
                farmList[No]["Usia"] = newValue
            else:
                print("\nNomor kandang tidak ditemukan\n")
            break

        print("\n== Data berhasil diperbarui!🐣 ==\n")
        showFarmList()

        while True:
            quest = input("Apakah kamu masih ingin mengupdate data kandang? (y/n): ").lower()
            if quest == "y":
                showUpdateMenu()
                break
            elif quest == "n": 
                break
            else:
                print("\nerror: masukkan y atau n\n")
    else:    
        print("\nNomor kandang tidak ditemukan\n")
        showUpdateMenu()
    

def showAddMenu():
    showFarmList()
    try: 
        num = input("Masukkan nomor kandang: ")
        if num in farmList:
            print("\nAduh, nomornya sudah digunakan.\n")
            showAddMenu()
            return

        farm = input("Masukkan nama kandang: ")
        manager = input("Masukkan nama manager: ")
        population = int(input("Masukkan jumlah populasi: "))
        age = int(input("Masukkan usia ayam: "))

        farmList[num] = {"No": num, "Nama Kandang":farm, "Manager":manager, "Populasi":population, "Usia":age}
        print("== Data berhasil diperbarui!🐣 ==\n") 
        showFarmList()
    
        while True:
            quest = input("\nApakah kamu mau menambahkan data kandang lagi? (y/n): \n").lower()
            if quest == "y":
                showAddMenu()
                break
            elif quest == "n":
                print("\nOke, data kamu berhasil Chicky simpan!\n")
                return
            else:
                print("\nerror: masukkan y atau n\n")
    except ValueError:
        print("Error")
            

def showDeleteMenu():
    showFarmList()
    No = input("Masukkan nomor kandang yang ingin kamu hapus: ")
    if No in farmList:
        del farmList[No]
        showFarmList()
        quest = input("Apakah kamu mau menghapus kandang lain? (y/n): ").lower()
        if quest == "y":
            showDeleteMenu()
        elif quest == "n":
            print("== Data kamu berhasil diperbarui!🐣 ==\n")
        else:
            print("\nerror: masukkan y atau n\n") 
    else:
        print("\nNomor kandang tidak ditemukan\n")
        showDeleteMenu()


def showSellMenu():
    cart = []
    while True:
        showFarmList()
        No = input("Masukkan no kandang: ")
        if No in farmList:
            try:
                amount = int(input("Masukkan jumlah (ekor) ayam yang akan dipanen: "))
                if amount > farmList[No]["Populasi"]:
                    print("Aduh, stok ayam tidak cukup :(\n")
                    continue
                elif amount <= farmList[No]["Populasi"]:
                    kg = float(input("Masukkan berat (kg) ayam yang akan dijual: "))
                    price = int(input("Masukkan harga daging saat ini: "))
                    total = int((amount * kg) * price)

                    farmList[No]["Populasi"] -= amount

                    cart.append({
                    "Kandang": farmList[No]["Nama Kandang"],
                    "Jumlah": amount,
                    "Berat": kg,
                    "Harga": price,
                    "Total": total
                    })
                    
                    print("\n== Transaksi berhasil dicatat ==\n")

                    for i, item in enumerate(cart, start=1): 
                        print(f"{i}.Kandang : {item["Kandang"]}")
                        print(f"Jumlah      : {item["Jumlah"]} ekor")
                        print(f"Berat       : {item["Berat"]} kg")
                        print(f"Harga       : Rp {item["Harga"]:,}")

            except ValueError:
                print("\nMasukkan jumlah yang benar\n")
                continue
        else:
            print("\nNomor kandang tidak ditemukan.\n")
            continue

        quest2 = input("\nApakah kamu mau panen ayam lagi? (y/n): \n").lower()
        if quest2 == "n":
            break

    print("\n==== Ringkasan Penjualan ====\n")
    print("Nama   |   Jumlah   |   Harga   |   Total   ")
    totalSold = 0
    for item in cart: 
        print(f"{item["Kandang"]:<7}|   {item["Jumlah"]}    |   {item["Harga"]}   |   {item["Total"]}")
        totalSold += item["Total"]
    
    print(f"\nTotal penjualan : Rp {totalSold:,}")
    print("*Catatan: Kamu akan dihubungi maks. 1x24 jam oleh bandar yang tertarik dengan penawaran kamu.")
    
           
accounts = {}
accountSaved = None
def showRegisterMenu():
    global accounts
    print("\n===Register Akun===")
    username = input("Masukkan username kamu: ")
    if username in accounts:
        print("Username sudah terdaftar!\n")
    else:
        password = input("Masukkan password kamu: ")
        if len(password) == 6 and password.isdigit():
            accounts[username] = password
            print("Registrasi berhasil!\n")
        else:
            print("Password harus terdiri dari 6 angka!")

def showLoginMenu():
    global accountSaved
    print ("\n===Login====")
    username = input("Masukkan username kamu: ")
    password = input("Masukkan password kamu: ")
    while True: 
        if username in accounts and accounts[username] == password:
            accountSaved = username
            print(f"\nHai, {username}!")
            return True
        else:
            print("Username atau password kamu salah :(")
            break

        
print("""
Hai nama aku Chicky!😎 
Aku asisten yang akan mendata semua ayam broilermu!
      
Kamu bisa memasukkan dan mengedit data-data populasi ayam mu disini!

🐣 Fitur baru:            
    Sekarang kamu juga bisa menjual ayam di menu 'Penjualan Livebird'
    Aplikasi ini sudah terhubung dengan komunitas bandar ayam broiler se-Jawa Barat lho! :D
      
== Aplikasi ini masih dalam tahap pengembangan. Beberapa fitur mungkin belum berfungsi dengan baik. == 
""")

while True:
        quest = input("\nApakah kamu sudah memiliki akun? (y/n) : ").lower()
        if quest == "y":
            if showLoginMenu():
                break
        elif quest == "n":
            print("Waduh, ayo bikin akunmu dulu!")
            showRegisterMenu()
        else:
            print("\nerror: masukkan y atau n\n")
    
while True:
        showMainMenu()
        try:
            noMenu = int(input("Masukkan nomor menu yang ingin kamu jalankan: "))
            if noMenu == 1: # tampilkan menu utama 
                showFarmList()
            elif noMenu == 2: # update data
                print("\nKamu bisa memperbarui data kandang kamu disini\n")
                showUpdateMenu()
            elif noMenu == 3: # tambah data
                print("\nKamu bisa menambah data kandang kamu disini\n")   
                showAddMenu()
            elif noMenu == 4: # hapus data
                print("\nKamu bisa menghapus data kandang kamu disini\n")
                showDeleteMenu()
            elif noMenu == 5: # penjualan livebird
                print("\nSekarang aku akan membantumu membuat penawaran penjualan ayam kamu~\n")
                showSellMenu()
            elif noMenu == 6: # log out
                quest = input("Apakah kamu yakin? (y/n): ").lower()
                if quest == "n":
                    continue
                elif quest == "y":
                    print("\nTerima kasih, sampai berjumpa lagi!\n")
                    break
                else:
                    print("\nerror: masukkan y atau n\n")
            else:
                print("\nMenu tidak ditemukan.\n")
        except ValueError:
            print("\nMasukkan angka saja!\n")
    


        
        
       
        
