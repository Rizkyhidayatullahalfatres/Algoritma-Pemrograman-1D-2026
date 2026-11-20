inventaris_pc = []

jumlah = int(input("Masukkan jumlah input: "))

for i in range(jumlah):
    print("PC ke-" + str(i + 1))
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    
    pc = [nama, status, ram]
    inventaris_pc.append(pc)

print("\nHasil Evaluasi Seluruh PC:")
for pc in inventaris_pc:
    nama_pc = pc[0]
    status_pc = pc[1]
    ram_pc = pc[2]
    
    try:
        ram_angka = int(ram_pc)
        if status_pc == "normal" and ram_angka >= 8:
            kelayakan = "Layak"
        else:
            kelayakan = "Tidak Layak"
    except:
        kelayakan = "Format RAM Kacau"
        
    print('{"PC": "' + nama_pc + '", "Status": "' + kelayakan + '"}')