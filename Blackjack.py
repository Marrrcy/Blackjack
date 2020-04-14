# Josep Marcello
# 14 April 2020
# MIT License

# Program Blackjack
# Gim kecil-kecilan buat main blackjack

# KAMUS
# iContAmnt          : int
# iLanjut            : int
# iSkor              : int
# iAngka             : int
# iNilaiAs           : int
# iJumlahAs          : int
# sAngka             : string
# sGambar            : string
# sKartu             : string
# sAngkaKartu        : array of string
# sGambarKartu       : array of string
# sHands             : array of string
# gambarKartu        : function
# angkaKartu         : function
# gambar             : function
# angka              : function
# nilaiKartu         : function
# hands              : function
# shuffle            : function


# ALGORITMA
import random

print("Anda akan bermain blackjack, tujuan dari permainan ini adalah untuk menjumlahkan \nsemua kartu anda sehingga totalnya bernilai 21.")
print("Nilai kartu: \nAs: 1 atau 11 \n2,3,4,5,...,10: Bernilai dirinya sendiri \n10, Jack, Queen, King: 10")


def gambarKartu(x):
    if x == 1:
        return "Sekop"
    elif x == 2:
        return "Hati"
    elif x == 3:
        return "Keriting"
    else:
        return "Wajik"


def angkaKartu(x):
    global iJumlahAs
    if x in range(2, 11):
        return str(x)
    elif x == 1:
        iJumlahAs += 1
        return "As"
    elif x == 11:
        return "Jack"
    elif x == 12:
        return "Queen"
    else:
        return "King"


def gambar():
    return int(random.randint(1, 4))


def angka():
    return int(random.randint(1, 13))


def nilaiKartu(x):
    if x in range(10, 14):
        return 10
    elif x in range(1, 10):
        return x


def hands(x):
    print("==================================================================================\nKartu di tangan: ")
    for i in range(x):
        print(sHands[i])
    print("==================================================================================")


def shuffle():
    global iSkor
    iAngka = angka()
    iSkor = iSkor + nilaiKartu(iAngka)
    sAngka = angkaKartu(iAngka)
    sGambar = gambarKartu(gambar())
    sAngkaKartu.append(sAngka)
    sGambarKartu.append(sGambar)


#Inisialisasi variabel dan kartu di tangan
sHands = []
sAngkaKartu = []
sGambarKartu = []
iSkor = 0
iContAmnt = 2
iJumlahAs = 0

#Membagikan kartu ke tangan pemain
for i in range(2):
    shuffle()
    sKartu = str(sAngkaKartu[i]) + " " + str(sGambarKartu[i])
    sHands.append(sKartu)

#Ngeprint kartu di tangan
hands(iContAmnt)

iLanjut = int(input("Lanjut (tekan 1)? "))

while iLanjut == 1:
    iContAmnt += 1
    while True:
        shuffle()
        sKartu = str(sAngkaKartu[iContAmnt - 1]) + " " + str(sGambarKartu[iContAmnt - 1])
        if (sKartu in sHands):
            sKartu = shuffle()
        else:
            sHands.append(sKartu)
            break
    hands(iContAmnt)
    iLanjut = int(input("Lanjut (tekan 1)? "))

if ("As" in sAngkaKartu):
    for i in range(iJumlahAs):
        iNilaiAs = int(input("Ingin berapa nilai kartu as ke-"+str(i+1)+" anda? Tekan 1 untuk 1, selain itu 11: "))
        if (iNilaiAs != 1):
            iSkor = iSkor + 10

print("Skor anda: ", iSkor)

if (iSkor == 20 or iSkor == 21):
    print("Anda menang!")
else:
    print("Anda kalah!")
