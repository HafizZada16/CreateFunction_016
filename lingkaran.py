import math

# Fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r**2  # Menghitung luas lingkaran

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung dan mencetak hasil luas lingkaran
hasil_luas = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {hasil_luas:.2f}")
