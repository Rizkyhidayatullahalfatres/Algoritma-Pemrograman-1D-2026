undangan = set()
webinar_a = set()
webinar_b = set()

n1 = int(input("Jumlah undangan: "))
for i in range(n1):
    undangan.add(input("Nama undangan: "))

n2 = int(input("Jumlah peserta Webinar A: "))
for i in range(n2):
    webinar_a.add(input("Nama peserta A: "))

n3 = int(input("Jumlah peserta Webinar B: "))
for i in range(n3):
    webinar_b.add(input("Nama peserta B: "))

semua_peserta = webinar_a.union(webinar_b)
keduanya = webinar_a.intersection(webinar_b)
salah_satu = webinar_a.symmetric_difference(webinar_b)
tidak_hadir = undangan.difference(semua_peserta)

print("\nSemua peserta kedua webinar:", semua_peserta)
print("Hadir di keduanya:", keduanya)
print("Hanya hadir di salah satu:", salah_satu)
print("Undangan tidak hadir:", tidak_hadir)