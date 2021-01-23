import numpy as np 
import matplotlib.pyplot as plt
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="bismillah"
)

print("===============SELAMAT DATANG DI APLIKASI PEMBAYARAN SPP===============")
def create():
    cursor = db.cursor()
    nis = int(input("Masukkan NIS anda:"))
    nama = input("Masukkan Nama anda:")
    ttl = input("Masukkan TTL anda:")
    kelas = int(input("Masukkan Kelas anda:"))
    jenjang_sekolah = input("Masukkan Jenjang Sekolah:")
    bulan_pembayaran = input("Masukkan Bulan Pembayaran:")
    bayaran = int(input("Masukkan Pembayaran anda:"))
    sql = "INSERT INTO pembayaran (nis,nama,ttl,kelas,jenjang_sekolah,bulan_pembayaran,bayaran) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (nis,nama,ttl,kelas,jenjang_sekolah,bulan_pembayaran,bayaran)
    cursor.execute(sql, val)

    db.commit()

    print("{} data ditambahkan".format(cursor.rowcount))

def read():
    pilih2 = input("Mau lihat data?[y/n]:")
    cursor = db.cursor()
    if pilih2 == "y":
        sql = "SELECT * FROM pembayaran"
        cursor.execute(sql)
        results = cursor.fetchall()

        if cursor.rowcount < 1:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)
    else:
        mainMenu()

def update():
    cursor = db.cursor()
    nis = int(input("Masukkan NIS data yang ingin diubah:"))
    nama = input("Update Nama:")
    ttl = input("Update TTL:")
    kelas = int(input("Update Kelas:"))
    jenjang_sekolah = input("Update Jenjang Sekolah:")
    bulan_pembayaran = input("Update Bulan Pembayaran:")
    bayaran = int(input("Update Pembayaran:"))

    sql = "UPDATE pembayaran SET nama=%s, ttl=%s, kelas=%s, jenjang_sekolah=%s, bulan_pembayaran=%s, bayaran=%s  WHERE nis=%s"
    val = (nama,ttl,kelas,jenjang_sekolah,bulan_pembayaran,bayaran,nis)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

def delete():
    cursor = db.cursor()
    nis = int(input("Masukkan NIS data yang ingin dihapus:"))
    sql = "DELETE FROM pembayaran WHERE nis=%s"
    val = (nis,)
    cursor.execute(sql, val)

    db.commit()

    print("{} data dihapus".format(cursor.rowcount))

def datvistotalpemasukantiapjenjang():
    cursor = db.cursor()
    sql = "SELECT sum(bayaran) from pembayaran where jenjang_sekolah = 'SD' group by bulan_pembayaran"
    cursor.execute(sql)
    hasil = cursor.fetchall() 
    
    bulan = []
    sd = []
    for a in hasil:
        print(a)
        bulan.append(a[0])
        sd.append(a[0])
    print(sd)

    cursor = db.cursor()
    sql = "SELECT sum(bayaran) from pembayaran where jenjang_sekolah = 'SMP' group by bulan_pembayaran"
    cursor.execute(sql)
    hasil = cursor.fetchall()
    
    bulan = []
    smp = []
    for a in hasil:
        print(a)
        bulan.append(a[0])
        smp.append(a[0])
    print(smp)
  
    cursor = db.cursor()
    sql = "SELECT sum(bayaran) from pembayaran where jenjang_sekolah = 'SMA' group by bulan_pembayaran"
    cursor.execute(sql)
    hasil = cursor.fetchall() 
    
    bulan = []
    sma = []
    for a in hasil:
        print(a)
        bulan.append(a[0])
        sma.append(a[0])
    print(sma)

    labels = ['Agustus','April','Desember','Februari','Januari','Juli','Juni','Maret','Mei','November','Oktober','September']
    x = np.arange(len(labels)) 
    width = 0.1
    fig, ax = plt.subplots()
    rects1 = ax.bar(x + width/2, sd, width, label='Total pemasukan sd', color = 'deepskyblue')
    rects2 = ax.bar(x + width+width/2, smp, width, label='Total pemasukan smp',color = 'lime')
    rects3 = ax.bar(x + width+width+width/2, sma, width, label='Total pemasukan sma',color = 'chocolate')
   
    ax.set_ylabel('Jumlah')
    ax.set_xlabel('Bulan')
    ax.set_title('Data Visualisasi Pemasukan per Jenjang tiap bulan')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.setp(rects1, color='deepskyblue')
    plt.setp(rects2, color='lime')
    plt.setp(rects3, color='chocolate')


    fig.tight_layout()
    plt.show()

    
