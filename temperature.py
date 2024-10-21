def konversi_suhu(temp, unit):
    if unit.upper() == 'C':
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    elif unit.upper() == 'F':
        return (temp - 32) * 5/9  # Fahrenheit to Celsius
    else:
        raise ValueError("Unit tidak valid. Gunakan 'C' atau 'F'.")

# Input dari pengguna
temp = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan unit suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ")

# Menghitung dan mencetak hasil konversi
try:
    hasil = konversi_suhu(temp, unit)
    print(f"Hasil konversi: {hasil:.2f} {'F' if unit.upper() == 'C' else 'C'}")
except ValueError as e:
    print(e)

