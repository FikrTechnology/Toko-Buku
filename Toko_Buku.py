data_buku = [
    'DP-250,Dasar Pemrograman,75000',
    'PSI-618,Penelitian Sistem Informasi,50000',
    'RPL-956,Rekayasa Perangkat Lunak,65000',
    'MPPL-247,Manajemen Proyek Perangkat Lunak,70000',
    'SSP-199,Sistem Pakar,85000',
    'DMB-435,Dasar Manajemen & Bisnis,90000',
    'JRK-996,Jaringan Komputer,65000',
    'STD-310,Struktur Data,55000',
    'WP1-699,Web Programming I,95000',
    'WP2-682,Web Programming II,105000'
]

list_Buku = []
disc = 0
subTotal2 = 0

def receipt():
    try:
        global disc
        global subTotal2

        print('='*100)
        print(' '*50+'Receipt')
        print('='*100)
        print('Kasir    : Muhammad Fikrie')
        print('NIM      : 17220207')
        print('-'*100)

        print('\n')
        print(f"{'Kode Buku':10} | {'Nama Buku':35} | {'Qty':5} | {'Harga Satuan':20} | {'Subtotal':20}")
        print('-'*100)

        for index, data in enumerate(list_Buku):
            data_break = data.split(',')
            codeBook = data_break[0]
            bookName = data_break[1]
            qty = data_break[2]
            harga = data_break[3]
            subTotal = data_break[4]
            disc += int(data_break[5])
            subTotal2 += int(subTotal)

            print(f"{codeBook:10} | {bookName:35} | {qty:5} | {harga:20} | {subTotal:20}")

        if subTotal2 > 500000:
            disc_True = int(subTotal2 * 0.03)
            disc = disc + disc_True
            subTotal2 = subTotal2 - disc_True

        pajak = int(subTotal2 * 0.1)
        total = subTotal2 + pajak

        print('\n')
        print('-'*100)
        print(' '*60+'Disc          : Rp'+str(disc))
        print(' '*60+'Sub Total     : Rp'+str(subTotal2))
        print(' '*60+'PPn           : Rp'+str(pajak))
        print(' '*60+'Total         : Rp'+str(total))


        while True:
            inp = input('Ingin Melanjutkan Pemesanan? [Y/N] ').upper()

            if inp == 'Y':
                list_Buku.clear()
                disc = 0
                subTotal2 = 0
                menu()
            elif inp == 'N':
                exit()
            else:
                print('Inputan tidak sesuai')
    except ValueError:
        print('Gagal Membuat Receipt')

def menu():
    print('='*100)
    print(' '*40+'Selamat Datang di Toko Buku')
    print('='*100)
    print('\n')

    print(f"{'Kode Buku':20} | {'Nama Buku':50} | {'Harga':30}")
    print('-'*100)

    for data in data_buku:
        data_break = data.split(',')
        kode_buku = data_break[0]
        nama_buku = data_break[1]
        harga = data_break[2]
        # list_Buku.append(kode_buku)

        print(f"{kode_buku:20} | {nama_buku:50} | {harga:30}")

    print('\n')
    print('='*100)
    print('\n')

    choose_book = input('Silahkan Masukkan Kode Buku : ').upper()

    try:
        quantity = int(input('Buku yang ingin di beli : '))

        len_dataBuku = 0

        for data in data_buku:
            data_break = data.split(',')
            kode_buku = data_break[0]
            nama_buku = data_break[1]
            harga = int(data_break[2])

            if len(choose_book) == len(kode_buku) and kode_buku.__contains__(choose_book):
                if quantity > 2:
                    disc = int((quantity * harga) * 0.05)
                    subTotal = int((quantity * harga) - disc)
                    list_Buku.append(f'{kode_buku},{nama_buku},{quantity},{harga},{subTotal},{disc}')
                else:
                    disc = 0
                    subTotal = int(quantity * harga)
                    list_Buku.append(f'{kode_buku},{nama_buku},{quantity},{harga},{subTotal},{disc}')

                while True:
                    inp = input('Cetak Receipt ? [Y/N] ').upper()
                    if inp == 'Y':
                        receipt()
                        break
                    elif inp == 'N':
                        menu()
                    else:
                        print('inputan tidak sesuai')
            else:
                pass

        while True:
            print('Kode buku tidak di temukan!!')
            inp = input('Ingin Melanjutkan ? [Y/N] ').upper()
            if inp == 'Y':
                menu()
            elif inp == 'N':
                break
            else:
                print('inputan tidak sesuai')
        
    except ValueError:
        print('Inputan yang anda masukkan salah')


menu()