def datvisjenjangsekolah():
    cursor=db.cursor()
    sql = "SELECT jenjang_sekolah,count(jenjang_sekolah) FROM pembayaran GROUP BY jenjang_sekolah"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    js = []
    jenjang_sekolah = []
    for a in results:
      print(a)
      js.append(a[0])
      jenjang_sekolah.append(int(a[1]))

    labels = js
    data = jenjang_sekolah

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, data, width, color="skyblue")

    ax.set_ylabel('Banyak data')
    ax.set_title('Total Jenjang Sekolah')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    fig.tight_layout()

    plt.show()


def datvispembayaran():
    cursor = db.cursor()
    sql = "SELECT bulan_pembayaran,sum(bayaran) FROM pembayaran GROUP BY bulan_pembayaran"
    cursor.execute(sql)
    results = cursor.fetchall()

    bulan = []
    bayaran = []
    for a in results:
      print(a)
      bulan.append(a[0])
      bayaran.append(int(a[1]))

    labels = bulan
    data = bayaran

    x = np.arange(len(labels))
    width = 0.35 

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, data, width, color="skyblue")

    ax.set_ylabel('Bayaran')
    ax.set_title('Total Pembayaran Perbulan')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    fig.tight_layout()

    plt.show()

def datvisjenjangsekolahperbulan():

    cursor = db.cursor()
    sql = "SELECT count(jenjang_sekolah) from pembayaran where jenjang_sekolah = 'SD' group by bulan_pembayaran"
    cursor.execute(sql)
    hasil = cursor.fetchall() 
    
    bulan = []
    csd = []
    for a in hasil:
        print(a)
        bulan.append(a[0])
        csd.append(a[0])
    print('sd',csd)

    cursor = db.cursor()
    sql = "SELECT count(jenjang_sekolah) from pembayaran where jenjang_sekolah = 'SMP' group by bulan_pembayaran"
    cursor.execute(sql)
    hasil = cursor.fetchall() 
    
    bulan = []
    csmp = []
    for a in hasil:
        print(a)
        bulan.append(a[0])
        csmp.append(a[0])
    print(csmp)

    cursor = db.cursor()
    sql = "SELECT count(jenjang_sekolah) from pembayaran where jenjang_sekolah = 'SMA' group by bulan_pembayaran"
    cursor.execute(sql)
    hasil = cursor.fetchall() 
    
    bulan = []
    csma = []
    for a in hasil:
        print(a)
        bulan.append(a[0])
        csma.append(a[0])
    print(csma)

    labels = ['Agustus','April','Desember','Februari','Januari','Juli','Juni','Maret','Mei','November','Oktober','September']
    x = np.arange(len(labels)) 
    width = 0.1
    fig, ax = plt.subplots()
    rects4 = ax.bar(x + width+width+width+width/2, csd, width, label='Jumlah jenjang sekolah sd', color = 'blue')
    rects5 = ax.bar(x + width+width+width+width+width/2, csmp, width, label='Jumlah jenjang sekolah smp',color = 'purple')
    rects6 = ax.bar(x + width+width+width+width+width+width/2, csma, width, label='Jumlah jenjang sekolah sma',color = 'orange')
    
    ax.set_ylabel('Jumlah')
    ax.set_xlabel('Bulan')
    ax.set_title('Data Visualisasi Jumlah Jenjang Sekolah perBulan')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.setp(rects4, color='blue')
    plt.setp(rects5, color='purple')
    plt.setp(rects6, color='orange')


    fig.tight_layout()
    plt.show()

def mainMenu():
    menu = 0
    while menu != 7:
        print("---------------------------------------------")
        print("1. Tambah data spp")
        print("2. Lihat data spp")
        print("3. Perbarui data spp")
        print("4. Hapus data spp")
        print("5. Visualisasi data Total Pemasukan per Jenjang tiap Bulan")
        print("6. Visualisasi data Total Jenjang Sekolah")
        print("7. Visualisasi data Total Pembayaran/bulan")
        print("8. Visualisasi data Jumlah Jenjang Sekolah/bulan")
        print("0. Exit")
        pm = input("Masukkan no pilihan:")
        if pm == "1":
            create()
        elif pm == "2":
            read()
        elif pm == "3":
            update()
        elif pm == "4":
            delete()
        elif pm == "5":
            datvistotalpemasukantiapjenjang()
        elif pm == "6":
            datvisjenjangsekolah()
        elif pm == "7":
            datvispembayaran()
        elif pm == "8":
            datvisjenjangsekolahperbulan()
        else:
            exit()
mainMenu()