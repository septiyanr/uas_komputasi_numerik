# Definisikan nilai-nilai
V = 10  # Tegangan sumber (V)
R1 = 2  # Resistor 1 (Ω)
R2 = 3  # Resistor 2 (Ω)
R3 = 5  # Resistor 3 (Ω)

# Hitung total resistansi
R_total = R1 + R2 + R3

# Hitung arus total yang mengalir melalui rangkaian
I = V / R_total

# Hitung tegangan pada masing-masing resistor
V_R1 = I * R1
V_R2 = I * R2
V_R3 = I * R3

# Cetak hasil
print(f"Arus yang mengalir melalui rangkaian: {I} A")
print(f"Tegangan pada R1: {V_R1} V")
print(f"Tegangan pada R2: {V_R2} V")
print(f"Tegangan pada R3: {V_R3} V")
