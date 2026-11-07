import numpy as np

nilaiUjian = np.array([90, 75, 85, 95, 70, 88, 92, 78, 84, 91, 76, 89, 82, 87, 93, 79, 81, 86, 94, 77, 83, 90, 88, 85, 92, 80, 89, 91, 84, 87])
terbesar = np.sort(nilaiUjian)[::-1][:5]  # Mengambil 5 nilai terbesar
print("5 Nilai Terbesar:", terbesar)