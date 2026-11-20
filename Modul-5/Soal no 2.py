def cek_palindrom(kata):

    kata_bersih = kata.lower()
    
    if kata_bersih == kata_bersih[::-1]:
        return True
        print(kata_bersih)
    else:
        return False
        print(kata_bersih)

input_kata = input("Masukkan kata: ")

hasil_cek = cek_palindrom(input_kata)

print(hasil_cek)
if hasil_cek == True:
    print(f"Kata '{input_kata}' merupakan kata palindrom!")
else:
    print(f"Kata '{input_kata}' BUKAN merupakan kata palindrom.")