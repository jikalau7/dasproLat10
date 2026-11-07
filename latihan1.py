import numpy as np

suhu = np.array([30, 32, 28, 35, 31,28, 29, 33, 34, 30])
suhu_fahrenheit = (suhu * 9/5) + 32

print("Suhu dalam Celsius:", suhu)
print("Suhu dalam Fahrenheit:", suhu_fahrenheit)