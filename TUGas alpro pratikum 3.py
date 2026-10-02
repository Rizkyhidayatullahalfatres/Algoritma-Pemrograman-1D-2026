jarak_satu_arah = 100
konsumsi_bbm = 40
sisa_bensin = 1.5
harga_per_liter = 10000

total_jarak = jarak_satu_arah * 2
total_kebutuhan_bbm = total_jarak / konsumsi_bbm
bbm_harus_dibeli = total_kebutuhan_bbm - sisa_bensin
total_biaya = bbm_harus_dibeli * harga_per_liter


print("Total jarak perjalanan (PP):", total_jarak, "km")
print("Total kebutuhan bahan bakar:", total_kebutuhan_bbm, "liter")
print("Bahan bakar yang harus dibeli:", bbm_harus_dibeli, "liter")
print("Total biaya bahan bakar: Rp", total_biaya)