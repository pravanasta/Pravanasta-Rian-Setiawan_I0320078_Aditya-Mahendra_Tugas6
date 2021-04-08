print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("====================       Mulai        ===================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")

# input
n = int(input("Banyaknya data yang ada yaitu: "))
data=[]
jumlah = 0

for i in range(0, n):
    x = float(input("Masukkan angka ke-%d: " % (i + 1)))
    data.append(x)
    jumlah += data[i]
    rata_rata = jumlah / n
print("Hasil rata-rata dari data: %g" % rata_rata)
    
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("===================       SELESAI        ==================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")